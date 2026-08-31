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

def test_shop_page_loads_and_header_elements(driver, base_url):
    driver.get(f"{base_url}/kiosk/shop.html")
    time.sleep(0.5)

    # 1. Page Title & Mall Logo
    assert "Shopping & Stores" in driver.title
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

    # 4. Title Header
    assert "STORES" in driver.page_source and "BRANDS" in driver.page_source

def test_shop_3col_layout_rendering(driver, base_url):
    driver.get(f"{base_url}/kiosk/shop.html")
    time.sleep(0.5)

    # 1. Left Sidebar: Categories
    sidebar = driver.find_element(By.ID, "categoriesSidebar")
    assert sidebar.is_displayed()
    assert "All Stores" in sidebar.text
    assert "Fashion" in sidebar.text
    assert "Footwear" in sidebar.text
    assert "Beauty & Health" in sidebar.text

    # 2. Center Column: Floor Bar & Store Cards
    floor_all = driver.find_element(By.ID, "floorAll")
    assert floor_all.is_displayed()

    grid = driver.find_element(By.ID, "storesGridContainer")
    assert grid.is_displayed()
    cards = grid.find_elements(By.CSS_SELECTOR, ".store-grid-card")
    assert len(cards) == 8

    # 3. Right Preview Panel
    panel = driver.find_element(By.ID, "storePreviewPanel")
    assert panel.is_displayed()
    assert "ZARA" in panel.text
    assert "Ground Floor, G-01" in panel.text

def test_store_selection_updates_preview_panel(driver, base_url):
    driver.get(f"{base_url}/kiosk/shop.html")
    time.sleep(0.3)

    # Click H&M Card
    hm_card = driver.find_element(By.CSS_SELECTOR, ".store-grid-card[data-id='hm']")
    hm_card.click()
    time.sleep(0.3)

    panel = driver.find_element(By.ID, "storePreviewPanel")
    assert "H&M" in panel.text
    assert "Ground Floor, G-12" in panel.text

    # Click SEPHORA Card
    sephora_card = driver.find_element(By.CSS_SELECTOR, ".store-grid-card[data-id='sephora']")
    sephora_card.click()
    time.sleep(0.3)

    assert "SEPHORA" in panel.text
    assert "Ground Floor, G-22" in panel.text

def test_category_navigation_filtering(driver, base_url):
    driver.get(f"{base_url}/kiosk/shop.html")
    time.sleep(0.3)

    # 1. Click Footwear Category
    driver.find_element(By.ID, "catItemFootwear").click()
    time.sleep(0.3)

    skechers_card = driver.find_element(By.CSS_SELECTOR, ".store-grid-card[data-id='skechers']")
    zara_card = driver.find_element(By.CSS_SELECTOR, ".store-grid-card[data-id='zara']")

    assert skechers_card.is_displayed()
    assert not zara_card.is_displayed()

    # 2. Click Beauty & Health Category
    driver.find_element(By.ID, "catItemBeauty").click()
    time.sleep(0.3)

    sephora_card = driver.find_element(By.CSS_SELECTOR, ".store-grid-card[data-id='sephora']")
    assert sephora_card.is_displayed()
    assert not skechers_card.is_displayed()

    # 3. Clear Filters
    driver.find_element(By.ID, "btnClearAllFilters").click()
    time.sleep(0.3)
    assert zara_card.is_displayed()
    assert skechers_card.is_displayed()

def test_floor_filtering(driver, base_url):
    driver.get(f"{base_url}/kiosk/shop.html")
    time.sleep(0.3)

    # 1. Click First Floor
    driver.find_element(By.ID, "floorFirst").click()
    time.sleep(0.3)

    trends_card = driver.find_element(By.CSS_SELECTOR, ".store-grid-card[data-id='trends']")
    zara_card = driver.find_element(By.CSS_SELECTOR, ".store-grid-card[data-id='zara']")

    assert trends_card.is_displayed()
    assert not zara_card.is_displayed()

    # 2. Click Second Floor
    driver.find_element(By.ID, "floorSecond").click()
    time.sleep(0.3)

    pvr_card = driver.find_element(By.CSS_SELECTOR, ".store-grid-card[data-id='pvr']")
    assert pvr_card.is_displayed()
    assert not trends_card.is_displayed()

    # 3. Reset All Floors
    driver.find_element(By.ID, "floorAll").click()
    time.sleep(0.3)
    assert zara_card.is_displayed()
    assert trends_card.is_displayed()

def test_store_search_simulation(driver, base_url):
    driver.get(f"{base_url}/kiosk/shop.html")
    time.sleep(0.3)

    search_inp = driver.find_element(By.ID, "shopStoreSearchInput")
    search_inp.send_keys("Zara")
    time.sleep(0.3)

    zara_card = driver.find_element(By.CSS_SELECTOR, ".store-grid-card[data-id='zara']")
    hm_card = driver.find_element(By.CSS_SELECTOR, ".store-grid-card[data-id='hm']")

    assert zara_card.is_displayed()
    assert not hm_card.is_displayed()

    # Test empty query notice
    search_inp.clear()
    search_inp.send_keys("nonexistent123")
    time.sleep(0.3)

    empty_notice = driver.find_element(By.ID, "emptyStoresNotice")
    assert empty_notice.is_displayed()
    assert "No Stores Found" in empty_notice.text

    # Clear filters
    driver.find_element(By.ID, "btnClearAllFilters").click()
    time.sleep(0.3)
    assert not empty_notice.is_displayed()
    assert zara_card.is_displayed()

def test_store_modals_and_take_me_there_handoff(driver, base_url):
    driver.get(f"{base_url}/kiosk/shop.html")
    time.sleep(0.3)

    # 1. Full Store Details Modal
    driver.find_element(By.ID, "btnViewStoreDetailsFull").click()
    time.sleep(0.3)

    detail_modal = driver.find_element(By.ID, "fullStoreDetailsModal")
    assert detail_modal.is_displayed()
    assert "ZARA" in detail_modal.text
    assert "Ground Floor, G-01" in detail_modal.text
    assert "SIMILAR STORES NEARBY" in detail_modal.text.upper()

    take_me_btn = driver.find_element(By.ID, "btnModalTakeMeThere")
    assert take_me_btn.is_displayed()
    assert "Take Me There" in take_me_btn.text

    driver.find_element(By.XPATH, "//div[@id='fullStoreDetailsModal']//button[text()='Close']").click()
    time.sleep(0.3)
    assert not detail_modal.is_displayed()

    # 2. Offers Modal
    driver.find_element(By.ID, "tileStoreOffers").click()
    time.sleep(0.3)
    offers_modal = driver.find_element(By.ID, "storeOffersModal")
    assert offers_modal.is_displayed()
    assert "Active Offers" in offers_modal.text
    driver.find_element(By.XPATH, "//div[@id='storeOffersModal']//button[text()='Close']").click()
    time.sleep(0.3)
    assert not offers_modal.is_displayed()

    # 3. Photos Modal
    driver.find_element(By.ID, "tileStorePhotos").click()
    time.sleep(0.3)
    photos_modal = driver.find_element(By.ID, "storePhotosModal")
    assert photos_modal.is_displayed()
    assert "Photo Gallery" in photos_modal.text
    driver.find_element(By.XPATH, "//div[@id='storePhotosModal']//button[text()='Close']").click()
    time.sleep(0.3)
    assert not photos_modal.is_displayed()

def test_strict_kiosk_shop_boundaries(driver, base_url):
    driver.get(f"{base_url}/kiosk/shop.html")
    time.sleep(0.3)

    body_text = driver.find_element(By.TAG_NAME, "body").text.lower()
    assert "admin panel" not in body_text
    assert "store manager login" not in body_text
    assert "conversion analytics" not in body_text
    assert "revenue chart" not in body_text
