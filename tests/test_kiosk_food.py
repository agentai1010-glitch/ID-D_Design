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

def test_food_page_loads_and_header(driver, base_url):
    driver.get(f"{base_url}/kiosk/food.html")
    time.sleep(0.5)

    # 1. Title & Branding
    assert "Food & Dining" in driver.title
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
    assert "FOOD & DINING" in driver.page_source

def test_food_category_bar_rendering(driver, base_url):
    driver.get(f"{base_url}/kiosk/food.html")
    time.sleep(0.5)

    # Verify all 6 category buttons
    cat_cafes = driver.find_element(By.ID, "catCafes")
    assert cat_cafes.is_displayed()
    assert "Cafes" in cat_cafes.text
    assert "32" in cat_cafes.text

    cat_rest = driver.find_element(By.ID, "catRestaurants")
    assert "Restaurants" in cat_rest.text
    assert "58" in cat_rest.text

    cat_fc = driver.find_element(By.ID, "catFoodCourt")
    assert "Food Court" in cat_fc.text
    assert "24" in cat_fc.text

    cat_desserts = driver.find_element(By.ID, "catDesserts")
    assert "Desserts" in cat_desserts.text

    cat_bev = driver.find_element(By.ID, "catBeverages")
    assert "Beverages" in cat_bev.text

    cat_all = driver.find_element(By.ID, "catAll")
    assert "All" in cat_all.text

def test_dining_grid_and_featured_cards_rendering(driver, base_url):
    driver.get(f"{base_url}/kiosk/food.html")
    time.sleep(0.5)

    # Switch to All to see all cards
    driver.find_element(By.ID, "catAll").click()
    time.sleep(0.3)

    # Top Row Outlets
    starbucks = driver.find_element(By.CSS_SELECTOR, ".dining-outlet-card[data-id='starbucks']")
    assert starbucks.is_displayed()
    assert "Starbucks" in starbucks.text
    assert "Ground Floor, G-15" in starbucks.text

    bbqnation = driver.find_element(By.CSS_SELECTOR, ".dining-outlet-card[data-id='bbqnation']")
    assert bbqnation.is_displayed()
    assert "Barbeque Nation" in bbqnation.text

    # Bottom Row Compact Cards
    ovenstory = driver.find_element(By.CSS_SELECTOR, ".dining-compact-card[data-id='ovenstory']")
    assert ovenstory.is_displayed()
    assert "Oven Story" in ovenstory.text

    # Featured Restaurant Card
    assert "Copper Chimney" in driver.page_source
    assert "First Floor, F-08" in driver.page_source

    # Meal Combos Banner
    assert "MEAL COMBOS" in driver.page_source
    assert "199" in driver.page_source

def test_dining_category_filtering(driver, base_url):
    driver.get(f"{base_url}/kiosk/food.html")
    time.sleep(0.3)

    starbucks = driver.find_element(By.CSS_SELECTOR, ".dining-outlet-card[data-id='starbucks']")
    bbqnation = driver.find_element(By.CSS_SELECTOR, ".dining-outlet-card[data-id='bbqnation']")
    baskin = driver.find_element(By.CSS_SELECTOR, ".dining-compact-card[data-id='baskinrobbins']")

    # 1. Click Restaurants
    driver.find_element(By.ID, "catRestaurants").click()
    time.sleep(0.3)
    assert bbqnation.is_displayed()
    assert not starbucks.is_displayed()

    # 2. Click Desserts
    driver.find_element(By.ID, "catDesserts").click()
    time.sleep(0.3)
    assert baskin.is_displayed()
    assert not bbqnation.is_displayed()

    # 3. Click All
    driver.find_element(By.ID, "catAll").click()
    time.sleep(0.3)
    assert starbucks.is_displayed()
    assert bbqnation.is_displayed()
    assert baskin.is_displayed()

def test_dining_search_simulation(driver, base_url):
    driver.get(f"{base_url}/kiosk/food.html")
    time.sleep(0.3)

    driver.find_element(By.ID, "catAll").click()
    time.sleep(0.2)

    search_inp = driver.find_element(By.ID, "diningSearchInput")
    search_inp.send_keys("Starbucks")
    time.sleep(0.3)

    starbucks = driver.find_element(By.CSS_SELECTOR, ".dining-outlet-card[data-id='starbucks']")
    bbqnation = driver.find_element(By.CSS_SELECTOR, ".dining-outlet-card[data-id='bbqnation']")

    assert starbucks.is_displayed()
    assert not bbqnation.is_displayed()

    # Empty search query
    search_inp.clear()
    search_inp.send_keys("unmatchedfood123")
    time.sleep(0.3)

    empty_notice = driver.find_element(By.ID, "emptyDiningNotice")
    assert empty_notice.is_displayed()
    assert "No Dining Outlets Found" in empty_notice.text

    # Reset
    driver.find_element(By.XPATH, "//div[@id='emptyDiningNotice']//button[text()='Reset Filters']").click()
    time.sleep(0.3)
    assert not empty_notice.is_displayed()

def test_dining_details_modal_and_take_me_there(driver, base_url):
    driver.get(f"{base_url}/kiosk/food.html")
    time.sleep(0.3)

    driver.find_element(By.ID, "catAll").click()
    time.sleep(0.2)

    # Click Starbucks card View Details
    driver.find_element(By.CSS_SELECTOR, ".dining-outlet-card[data-id='starbucks']").click()
    time.sleep(0.3)

    modal = driver.find_element(By.ID, "diningDetailsModal")
    assert modal.is_displayed()
    assert "Starbucks" in modal.text
    assert "Ground Floor, G-15" in modal.text

    take_me_btn = driver.find_element(By.ID, "btnDiningModalNav")
    assert take_me_btn.is_displayed()
    assert "Take Me There" in take_me_btn.text

    driver.find_element(By.XPATH, "//div[@id='diningDetailsModal']//button[text()='Close']").click()
    time.sleep(0.3)
    assert not modal.is_displayed()

def test_featured_restaurant_menu_offers_and_photos_modals(driver, base_url):
    driver.get(f"{base_url}/kiosk/food.html")
    time.sleep(0.3)

    # 1. Open Digital Menu Modal
    driver.find_element(By.ID, "tileDiningMenu").click()
    time.sleep(0.3)

    menu_modal = driver.find_element(By.ID, "diningMenuModal")
    assert menu_modal.is_displayed()
    assert "Digital Menu" in menu_modal.text
    assert "Tandoori Paneer Tikka" in menu_modal.text
    assert "₹385" in menu_modal.text

    driver.find_element(By.XPATH, "//div[@id='diningMenuModal']//button[text()='Close']").click()
    time.sleep(0.3)
    assert not menu_modal.is_displayed()

    # 2. Open Offers Modal
    driver.find_element(By.ID, "tileDiningOffers").click()
    time.sleep(0.3)
    offers_modal = driver.find_element(By.ID, "diningOffersModal")
    assert offers_modal.is_displayed()
    assert "Flat 20% Off" in offers_modal.text

    driver.find_element(By.XPATH, "//div[@id='diningOffersModal']//button[text()='Close']").click()
    time.sleep(0.3)
    assert not offers_modal.is_displayed()

    # 3. Open Photos Modal
    driver.find_element(By.ID, "tileDiningPhotos").click()
    time.sleep(0.3)
    photos_modal = driver.find_element(By.ID, "diningPhotosModal")
    assert photos_modal.is_displayed()

    driver.find_element(By.XPATH, "//div[@id='diningPhotosModal']//button[text()='Close']").click()
    time.sleep(0.3)
    assert not photos_modal.is_displayed()

def test_strict_kiosk_food_boundaries(driver, base_url):
    driver.get(f"{base_url}/kiosk/food.html")
    time.sleep(0.3)

    body_text = driver.find_element(By.TAG_NAME, "body").text.lower()
    assert "analytics report" not in body_text
    assert "restaurant pos integration" not in body_text
    assert "revenue breakdown" not in body_text
    assert "kitchen management" not in body_text
