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

def test_search_page_loads_and_header_elements(driver, base_url):
    driver.get(f"{base_url}/kiosk/search.html")
    time.sleep(0.5)

    # 1. Title & Grand Metro Mall logo
    assert "Search & Discovery" in driver.title
    assert "GRAND" in driver.page_source
    assert "METRO MALL" in driver.page_source

    # 2. Back button
    back_btn = driver.find_element(By.ID, "btnHeaderBack")
    assert back_btn.is_displayed()
    assert "Back" in back_btn.text

    # 3. Weather & Clock
    weather = driver.find_element(By.ID, "headerWeather")
    assert "28°C" in weather.text
    clock = driver.find_element(By.ID, "kioskLiveTime")
    assert clock.is_displayed()

def test_search_input_and_results_rendering(driver, base_url):
    driver.get(f"{base_url}/kiosk/search.html")
    time.sleep(0.5)

    # Search input exists and has default query
    search_inp = driver.find_element(By.ID, "kioskMainSearchInput")
    assert search_inp.get_attribute("value") == "adidas"

    # Verify Stores Section
    sec_stores = driver.find_element(By.ID, "sectionStores")
    assert sec_stores.is_displayed()
    assert "Adidas" in sec_stores.text
    assert "Adidas Originals" in sec_stores.text
    assert "Adidas Kids" in sec_stores.text

    # Verify Food Section
    sec_food = driver.find_element(By.ID, "sectionFood")
    assert sec_food.is_displayed()
    assert "Adidas Café" in sec_food.text
    assert "Adidas Treats" in sec_food.text

    # Verify Offers Section
    sec_offers = driver.find_element(By.ID, "sectionOffers")
    assert sec_offers.is_displayed()
    assert "Flat 30% Off" in sec_offers.text
    assert "Buy 2 Get 20% Off" in sec_offers.text

    # Verify Events Section
    sec_events = driver.find_element(By.ID, "sectionEvents")
    assert sec_events.is_displayed()
    assert "Adidas Run Club" in sec_events.text

def test_category_tabs_filtering(driver, base_url):
    driver.get(f"{base_url}/kiosk/search.html")
    time.sleep(0.5)

    sec_stores = driver.find_element(By.ID, "sectionStores")
    sec_food = driver.find_element(By.ID, "sectionFood")
    sec_offers = driver.find_element(By.ID, "sectionOffers")
    sec_events = driver.find_element(By.ID, "sectionEvents")

    # 1. Click Stores Tab
    driver.find_element(By.ID, "tabStores").click()
    time.sleep(0.2)
    assert sec_stores.is_displayed()
    assert not sec_food.is_displayed()
    assert not sec_offers.is_displayed()
    assert not sec_events.is_displayed()

    # 2. Click Food & Dining Tab
    driver.find_element(By.ID, "tabFood").click()
    time.sleep(0.2)
    assert not sec_stores.is_displayed()
    assert sec_food.is_displayed()
    assert not sec_offers.is_displayed()

    # 3. Click Offers Tab
    driver.find_element(By.ID, "tabOffers").click()
    time.sleep(0.2)
    assert sec_offers.is_displayed()
    assert not sec_stores.is_displayed()

    # 4. Click Events Tab
    driver.find_element(By.ID, "tabEvents").click()
    time.sleep(0.2)
    assert sec_events.is_displayed()
    assert not sec_stores.is_displayed()

    # 5. Restore All Results Tab
    driver.find_element(By.ID, "tabAllResults").click()
    time.sleep(0.2)
    assert sec_stores.is_displayed()
    assert sec_food.is_displayed()
    assert sec_offers.is_displayed()
    assert sec_events.is_displayed()

def test_empty_search_state(driver, base_url):
    driver.get(f"{base_url}/kiosk/search.html")
    time.sleep(0.3)

    search_inp = driver.find_element(By.ID, "kioskMainSearchInput")
    search_inp.clear()
    search_inp.send_keys("xyz123")
    time.sleep(0.3)

    empty_state = driver.find_element(By.ID, "emptySearchResults")
    assert empty_state.is_displayed()
    assert "No Results Found" in empty_state.text

    # Clear search
    driver.find_element(By.ID, "btnClearSearch").click()
    time.sleep(0.3)
    assert not empty_state.is_displayed()
    assert driver.find_element(By.ID, "searchResultsMainArea").is_displayed()

def test_search_filter_modal(driver, base_url):
    driver.get(f"{base_url}/kiosk/search.html")
    time.sleep(0.3)

    # Open Filters Modal
    driver.find_element(By.ID, "btnOpenFilters").click()
    time.sleep(0.3)

    modal = driver.find_element(By.ID, "searchFilterModal")
    assert modal.is_displayed()
    assert "Filter Search Results" in modal.text
    assert "CATEGORY" in modal.text.upper()
    assert "Fashion" in modal.text
    assert "Ground Floor" in modal.text

    # Close modal
    driver.find_element(By.XPATH, "//div[@id='searchFilterModal']//button[text()='Cancel']").click()
    time.sleep(0.3)
    assert not modal.is_displayed()

def test_store_details_and_navigation_handoff(driver, base_url):
    driver.get(f"{base_url}/kiosk/search.html")
    time.sleep(0.3)

    # Click first store card
    driver.find_element(By.CSS_SELECTOR, ".store-result-card").click()
    time.sleep(0.3)

    modal = driver.find_element(By.ID, "storeDetailsModal")
    assert modal.is_displayed()
    assert "Adidas" in modal.text
    assert "Ground Floor, G-12" in modal.text

    take_me_btn = driver.find_element(By.ID, "btnTakeMeThere")
    assert take_me_btn.is_displayed()
    assert "Take Me There" in take_me_btn.text

    # Close modal
    driver.find_element(By.XPATH, "//div[@id='storeDetailsModal']//button[text()='Close']").click()
    time.sleep(0.3)
    assert not modal.is_displayed()

def test_offer_and_event_modals(driver, base_url):
    driver.get(f"{base_url}/kiosk/search.html")
    time.sleep(0.3)

    # 1. Offer Modal
    driver.find_element(By.CSS_SELECTOR, ".offer-res-card").click()
    time.sleep(0.3)
    offer_modal = driver.find_element(By.ID, "offerDetailsModal")
    assert offer_modal.is_displayed()
    assert "Flat 30% Off" in offer_modal.text
    driver.find_element(By.XPATH, "//div[@id='offerDetailsModal']//button[text()='Close']").click()
    time.sleep(0.3)
    assert not offer_modal.is_displayed()

    # 2. Event Modal
    driver.find_element(By.CSS_SELECTOR, ".event-res-card").click()
    time.sleep(0.3)
    event_modal = driver.find_element(By.ID, "eventDetailsModal")
    assert event_modal.is_displayed()
    assert "Adidas Run Club" in event_modal.text
    driver.find_element(By.XPATH, "//div[@id='eventDetailsModal']//button[text()='Close']").click()
    time.sleep(0.3)
    assert not event_modal.is_displayed()

def test_strict_kiosk_search_boundaries(driver, base_url):
    driver.get(f"{base_url}/kiosk/search.html")
    time.sleep(0.3)

    body_text = driver.find_element(By.TAG_NAME, "body").text.lower()
    # Confirm no admin / analytics intrusion
    assert "analytics dashboard" not in body_text
    assert "conversion rate" not in body_text
    assert "cms editor" not in body_text
    assert "visitor count chart" not in body_text
