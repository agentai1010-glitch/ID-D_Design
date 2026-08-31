import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="module")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def base_url():
    return "http://localhost:8000"

def test_services_page_loads_and_header(driver, base_url):
    driver.get(f"{base_url}/kiosk/services.html")
    time.sleep(0.5)

    # 1. Title & Branding
    assert "Services & Facilities" in driver.title
    assert "GRAND" in driver.page_source
    assert "METRO MALL" in driver.page_source

    # 2. Back button
    back_btn = driver.find_element(By.ID, "btnHeaderBack")
    assert back_btn.is_displayed()
    assert "Back" in back_btn.text

    # 3. Weather & Live Time
    weather = driver.find_element(By.ID, "headerWeather")
    assert "28°C" in weather.text
    clock = driver.find_element(By.ID, "kioskLiveTime")
    assert clock.is_displayed()

    # 4. Heading
    assert "SERVICES" in driver.page_source and "FACILITIES" in driver.page_source

def test_services_category_bar_rendering(driver, base_url):
    driver.get(f"{base_url}/kiosk/services.html")
    time.sleep(0.5)

    cat_all = driver.find_element(By.ID, "catAllServices")
    assert cat_all.is_displayed()
    assert "All Services" in cat_all.text
    assert "64" in cat_all.text

    cat_guest = driver.find_element(By.ID, "catGuestServices")
    assert "Guest Services" in cat_guest.text
    assert "12" in cat_guest.text

    cat_conv = driver.find_element(By.ID, "catConvenience")
    assert "Convenience" in cat_conv.text

    cat_fam = driver.find_element(By.ID, "catFamilyKids")
    assert "Family & Kids" in cat_fam.text

    cat_acc = driver.find_element(By.ID, "catAccessibility")
    assert "Accessibility" in cat_acc.text

def test_services_grid_and_right_panel_rendering(driver, base_url):
    driver.get(f"{base_url}/kiosk/services.html")
    time.sleep(0.5)

    grid = driver.find_element(By.ID, "servicesGridContainer")
    assert grid.is_displayed()
    cards = grid.find_elements(By.CSS_SELECTOR, ".service-facility-card")
    assert len(cards) == 8

    # Specific cards
    concierge = driver.find_element(By.CSS_SELECTOR, ".service-facility-card[data-id='concierge']")
    assert "Concierge" in concierge.text
    assert "Ground Floor" in concierge.text

    wheelchair = driver.find_element(By.CSS_SELECTOR, ".service-facility-card[data-id='wheelchair']")
    assert "Wheelchair" in wheelchair.text

    # Right Column Cards
    assert "Need Immediate Help?" in driver.page_source
    assert "Guest Assistance" in driver.page_source
    assert "Mall Information" in driver.page_source
    assert "Parking Information" in driver.page_source
    assert "Request a Service" in driver.page_source

def test_services_category_filtering(driver, base_url):
    driver.get(f"{base_url}/kiosk/services.html")
    time.sleep(0.3)

    concierge = driver.find_element(By.CSS_SELECTOR, ".service-facility-card[data-id='concierge']")
    lockers = driver.find_element(By.CSS_SELECTOR, ".service-facility-card[data-id='lockers']")
    wheelchair = driver.find_element(By.CSS_SELECTOR, ".service-facility-card[data-id='wheelchair']")

    # 1. Click Guest Services
    driver.find_element(By.ID, "catGuestServices").click()
    time.sleep(0.3)
    assert concierge.is_displayed()
    assert not lockers.is_displayed()

    # 2. Click Accessibility
    driver.find_element(By.ID, "catAccessibility").click()
    time.sleep(0.3)
    assert wheelchair.is_displayed()
    assert not concierge.is_displayed()

    # 3. Click All Services
    driver.find_element(By.ID, "catAllServices").click()
    time.sleep(0.3)
    assert concierge.is_displayed()
    assert lockers.is_displayed()
    assert wheelchair.is_displayed()

def test_services_search_simulation(driver, base_url):
    driver.get(f"{base_url}/kiosk/services.html")
    time.sleep(0.3)

    search_inp = driver.find_element(By.ID, "servicesSearchInput")
    search_inp.send_keys("Wheelchair")
    time.sleep(0.3)

    wheelchair = driver.find_element(By.CSS_SELECTOR, ".service-facility-card[data-id='wheelchair']")
    concierge = driver.find_element(By.CSS_SELECTOR, ".service-facility-card[data-id='concierge']")

    assert wheelchair.is_displayed()
    assert not concierge.is_displayed()

    # Empty search query
    search_inp.clear()
    search_inp.send_keys("nonexistentservice123")
    time.sleep(0.3)

    empty_notice = driver.find_element(By.ID, "emptyServicesNotice")
    assert empty_notice.is_displayed()
    assert "No Services Found" in empty_notice.text

    # Reset
    driver.find_element(By.XPATH, "//div[@id='emptyServicesNotice']//button[text()='Reset Filters']").click()
    time.sleep(0.3)
    assert not empty_notice.is_displayed()
    assert concierge.is_displayed()

def test_service_details_modal_and_take_me_there(driver, base_url):
    driver.get(f"{base_url}/kiosk/services.html")
    time.sleep(0.3)

    # Click Concierge View Details
    driver.find_element(By.CSS_SELECTOR, ".service-facility-card[data-id='concierge']").click()
    time.sleep(0.3)

    modal = driver.find_element(By.ID, "serviceDetailsModal")
    assert modal.is_displayed()
    assert "Concierge" in modal.text
    assert "Available Now" in modal.text

    # Verify action button
    btn_nav = driver.find_element(By.ID, "btnServiceTakeMeThere")
    assert btn_nav.is_displayed()
    assert "Take Me There" in btn_nav.text

    driver.find_element(By.XPATH, "//div[@id='serviceDetailsModal']//i[contains(@class,'fa-xmark')]").click()
    time.sleep(0.3)
    assert not modal.is_displayed()

def test_immediate_help_and_request_assistance_flow(driver, base_url):
    driver.get(f"{base_url}/kiosk/services.html")
    time.sleep(0.3)

    # 1. Connect Now Immediate Help
    driver.find_element(By.ID, "btnConnectNow").click()
    time.sleep(0.3)

    help_modal = driver.find_element(By.ID, "immediateHelpModal")
    assert help_modal.is_displayed()
    assert "Connecting to Guest Concierge" in help_modal.text

    driver.find_element(By.XPATH, "//div[@id='immediateHelpModal']//button[text()='Dismiss']").click()
    time.sleep(0.3)
    assert not help_modal.is_displayed()

    # 2. Request a Service Flow
    driver.find_element(By.ID, "btnRequestServiceNow").click()
    time.sleep(0.3)

    req_modal = driver.find_element(By.ID, "serviceRequestModal")
    assert req_modal.is_displayed()
    assert "Request Assistance" in req_modal.text

    # Submit Request
    driver.find_element(By.ID, "btnSubmitServiceRequest").click()
    time.sleep(0.3)

    confirm_modal = driver.find_element(By.ID, "serviceConfirmModal")
    assert confirm_modal.is_displayed()
    assert "Request Confirmed!" in confirm_modal.text
    assert "Ticket #SR-" in confirm_modal.text

    driver.find_element(By.XPATH, "//div[@id='serviceConfirmModal']//button[text()='Done']").click()
    time.sleep(0.3)
    assert not confirm_modal.is_displayed()

def test_mall_information_shortcuts_interaction(driver, base_url):
    driver.get(f"{base_url}/kiosk/services.html")
    time.sleep(0.3)

    # Click Parking Information
    driver.find_element(By.ID, "shortcutParking").click()
    time.sleep(0.3)

    modal = driver.find_element(By.ID, "serviceDetailsModal")
    assert modal.is_displayed()
    assert "Parking" in modal.text

    driver.find_element(By.XPATH, "//div[@id='serviceDetailsModal']//i[contains(@class,'fa-xmark')]").click()
    time.sleep(0.3)
    assert not modal.is_displayed()

    # Click ATM & Banking
    driver.find_element(By.ID, "shortcutATM").click()
    time.sleep(0.3)

    assert modal.is_displayed()
    assert "ATM" in modal.text
    driver.find_element(By.XPATH, "//div[@id='serviceDetailsModal']//i[contains(@class,'fa-xmark')]").click()
    time.sleep(0.3)

def test_strict_kiosk_services_boundaries(driver, base_url):
    driver.get(f"{base_url}/kiosk/services.html")
    time.sleep(0.3)

    body_text = driver.find_element(By.TAG_NAME, "body").text.lower()
    assert "janitorial dispatch cms" not in body_text
    assert "security patrol analytics" not in body_text
    assert "hvac maintenance logs" not in body_text
    assert "facility cost chart" not in body_text
