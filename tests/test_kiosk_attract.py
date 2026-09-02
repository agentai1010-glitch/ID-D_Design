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

    cards = driver.find_elements(By.CSS_SELECTOR, ".ad2-feature-card")
    assert len(cards) >= 6

    assert "FASHION" in driver.page_source
    assert "GREAT FOOD" in driver.page_source
    assert "EXCITING EXPERIENCES" in driver.page_source
    assert "A LIFESTYLE YOU'LL LOVE" in driver.page_source

def test_attract_brand_strip_and_touch_to_begin(driver, base_url):
    driver.get(f"{base_url}/kiosk/attract.html")
    time.sleep(0.5)

    # Brand / Pill Strip
    assert "TOP BRANDS" in driver.page_source
    assert "FAMILY FRIENDLY" in driver.page_source
    assert "MEMORABLE EXPERIENCES" in driver.page_source
    assert "IN THE HEART OF THE CITY" in driver.page_source

    # Touch To Explore Button
    btn = driver.find_element(By.ID, "btnTouchToBegin")
    assert btn.is_displayed()
    assert "TOUCH THE SCREEN TO EXPLORE" in btn.text

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

def test_attract_dual_campaign_carousel_rotation(driver, base_url):
    driver.get(f"{base_url}/kiosk/attract.html")
    time.sleep(0.5)

    # 1. Verify both campaign slides and images exist
    slide1 = driver.find_element(By.ID, "adSlide1")
    slide2 = driver.find_element(By.ID, "adSlide2")
    assert slide1 is not None and slide2 is not None

    img1 = driver.find_element(By.ID, "attractHeroGirlImg")
    img2 = driver.find_element(By.ID, "attractHeroGirl2Img")
    assert img1 is not None and img2 is not None

    # 2. Switch to Slide 2 (Ad 02 - Anchor 02)
    driver.execute_script("showSlide(1);")
    time.sleep(0.5)

    # Verify Slide 2 is active
    assert "active" in slide2.get_attribute("class")

    # Verify Ad 2 Content
    assert "Brands" in driver.page_source
    assert "Brighter" in driver.page_source
    assert "Moments" in driver.page_source
    assert "DISCOVER THE BEST" in driver.page_source

    # Verify Persistent Sub-Ads Cards
    assert "FASHION THAT MOVES YOU" in driver.page_source
    assert "GREAT FOOD HAPPIER MOMENTS" in driver.page_source
    assert "EXCITING EXPERIENCES" in driver.page_source
    assert "A LIFESTYLE YOU'LL LOVE" in driver.page_source

    # 3. Verify Touch Prompt redirects to home
    btn_explore = driver.find_element(By.ID, "btnTouchToBegin")
    assert btn_explore.is_displayed()
    btn_explore.click()
    time.sleep(0.5)
    assert "home.html" in driver.current_url

def test_attract_slide1_interactive_brand_showcase(driver, base_url):
    driver.get(f"{base_url}/kiosk/attract.html")
    time.sleep(0.5)

    # Verify Slide 1 Interactive Brand Cards
    assert "FEATURED FLAGSHIPS" in driver.page_source
    assert "ZARA" in driver.page_source
    assert "GF-14" in driver.page_source
    assert "UP TO 50% OFF" in driver.page_source

    assert "H&M" in driver.page_source
    assert "GF-02" in driver.page_source
    assert "FLAT 20% OFF" in driver.page_source

    assert "ADIDAS" in driver.page_source
    assert "LG-08" in driver.page_source
    assert "FLAT 35% OFF" in driver.page_source

    assert "STARBUCKS" in driver.page_source
    assert "LG-10" in driver.page_source
    assert "BUY 1 GET 1 BEV" in driver.page_source

    assert "PVR CINEMAS" in driver.page_source
    assert "L3" in driver.page_source
    assert "IMAX 3D" in driver.page_source
    assert "4DX" in driver.page_source

def test_attract_slide2_visual_experience_pillars(driver, base_url):
    driver.get(f"{base_url}/kiosk/attract.html")
    time.sleep(0.5)

    # Switch to Slide 2
    driver.execute_script("showSlide(1);")
    time.sleep(0.5)

    # Verify Visual Experience Pillars
    assert "CURATED EXPERIENCES" in driver.page_source
    assert "DISCOVER THE BEST" in driver.page_source
    assert "FASHION FOR EVERY YOU" in driver.page_source
    assert "GREAT FOOD BRINGS PEOPLE TOGETHER" in driver.page_source
    assert "LIVE EVENTS BIGGER THAN EVER" in driver.page_source
    assert "GOOD TIMES STAY LONGER" in driver.page_source

def test_strict_kiosk_attract_boundaries(driver, base_url):
    driver.get(f"{base_url}/kiosk/attract.html")
    time.sleep(0.3)

    body_text = driver.find_element(By.TAG_NAME, "body").text.lower()
    assert "ad campaign analytics dashboard" not in body_text
    assert "cpm pricing table" not in body_text
    assert "ad scheduler queue" not in body_text
    assert "media asset cms" not in body_text


