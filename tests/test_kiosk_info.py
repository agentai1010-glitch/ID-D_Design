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

def test_info_page_loads_and_header(driver, base_url):
    driver.get(f"{base_url}/kiosk/info.html")
    time.sleep(0.5)

    # 1. Title & Branding
    assert "Mall Information" in driver.title
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
    assert "MALL INFORMATION" in driver.page_source and "EXPERIENCE CENTRE" in driver.page_source

def test_info_six_section_navigation_bar(driver, base_url):
    driver.get(f"{base_url}/kiosk/info.html")
    time.sleep(0.5)

    sec_centre = driver.find_element(By.ID, "secCentreInfo")
    assert sec_centre.is_displayed()
    assert "Centre Information" in sec_centre.text

    sec_gallery = driver.find_element(By.ID, "secGallery")
    assert "Gallery" in sec_gallery.text

    sec_booklet = driver.find_element(By.ID, "secBooklet")
    assert "Mall Booklet" in sec_booklet.text

    sec_exp = driver.find_element(By.ID, "secExperience")
    assert "Experience Centre" in sec_exp.text

    sec_guide = driver.find_element(By.ID, "secVisitorGuide")
    assert "Visitor Guide" in sec_guide.text

    sec_help = driver.find_element(By.ID, "secHelpSupport")
    assert "Help & Support" in sec_help.text

def test_centre_information_cards_rendering(driver, base_url):
    driver.get(f"{base_url}/kiosk/info.html")
    time.sleep(0.5)

    assert "About the Mall" in driver.page_source
    assert "Mall Timings" in driver.page_source
    assert "Parking Information" in driver.page_source
    assert "How to Reach" in driver.page_source

    assert "GALLERY" in driver.page_source
    assert "MALL BOOKLET" in driver.page_source
    assert "EXPERIENCE CENTRE" in driver.page_source

def test_quick_information_and_latest_updates(driver, base_url):
    driver.get(f"{base_url}/kiosk/info.html")
    time.sleep(0.5)

    # Quick Information
    assert "QUICK INFORMATION" in driver.page_source
    assert "Mall Directory" in driver.page_source
    assert "Store List" in driver.page_source
    assert "ATM & Banking" in driver.page_source
    assert "Restrooms" in driver.page_source
    assert "First Aid" in driver.page_source
    assert "Wi-Fi Information" in driver.page_source

    # Latest Updates
    assert "LATEST UPDATES" in driver.page_source
    assert "New Stores Coming Soon" in driver.page_source
    assert "Season of Celebrations" in driver.page_source
    assert "Weekend Entertainment" in driver.page_source

def test_info_card_modal_and_take_me_there(driver, base_url):
    driver.get(f"{base_url}/kiosk/info.html")
    time.sleep(0.3)

    # Click on About the Mall card
    driver.find_element(By.XPATH, "//div[contains(@class,'info-card-name') and text()='About the Mall']").click()
    time.sleep(0.3)

    modal = driver.find_element(By.ID, "infoDetailsModal")
    assert modal.is_displayed()
    assert "About Grand Metro Mall" in modal.text

    # Take Me There button
    btn_nav = driver.find_element(By.ID, "btnInfoTakeMeThere")
    assert btn_nav.is_displayed()
    assert "Take Me There" in btn_nav.text

    driver.find_element(By.XPATH, "//div[@id='infoDetailsModal']//i[contains(@class,'fa-xmark')]").click()
    time.sleep(0.3)
    assert not modal.is_displayed()

def test_digital_booklet_flip_viewer(driver, base_url):
    driver.get(f"{base_url}/kiosk/info.html")
    time.sleep(0.3)

    # Click Mall Booklet
    driver.find_element(By.ID, "secBooklet").click()
    time.sleep(0.3)

    modal = driver.find_element(By.ID, "bookletModal")
    assert modal.is_displayed()
    assert "Official Booklet" in modal.text
    assert "Page 1 of 4" in driver.find_element(By.ID, "bookletPageCounter").text

    # Next page
    driver.find_element(By.ID, "btnBookletNext").click()
    time.sleep(0.3)
    assert "Page 2 of 4" in driver.find_element(By.ID, "bookletPageCounter").text

    # Previous page
    driver.find_element(By.ID, "btnBookletPrev").click()
    time.sleep(0.3)
    assert "Page 1 of 4" in driver.find_element(By.ID, "bookletPageCounter").text

    driver.find_element(By.XPATH, "//div[@id='bookletModal']//i[contains(@class,'fa-xmark')]").click()
    time.sleep(0.3)
    assert not modal.is_displayed()

def test_virtual_tour_and_experience_centre(driver, base_url):
    driver.get(f"{base_url}/kiosk/info.html")
    time.sleep(0.3)

    # Click Experience Centre
    driver.find_element(By.ID, "secExperience").click()
    time.sleep(0.3)

    modal = driver.find_element(By.ID, "virtualTourModal")
    assert modal.is_displayed()
    assert "360° Virtual Walkthrough" in modal.text

    # Switch to Food Court spot
    driver.find_element(By.XPATH, "//div[@id='virtualTourModal']//button[text()='Food Court']").click()
    time.sleep(0.3)
    assert "Food Court" in driver.find_element(By.ID, "tourLocationBadge").text

    driver.find_element(By.XPATH, "//div[@id='virtualTourModal']//i[contains(@class,'fa-xmark')]").click()
    time.sleep(0.3)
    assert not modal.is_displayed()

def test_information_search_simulation(driver, base_url):
    driver.get(f"{base_url}/kiosk/info.html")
    time.sleep(0.3)

    inp = driver.find_element(By.ID, "infoSearchInput")
    inp.send_keys("parking")
    time.sleep(0.3)

    modal = driver.find_element(By.ID, "infoDetailsModal")
    assert modal.is_displayed()
    assert "Parking" in modal.text

    driver.find_element(By.XPATH, "//div[@id='infoDetailsModal']//i[contains(@class,'fa-xmark')]").click()
    time.sleep(0.3)

def test_strict_kiosk_info_boundaries(driver, base_url):
    driver.get(f"{base_url}/kiosk/info.html")
    time.sleep(0.3)

    body_text = driver.find_element(By.TAG_NAME, "body").text.lower()
    assert "cms article publisher" not in body_text
    assert "pageview analytics dashboard" not in body_text
    assert "content approval workflow" not in body_text
    assert "editorial queue" not in body_text
