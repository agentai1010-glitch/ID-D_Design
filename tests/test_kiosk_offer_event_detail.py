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

# =========================================================================
# 1. OFFER DETAIL TESTS
# =========================================================================
def test_offer_detail_page_loads_and_branding(driver, base_url):
    driver.get(f"{base_url}/kiosk/offer_detail.html?id=deal-nike-1&from=offers")
    time.sleep(0.5)

    assert "Offer Details" in driver.title or "Grand Metro Mall" in driver.title
    assert "GRAND METRO MALL" in driver.page_source
    assert "CELEBRATE EVERYDAY" in driver.page_source
    assert "28°C" in driver.page_source

def test_offer_detail_nike_metadata_and_terms(driver, base_url):
    driver.get(f"{base_url}/kiosk/offer_detail.html?id=deal-nike-1&from=offers")
    time.sleep(0.5)

    badge = driver.find_element(By.ID, "offerHeroDiscountBadge").text
    headline = driver.find_element(By.ID, "offerHeroHeadline").text
    code = driver.find_element(By.ID, "offerPromoCode").text
    summary = driver.find_element(By.ID, "offerSummary").text
    terms = driver.find_elements(By.CSS_SELECTOR, "#offerTermsList li")

    assert "40% OFF" in badge
    assert "Running Shoes" in headline
    assert "RUNFAST40" in code
    assert "Pegasus" in summary or "Nike" in summary
    assert len(terms) >= 3

def test_offer_detail_take_me_to_store(driver, base_url):
    driver.get(f"{base_url}/kiosk/offer_detail.html?id=deal-nike-1&from=offers")
    time.sleep(0.3)

    btn = driver.find_element(By.ID, "btnTakeMeToStore")
    assert btn.is_displayed()
    btn.click()
    time.sleep(0.5)

    assert "map.html" in driver.current_url

def test_offer_detail_dynamic_switching(driver, base_url):
    driver.get(f"{base_url}/kiosk/offer_detail.html?id=deal-nike-1&from=offers")
    time.sleep(0.3)

    # Click on another offer card in left sidebar
    left_cards = driver.find_elements(By.CSS_SELECTOR, ".offer-list-card")
    assert len(left_cards) >= 3

    # Click Zara offer
    left_cards[2].click()
    time.sleep(0.4)

    # Verify updated dynamically
    code = driver.find_element(By.ID, "offerPromoCode").text
    assert "RUNFAST40" not in code or "ZARAGALA" in driver.page_source

def test_offer_detail_back_button(driver, base_url):
    # From Store
    driver.get(f"{base_url}/kiosk/offer_detail.html?id=deal-nike-1&from=store&storeId=nike")
    time.sleep(0.3)
    driver.find_element(By.ID, "btnOfferBack").click()
    time.sleep(0.5)
    assert "detail.html" in driver.current_url

    # From Offers
    driver.get(f"{base_url}/kiosk/offer_detail.html?id=deal-nike-1&from=offers")
    time.sleep(0.3)
    driver.find_element(By.ID, "btnOfferBack").click()
    time.sleep(0.5)
    assert "offers.html" in driver.current_url

# =========================================================================
# 2. EVENT DETAIL TESTS
# =========================================================================
def test_event_detail_page_loads_and_branding(driver, base_url):
    driver.get(f"{base_url}/kiosk/event_detail.html?id=armaan&from=events")
    time.sleep(0.5)

    assert "Event Details" in driver.title or "Grand Metro Mall" in driver.title
    assert "GRAND METRO MALL" in driver.page_source

def test_event_detail_armaan_metadata_and_schedule(driver, base_url):
    driver.get(f"{base_url}/kiosk/event_detail.html?id=armaan&from=events")
    time.sleep(0.5)

    title = driver.find_element(By.ID, "eventHeroTitle").text
    venue = driver.find_element(By.ID, "eventVenue").text
    date = driver.find_element(By.ID, "eventDate").text
    timeline_items = driver.find_elements(By.CSS_SELECTOR, ".timeline-item-row")
    guidelines = driver.find_elements(By.CSS_SELECTOR, "#eventGuidelinesList li")

    assert "Armaan Malik" in title
    assert "Main Atrium" in venue
    assert "12 Sep" in date
    assert len(timeline_items) >= 3
    assert len(guidelines) >= 2

def test_event_detail_take_me_to_venue(driver, base_url):
    driver.get(f"{base_url}/kiosk/event_detail.html?id=armaan&from=events")
    time.sleep(0.3)

    btn = driver.find_element(By.ID, "btnTakeMeToVenue")
    assert btn.is_displayed()
    btn.click()
    time.sleep(0.5)

    assert "map.html" in driver.current_url
    assert "atrium" in driver.current_url

def test_event_detail_rsvp_booking_modal(driver, base_url):
    driver.get(f"{base_url}/kiosk/event_detail.html?id=armaan&from=events")
    time.sleep(0.3)

    driver.find_element(By.CSS_SELECTOR, ".btn-event-rsvp").click()
    time.sleep(0.4)

    modal = driver.find_element(By.ID, "rsvpBookingModal")
    assert "open" in modal.get_attribute("class")

    driver.find_element(By.ID, "btnConfirmRSVP").click()
    time.sleep(0.5)

    success = driver.find_element(By.ID, "rsvpSuccessState")
    assert success.is_displayed()

# =========================================================================
# 3. CROSS-WORKFLOW DEEP LINKING
# =========================================================================
def test_cross_workflow_offer_and_event_navigation(driver, base_url):
    # 1. Offers listing -> Offer detail
    driver.get(f"{base_url}/kiosk/offers.html")
    time.sleep(0.4)
    driver.execute_script("openOfferDetailsModal('deal-nike-1');")
    time.sleep(0.5)
    assert "offer_detail.html" in driver.current_url

    # 2. Events listing -> Event detail
    driver.get(f"{base_url}/kiosk/events.html")
    time.sleep(0.4)
    driver.execute_script("openEventDetailsModal('armaan');")
    time.sleep(0.5)
    assert "event_detail.html" in driver.current_url

def test_strict_kiosk_boundaries(driver, base_url):
    driver.get(f"{base_url}/kiosk/offer_detail.html?id=deal-nike-1&from=offers")
    time.sleep(0.3)

    body_text = driver.find_element(By.TAG_NAME, "body").text.lower()
    assert "crm marketing suite" not in body_text
    assert "merchant payout gateway" not in body_text
    assert "admin campaign cms" not in body_text
