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

def test_map_page_loads_and_header(driver, base_url):
    driver.get(f"{base_url}/kiosk/map.html")
    time.sleep(0.5)

    # 1. Title & Branding
    assert "Mall Map & Navigation" in driver.title
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
    assert "MALL MAP" in driver.page_source and "NAVIGATION" in driver.page_source

def test_floor_selector_and_legend_rendering(driver, base_url):
    driver.get(f"{base_url}/kiosk/map.html")
    time.sleep(0.5)

    # Floor Selector Cards
    floor_gf = driver.find_element(By.ID, "floorGF")
    assert floor_gf.is_displayed()
    assert "Ground Floor" in floor_gf.text

    floor_f1 = driver.find_element(By.ID, "floorF1")
    assert "First Floor" in floor_f1.text

    # Map Legend
    assert "Map Legend" in driver.page_source
    assert "Stores" in driver.page_source
    assert "Food" in driver.page_source and "Dining" in driver.page_source
    assert "Escalator" in driver.page_source
    assert "You Are Here" in driver.page_source

def test_interactive_map_canvas_and_controls(driver, base_url):
    driver.get(f"{base_url}/kiosk/map.html")
    time.sleep(0.5)

    # Floor plan image
    img = driver.find_element(By.ID, "floorPlanImg")
    assert img.is_displayed()

    # You Are Here beacon
    beacon = driver.find_element(By.ID, "youAreHerePin")
    assert beacon.is_displayed()

    # Floating zoom buttons
    btn_in = driver.find_element(By.ID, "btnZoomIn")
    btn_out = driver.find_element(By.ID, "btnZoomOut")
    btn_recenter = driver.find_element(By.ID, "btnRecenter")

    assert btn_in.is_displayed()
    assert btn_out.is_displayed()
    assert btn_recenter.is_displayed()

    # Click Zoom In & Recenter
    btn_in.click()
    time.sleep(0.2)
    btn_recenter.click()
    time.sleep(0.2)

def test_map_destination_selection_and_right_panel(driver, base_url):
    driver.get(f"{base_url}/kiosk/map.html")
    time.sleep(0.3)

    # Default selected destination: PVR Cinemas
    dest_name = driver.find_element(By.ID, "destName")
    assert "PVR Cinemas" in dest_name.text

    # Click ZARA Hotspot Pin
    driver.find_element(By.ID, "pinZARA").click()
    time.sleep(0.3)
    assert "ZARA" in dest_name.text
    assert "Ground Floor, G-01" in driver.find_element(By.ID, "destLoc").text

    # Click H&M Hotspot Pin
    driver.find_element(By.ID, "pinHM").click()
    time.sleep(0.3)
    assert "H&M" in dest_name.text

def test_quick_categories_interaction(driver, base_url):
    driver.get(f"{base_url}/kiosk/map.html")
    time.sleep(0.3)

    dest_name = driver.find_element(By.ID, "destName")

    # 1. Quick Category: Food & Dining
    driver.find_element(By.ID, "quickCatFood").click()
    time.sleep(0.3)
    assert "Food Court" in dest_name.text

    # 2. Quick Category: Services
    driver.find_element(By.ID, "quickCatServices").click()
    time.sleep(0.3)
    assert "Concierge" in dest_name.text

    # 3. Quick Category: Events
    driver.find_element(By.ID, "quickCatEvents").click()
    time.sleep(0.3)
    assert "Atrium" in dest_name.text

def test_recent_searches_and_clear(driver, base_url):
    driver.get(f"{base_url}/kiosk/map.html")
    time.sleep(0.3)

    dest_name = driver.find_element(By.ID, "destName")

    # Click Starbucks recent search
    driver.find_element(By.XPATH, "//div[@id='recentSearchesList']//span[contains(text(),'Starbucks')]").click()
    time.sleep(0.3)
    assert "Starbucks" in dest_name.text

    # Clear Recent Searches
    driver.find_element(By.ID, "btnClearRecentSearches").click()
    time.sleep(0.3)
    assert "No recent searches" in driver.find_element(By.ID, "recentSearchesList").text

def test_get_directions_and_route_modal(driver, base_url):
    driver.get(f"{base_url}/kiosk/map.html")
    time.sleep(0.3)

    # Click Get Directions
    driver.find_element(By.ID, "btnGetDirections").click()
    time.sleep(0.3)

    modal = driver.find_element(By.ID, "activeRouteModal")
    assert modal.is_displayed()
    assert "Route to PVR Cinemas" in modal.text
    assert "Step 1:" in modal.text
    assert "Step 2:" in modal.text

    # Verify Send to Mobile button
    btn_mobile = driver.find_element(By.ID, "btnSendRouteMobile")
    assert btn_mobile.is_displayed()

    driver.find_element(By.XPATH, "//div[@id='activeRouteModal']//i[contains(@class,'fa-xmark')]").click()
    time.sleep(0.3)
    assert not modal.is_displayed()

def test_cross_domain_url_handoff(driver, base_url):
    # Test handoff with ?dest=zara
    driver.get(f"{base_url}/kiosk/map.html?dest=zara")
    time.sleep(0.5)

    dest_name = driver.find_element(By.ID, "destName")
    assert "ZARA" in dest_name.text
    assert "G-01" in driver.find_element(By.ID, "destLoc").text

    # Test handoff with ?dest=starbucks
    driver.get(f"{base_url}/kiosk/map.html?dest=starbucks")
    time.sleep(0.5)
    assert "Starbucks" in driver.find_element(By.ID, "destName").text

def test_strict_kiosk_map_boundaries(driver, base_url):
    driver.get(f"{base_url}/kiosk/map.html")
    time.sleep(0.3)

    body_text = driver.find_element(By.TAG_NAME, "body").text.lower()
    assert "gis sensor telemetry" not in body_text
    assert "map layer editor" not in body_text
    assert "cad drawing upload" not in body_text
    assert "beacon battery analytics" not in body_text
