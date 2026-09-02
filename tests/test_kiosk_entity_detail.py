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

def test_detail_page_loads_and_branding(driver, base_url):
    driver.get(f"{base_url}/kiosk/detail.html?id=nike&from=shop")
    time.sleep(0.5)

    assert "Entity Detail" in driver.title or "Grand Metro Mall" in driver.title
    assert "GRAND METRO MALL" in driver.page_source
    assert "CELEBRATE EVERYDAY" in driver.page_source
    assert "28°C" in driver.page_source

def test_detail_default_entity_nike(driver, base_url):
    driver.get(f"{base_url}/kiosk/detail.html?id=nike&from=shop")
    time.sleep(0.5)

    name = driver.find_element(By.ID, "detailEntityName").text
    cat = driver.find_element(By.ID, "detailEntityCat").text
    floor = driver.find_element(By.ID, "detailEntityFloor").text
    hours = driver.find_element(By.ID, "detailEntityHours").text
    phone = driver.find_element(By.ID, "detailEntityPhone").text

    assert name == "Nike"
    assert "SPORTSWEAR" in cat.upper()
    assert "GF-12" in floor
    assert "10:00 AM - 10:00 PM" in hours
    assert "0124-4567890" in phone

def test_detail_hero_carousel_controls(driver, base_url):
    driver.get(f"{base_url}/kiosk/detail.html?id=nike&from=shop")
    time.sleep(0.5)

    img = driver.find_element(By.ID, "detailHeroImg")
    initial_src = img.get_attribute("src")

    # Click next arrow
    next_btn = driver.find_element(By.CSS_SELECTOR, ".detail-hero-nav-arrow.next")
    next_btn.click()
    time.sleep(0.4)

    # Verify dots exist
    dots = driver.find_elements(By.CSS_SELECTOR, ".detail-hero-dot")
    assert len(dots) >= 2

def test_detail_take_me_there_navigation(driver, base_url):
    driver.get(f"{base_url}/kiosk/detail.html?id=nike&from=shop")
    time.sleep(0.3)

    take_btn = driver.find_element(By.ID, "btnTakeMeThere")
    assert take_btn.is_displayed()
    take_btn.click()
    time.sleep(0.5)

    assert "map.html" in driver.current_url
    assert "GF-12" in driver.current_url or "Nike" in driver.current_url

def test_detail_add_to_favourites_toggle(driver, base_url):
    driver.get(f"{base_url}/kiosk/detail.html?id=nike&from=shop")
    time.sleep(0.3)

    fav_btn = driver.find_element(By.ID, "btnAddFavourites")
    assert "ADD TO FAVOURITES" in fav_btn.text

    fav_btn.click()
    time.sleep(0.2)
    assert "ADDED TO FAVOURITES" in fav_btn.text
    assert "active" in fav_btn.get_attribute("class")

    # Toggle off
    fav_btn.click()
    time.sleep(0.2)
    assert "ADD TO FAVOURITES" in fav_btn.text

def test_detail_visitor_feedback_and_review_modal(driver, base_url):
    driver.get(f"{base_url}/kiosk/detail.html?id=nike&from=shop")
    time.sleep(0.3)

    score = driver.find_element(By.ID, "feedbackScore").text
    assert "4.6" in score

    # Open Rate & Review Modal
    driver.find_element(By.CSS_SELECTOR, ".btn-rate-review").click()
    time.sleep(0.4)

    modal = driver.find_element(By.ID, "rateReviewModal")
    assert "open" in modal.get_attribute("class")

    # Select star & submit
    stars = driver.find_elements(By.CSS_SELECTOR, ".modal-star-btn")
    if len(stars) >= 5:
        stars[4].click()

    driver.find_element(By.ID, "btnSubmitReview").click()
    time.sleep(0.5)

    success_state = driver.find_element(By.ID, "reviewSuccessState")
    assert success_state.is_displayed()

def test_detail_todays_deals_widget(driver, base_url):
    driver.get(f"{base_url}/kiosk/detail.html?id=nike&from=shop")
    time.sleep(0.3)

    deals = driver.find_elements(By.CSS_SELECTOR, ".deal-mini-card")
    assert len(deals) >= 1
    assert "40% OFF" in driver.page_source or "OFF" in driver.page_source

def test_detail_similar_brands_dynamic_switch(driver, base_url):
    driver.get(f"{base_url}/kiosk/detail.html?id=nike&from=shop")
    time.sleep(0.3)

    # Find Adidas in Similar Brands list
    similar_items = driver.find_elements(By.CSS_SELECTOR, ".similar-brand-row")
    assert len(similar_items) >= 2

    # Click first similar brand (Adidas)
    similar_items[0].click()
    time.sleep(0.4)

    # Verify detail updated to Adidas dynamically
    new_name = driver.find_element(By.ID, "detailEntityName").text
    assert new_name == "Adidas"
    assert "GF-14" in driver.page_source

def test_detail_back_button_context_routing(driver, base_url):
    # 1. From Shop
    driver.get(f"{base_url}/kiosk/detail.html?id=nike&from=shop")
    time.sleep(0.3)
    driver.find_element(By.ID, "btnDetailBack").click()
    time.sleep(0.5)
    assert "shop.html" in driver.current_url

    # 2. From Food
    driver.get(f"{base_url}/kiosk/detail.html?id=copper-chimney&from=food")
    time.sleep(0.3)
    driver.find_element(By.ID, "btnDetailBack").click()
    time.sleep(0.5)
    assert "food.html" in driver.current_url

def test_cross_workflow_entry_points(driver, base_url):
    # Test food entry point directly
    driver.get(f"{base_url}/kiosk/detail.html?id=copper-chimney&from=food")
    time.sleep(0.4)

    assert "Copper Chimney" in driver.find_element(By.ID, "detailEntityName").text
    assert "FF-04" in driver.page_source

    # Test services entry point directly
    driver.get(f"{base_url}/kiosk/detail.html?id=atm&from=services")
    time.sleep(0.4)

    assert "ATM" in driver.find_element(By.ID, "detailEntityName").text
    assert "GF-ATM" in driver.page_source

def test_strict_kiosk_boundaries(driver, base_url):
    driver.get(f"{base_url}/kiosk/detail.html?id=nike&from=shop")
    time.sleep(0.3)

    body_text = driver.find_element(By.TAG_NAME, "body").text.lower()
    assert "crm analytics" not in body_text
    assert "tenant billing portal" not in body_text
    assert "admin moderation queue" not in body_text
    assert "database cms" not in body_text
