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

def test_events_page_loads_and_header(driver, base_url):
    driver.get(f"{base_url}/kiosk/events.html")
    time.sleep(0.5)

    # 1. Title & Branding
    assert "Events & Entertainment" in driver.title
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
    assert "EVENTS" in driver.page_source

def test_events_category_bar_rendering(driver, base_url):
    driver.get(f"{base_url}/kiosk/events.html")
    time.sleep(0.5)

    cat_all = driver.find_element(By.ID, "catAllEvents")
    assert cat_all.is_displayed()
    assert "All Events" in cat_all.text
    assert "64" in cat_all.text

    cat_live = driver.find_element(By.ID, "catLiveShows")
    assert "Live Shows" in cat_live.text
    assert "12" in cat_live.text

    cat_music = driver.find_element(By.ID, "catMusicConcerts")
    assert "Music & Concerts" in cat_music.text

    cat_kids = driver.find_element(By.ID, "catKidsFamily")
    assert "Kids & Family" in cat_kids.text

    cat_fest = driver.find_element(By.ID, "catFestivals")
    assert "Festivals" in cat_fest.text

def test_events_grid_and_featured_cards_rendering(driver, base_url):
    driver.get(f"{base_url}/kiosk/events.html")
    time.sleep(0.5)

    grid = driver.find_element(By.ID, "eventsGridContainer")
    assert grid.is_displayed()
    cards = grid.find_elements(By.CSS_SELECTOR, ".event-featured-card")
    assert len(cards) == 4

    # Top row cards
    armaan = driver.find_element(By.CSS_SELECTOR, ".event-featured-card[data-id='armaan']")
    assert "Armaan Malik Live" in armaan.text
    assert "12 Sep 2026" in armaan.text

    comedy = driver.find_element(By.CSS_SELECTOR, ".event-featured-card[data-id='comedy']")
    assert "Comedy Night" in comedy.text

    # Today's Highlights
    assert "Today's Highlights" in driver.page_source
    assert "Live Acoustic Session" in driver.page_source
    assert "Magic Show for Kids" in driver.page_source

    # Right column Featured Event & Upcoming
    assert "Featured Event" in driver.page_source
    assert "12" in driver.page_source
    assert "SEP" in driver.page_source
    assert "Upcoming Events" in driver.page_source
    assert "Food Festival" in driver.page_source

def test_events_category_filtering(driver, base_url):
    driver.get(f"{base_url}/kiosk/events.html")
    time.sleep(0.3)

    armaan = driver.find_element(By.CSS_SELECTOR, ".event-featured-card[data-id='armaan']")
    comedy = driver.find_element(By.CSS_SELECTOR, ".event-featured-card[data-id='comedy']")
    kidsart = driver.find_element(By.CSS_SELECTOR, ".event-featured-card[data-id='kidsart']")

    # 1. Click Music & Concerts
    driver.find_element(By.ID, "catMusicConcerts").click()
    time.sleep(0.3)
    assert armaan.is_displayed()
    assert not comedy.is_displayed()
    assert not kidsart.is_displayed()

    # 2. Click Live Shows
    driver.find_element(By.ID, "catLiveShows").click()
    time.sleep(0.3)
    assert comedy.is_displayed()
    assert not armaan.is_displayed()

    # 3. Click Kids & Family
    driver.find_element(By.ID, "catKidsFamily").click()
    time.sleep(0.3)
    assert kidsart.is_displayed()
    assert not comedy.is_displayed()

    # 4. Click All Events
    driver.find_element(By.ID, "catAllEvents").click()
    time.sleep(0.3)
    assert armaan.is_displayed()
    assert comedy.is_displayed()
    assert kidsart.is_displayed()

def test_events_search_simulation(driver, base_url):
    driver.get(f"{base_url}/kiosk/events.html")
    time.sleep(0.3)

    search_inp = driver.find_element(By.ID, "eventsSearchInput")
    search_inp.send_keys("Armaan")
    time.sleep(0.3)

    armaan = driver.find_element(By.CSS_SELECTOR, ".event-featured-card[data-id='armaan']")
    comedy = driver.find_element(By.CSS_SELECTOR, ".event-featured-card[data-id='comedy']")

    assert armaan.is_displayed()
    assert not comedy.is_displayed()

    # Empty search query
    search_inp.clear()
    search_inp.send_keys("nonexistentevent123")
    time.sleep(0.3)

    empty_notice = driver.find_element(By.ID, "emptyEventsNotice")
    assert empty_notice.is_displayed()
    assert "No Events Found" in empty_notice.text

    # Reset
    driver.find_element(By.XPATH, "//div[@id='emptyEventsNotice']//button[text()='Reset Filters']").click()
    time.sleep(0.3)
    assert not empty_notice.is_displayed()
    assert armaan.is_displayed()

def test_event_details_modal_and_take_me_there(driver, base_url):
    driver.get(f"{base_url}/kiosk/events.html")
    time.sleep(0.3)

    # Click Armaan Malik View Details
    driver.find_element(By.CSS_SELECTOR, ".event-featured-card[data-id='armaan']").click()
    time.sleep(0.3)

    modal = driver.find_element(By.ID, "eventDetailsModal")
    assert modal.is_displayed()
    assert "Armaan Malik" in modal.text
    assert "12 Sep 2026" in modal.text
    assert "Main Atrium" in modal.text

    # Verify Take Me There action
    btn_nav = driver.find_element(By.ID, "btnEventTakeMeThere")
    assert btn_nav.is_displayed()
    assert "Take Me There" in btn_nav.text

    driver.find_element(By.XPATH, "//div[@id='eventDetailsModal']//i[contains(@class,'fa-xmark')]").click()
    time.sleep(0.3)
    assert not modal.is_displayed()

def test_todays_highlights_and_upcoming_interactions(driver, base_url):
    driver.get(f"{base_url}/kiosk/events.html")
    time.sleep(0.3)

    # 1. Click Today's Highlight (Magic Show for Kids)
    driver.find_element(By.XPATH, "//div[contains(@class,'highlight-activity-tile')]//div[text()='Magic Show for Kids']").click()
    time.sleep(0.3)

    modal = driver.find_element(By.ID, "eventDetailsModal")
    assert modal.is_displayed()
    assert "Magic Show" in modal.text
    driver.find_element(By.XPATH, "//div[@id='eventDetailsModal']//i[contains(@class,'fa-xmark')]").click()
    time.sleep(0.3)
    assert not modal.is_displayed()

    # 2. Click Upcoming Event (Food Festival)
    driver.find_element(By.XPATH, "//div[contains(@class,'upcoming-event-row')]//div[text()='Food Festival']").click()
    time.sleep(0.3)

    assert modal.is_displayed()
    assert "Food" in modal.text
    driver.find_element(By.XPATH, "//div[@id='eventDetailsModal']//i[contains(@class,'fa-xmark')]").click()
    time.sleep(0.3)

def test_strict_kiosk_events_boundaries(driver, base_url):
    driver.get(f"{base_url}/kiosk/events.html")
    time.sleep(0.3)

    body_text = driver.find_element(By.TAG_NAME, "body").text.lower()
    assert "ticket sales dashboard" not in body_text
    assert "event organizer cms" not in body_text
    assert "gross gate revenue" not in body_text
    assert "artist backstage portal" not in body_text
