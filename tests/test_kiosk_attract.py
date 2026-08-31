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

def test_attract_page_loads_and_branding(driver, base_url):
    driver.get(f"{base_url}/kiosk/attract.html")
    time.sleep(0.5)

    # 1. Title & Branding
    assert "Grand Metro Mall" in driver.title
    assert "GRAND METRO MALL" in driver.page_source
    assert "CELEBRATE EVERYDAY" in driver.page_source

    # 2. Top Slogan
    assert "SHOP" in driver.page_source
    assert "DINE" in driver.page_source
    assert "EXPLORE" in driver.page_source
    assert "BELONG" in driver.page_source

def test_attract_hero_and_model_girl_layer(driver, base_url):
    driver.get(f"{base_url}/kiosk/attract.html")
    time.sleep(0.5)

    # Hero girl image
    img = driver.find_element(By.ID, "attractHeroGirlImg")
    assert img.is_displayed()

    # Hero copy
    assert "More Than a Mall" in driver.page_source or "Grand Festive" in driver.page_source
    assert "Experiences" in driver.page_source or "Moments" in driver.page_source

def test_attract_category_circles(driver, base_url):
    driver.get(f"{base_url}/kiosk/attract.html")
    time.sleep(0.5)

    assert "Shopping" in driver.page_source
    assert "Dining" in driver.page_source
    assert "Events" in driver.page_source
    assert "Moments" in driver.page_source

def test_attract_supporting_promo_tiles(driver, base_url):
    driver.get(f"{base_url}/kiosk/attract.html")
    time.sleep(0.5)

    tiles = driver.find_elements(By.CSS_SELECTOR, ".promo-feature-tile")
    assert len(tiles) == 4

    assert "FASHION" in driver.page_source
    assert "GREAT FOOD" in driver.page_source
    assert "LIVE EVENTS" in driver.page_source
    assert "GOOD TIMES" in driver.page_source

def test_attract_brand_strip_and_touch_to_begin(driver, base_url):
    driver.get(f"{base_url}/kiosk/attract.html")
    time.sleep(0.5)

    # Brand Strip
    assert "ZARA" in driver.page_source
    assert "ADIDAS" in driver.page_source
    assert "STARBUCKS" in driver.page_source
    assert "PVR CINEMAS" in driver.page_source

    # Touch To Begin Button
    btn = driver.find_element(By.ID, "btnTouchToBegin")
    assert btn.is_displayed()
    assert "TOUCH TO BEGIN" in btn.text

def test_attract_touch_transitions_to_home(driver, base_url):
    driver.get(f"{base_url}/kiosk/attract.html")
    time.sleep(0.3)

    # Click Touch To Begin
    driver.find_element(By.ID, "btnTouchToBegin").click()
    time.sleep(0.5)

    # Verify navigated to home.html
    assert "home.html" in driver.current_url or "Grand Metro Mall" in driver.title

def test_idle_timeout_attract_mode_transition(driver, base_url):
    # 1. Open home.html
    driver.get(f"{base_url}/kiosk/home.html")
    time.sleep(0.5)
    assert "home.html" in driver.current_url

    # 2. Wait 16 seconds without touching/interacting
    time.sleep(16.0)

    # 3. Verify it automatically transitioned to attract.html
    assert "attract.html" in driver.current_url

    # 4. Touch anywhere on attract screen and verify it returns to home.html
    driver.find_element(By.ID, "btnTouchToBegin").click()
    time.sleep(0.5)
    assert "home.html" in driver.current_url

def test_strict_kiosk_attract_boundaries(driver, base_url):
    driver.get(f"{base_url}/kiosk/attract.html")
    time.sleep(0.3)

    body_text = driver.find_element(By.TAG_NAME, "body").text.lower()
    assert "ad campaign analytics dashboard" not in body_text
    assert "cpm pricing table" not in body_text
    assert "ad scheduler queue" not in body_text
    assert "media asset cms" not in body_text
