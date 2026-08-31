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

def test_offers_page_loads_and_header(driver, base_url):
    driver.get(f"{base_url}/kiosk/offers.html")
    time.sleep(0.5)

    # 1. Title & Branding
    assert "Offers & Deals" in driver.title
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
    assert "OFFERS" in driver.page_source and "DEALS" in driver.page_source

def test_offers_category_bar_rendering(driver, base_url):
    driver.get(f"{base_url}/kiosk/offers.html")
    time.sleep(0.5)

    cat_all = driver.find_element(By.ID, "catAllOffers")
    assert cat_all.is_displayed()
    assert "All Offers" in cat_all.text
    assert "124" in cat_all.text

    cat_fashion = driver.find_element(By.ID, "catFashionOffers")
    assert "Fashion" in cat_fashion.text
    assert "36" in cat_fashion.text

    cat_food = driver.find_element(By.ID, "catFoodOffers")
    assert "Food & Dining" in cat_food.text

    cat_life = driver.find_element(By.ID, "catLifestyleOffers")
    assert "Lifestyle" in cat_life.text

    cat_ent = driver.find_element(By.ID, "catEntertainmentOffers")
    assert "Entertainment" in cat_ent.text

def test_offers_grid_and_featured_cards_rendering(driver, base_url):
    driver.get(f"{base_url}/kiosk/offers.html")
    time.sleep(0.5)

    grid = driver.find_element(By.ID, "offersGridContainer")
    assert grid.is_displayed()
    cards = grid.find_elements(By.CSS_SELECTOR, ".offer-dual-card")
    assert len(cards) == 8

    # Specific cards
    adidas = driver.find_element(By.CSS_SELECTOR, ".offer-dual-card[data-id='adidas']")
    assert "Adidas" in adidas.text
    assert "30%" in adidas.text

    pvr = driver.find_element(By.CSS_SELECTOR, ".offer-dual-card[data-id='pvr']")
    assert "PVR Cinemas" in pvr.text
    assert "BUY 1" in pvr.text

    # Featured Deal card
    assert "Featured Deal" in driver.page_source
    assert "END OF SEASON" in driver.page_source
    assert "60%" in driver.page_source

    # Offers Near You
    assert "Offers Near You" in driver.page_source
    assert "ZARA" in driver.page_source
    assert "H&M" in driver.page_source

def test_offers_category_filtering(driver, base_url):
    driver.get(f"{base_url}/kiosk/offers.html")
    time.sleep(0.3)

    adidas = driver.find_element(By.CSS_SELECTOR, ".offer-dual-card[data-id='adidas']")
    pvr = driver.find_element(By.CSS_SELECTOR, ".offer-dual-card[data-id='pvr']")
    starbucks = driver.find_element(By.CSS_SELECTOR, ".offer-dual-card[data-id='starbucks']")

    # 1. Click Fashion
    driver.find_element(By.ID, "catFashionOffers").click()
    time.sleep(0.3)
    assert adidas.is_displayed()
    assert not pvr.is_displayed()
    assert not starbucks.is_displayed()

    # 2. Click Entertainment
    driver.find_element(By.ID, "catEntertainmentOffers").click()
    time.sleep(0.3)
    assert pvr.is_displayed()
    assert not adidas.is_displayed()

    # 3. Click Food & Dining
    driver.find_element(By.ID, "catFoodOffers").click()
    time.sleep(0.3)
    assert starbucks.is_displayed()
    assert not pvr.is_displayed()

    # 4. Click All Offers
    driver.find_element(By.ID, "catAllOffers").click()
    time.sleep(0.3)
    assert adidas.is_displayed()
    assert pvr.is_displayed()
    assert starbucks.is_displayed()

def test_offers_search_simulation(driver, base_url):
    driver.get(f"{base_url}/kiosk/offers.html")
    time.sleep(0.3)

    search_inp = driver.find_element(By.ID, "offersSearchInput")
    search_inp.send_keys("Adidas")
    time.sleep(0.3)

    adidas = driver.find_element(By.CSS_SELECTOR, ".offer-dual-card[data-id='adidas']")
    pvr = driver.find_element(By.CSS_SELECTOR, ".offer-dual-card[data-id='pvr']")

    assert adidas.is_displayed()
    assert not pvr.is_displayed()

    # Empty search query
    search_inp.clear()
    search_inp.send_keys("nonexistentoffer123")
    time.sleep(0.3)

    empty_notice = driver.find_element(By.ID, "emptyOffersNotice")
    assert empty_notice.is_displayed()
    assert "No Offers Found" in empty_notice.text

    # Reset
    driver.find_element(By.XPATH, "//div[@id='emptyOffersNotice']//button[text()='Reset Filters']").click()
    time.sleep(0.3)
    assert not empty_notice.is_displayed()
    assert adidas.is_displayed()

def test_offer_details_modal_and_handoff(driver, base_url):
    driver.get(f"{base_url}/kiosk/offers.html")
    time.sleep(0.3)

    # Click Adidas View Details
    driver.find_element(By.CSS_SELECTOR, ".offer-dual-card[data-id='adidas']").click()
    time.sleep(0.3)

    modal = driver.find_element(By.ID, "offerDetailsModal")
    assert modal.is_displayed()
    assert "Flat 30% Off on Footwear" in modal.text
    assert "ADIDAS30" in modal.text

    # Verify action buttons: View Store & Take Me There
    btn_store = driver.find_element(By.ID, "btnOfferHandoffStore")
    assert btn_store.is_displayed()
    assert "View Store" in btn_store.text

    btn_nav = driver.find_element(By.ID, "btnOfferTakeMeThere")
    assert btn_nav.is_displayed()
    assert "Take Me There" in btn_nav.text

    driver.find_element(By.XPATH, "//div[@id='offerDetailsModal']//i[contains(@class,'fa-xmark')]").click()
    time.sleep(0.3)
    assert not modal.is_displayed()

def test_featured_deal_and_near_you_interactions(driver, base_url):
    driver.get(f"{base_url}/kiosk/offers.html")
    time.sleep(0.3)

    # 1. Click Explore Now on Featured Deal
    driver.find_element(By.ID, "btnExploreFeaturedDeal").click()
    time.sleep(0.3)

    modal = driver.find_element(By.ID, "offerDetailsModal")
    assert modal.is_displayed()
    assert "ZARA" in modal.text or "Sale" in modal.text

    driver.find_element(By.XPATH, "//div[@id='offerDetailsModal']//i[contains(@class,'fa-xmark')]").click()
    time.sleep(0.3)
    assert not modal.is_displayed()

    # 2. Click Near You row (H&M)
    driver.find_element(By.XPATH, "//div[contains(@class,'near-you-item-row')]//div[text()='H&M']").click()
    time.sleep(0.3)

    assert modal.is_displayed()
    assert "H&M" in modal.text
    driver.find_element(By.XPATH, "//div[@id='offerDetailsModal']//i[contains(@class,'fa-xmark')]").click()
    time.sleep(0.3)

def test_strict_kiosk_offers_boundaries(driver, base_url):
    driver.get(f"{base_url}/kiosk/offers.html")
    time.sleep(0.3)

    body_text = driver.find_element(By.TAG_NAME, "body").text.lower()
    assert "campaign analytics" not in body_text
    assert "ad manager" not in body_text
    assert "cpc bidding" not in body_text
    assert "merchant portal" not in body_text
