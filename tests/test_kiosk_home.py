import time
from selenium.webdriver.common.by import By

def test_kiosk_home_page_loads(driver, base_url):
    driver.get(f"{base_url}/kiosk/home.html")
    assert "Grand Metro Mall" in driver.title

    # Header elements
    body_text = driver.find_element(By.TAG_NAME, "body").text
    assert "28°C" in body_text
    assert "Sunny" in body_text
    assert "GRAND" in body_text
    assert "METRO MALL" in body_text
    assert "CELEBRATE EVERYDAY" in body_text
    assert "Scan to Explore" in body_text

    # Footer Home button
    home_btn = driver.find_element(By.ID, "btnKioskHome")
    assert "HOME" in home_btn.text

def test_kiosk_8_primary_destinations(driver, base_url):
    driver.get(f"{base_url}/kiosk/home.html")
    time.sleep(0.3)
    body_text = driver.find_element(By.TAG_NAME, "body").text

    # Verify all 8 primary navigation destinations
    assert "SHOP" in body_text
    assert "STORES & BRANDS" in body_text

    assert "FOOD & DINING" in body_text
    assert "CAFES, RESTAURANTS" in body_text

    assert "OFFERS & DEALS" in body_text
    assert "DISCOUNTS & MORE" in body_text

    assert "EVENTS" in body_text
    assert "WHAT'S HAPPENING" in body_text

    assert "MALL MAP" in body_text
    assert "FIND YOUR WAY" in body_text

    assert "MOVIES" in body_text
    assert "NOW SHOWING" in body_text

    assert "PARKING" in body_text
    assert "INFO & AVAILABILITY" in body_text

    assert "SERVICES & FACILITIES" in body_text
    assert "AMENITIES & MORE" in body_text

    # Test Shop navigation
    driver.find_element(By.ID, "cardShop").click()
    time.sleep(0.4)
    assert "shop.html" in driver.current_url

def test_featured_promotional_carousel(driver, base_url):
    driver.get(f"{base_url}/kiosk/home.html")
    time.sleep(0.3)

    # Initial slide contains Festive Sale
    slide1 = driver.find_element(By.ID, "promoSlide1")
    assert "FESTIVE" in slide1.text
    assert "SALE" in slide1.text
    assert "UP TO 50% OFF" in slide1.text
    assert "EXPLORE OFFERS" in slide1.text

    # Switch to slide 2
    dots = driver.find_elements(By.CSS_SELECTOR, ".carousel-dot")
    assert len(dots) >= 3
    dots[1].click()
    time.sleep(0.4)

    slide2 = driver.find_element(By.ID, "promoSlide2")
    assert "BLEU DE CHANEL" in slide2.text

def test_search_entry_and_overlay(driver, base_url):
    driver.get(f"{base_url}/kiosk/home.html")
    time.sleep(0.3)

    # Click search bar to navigate to Search & Discovery
    search_bar = driver.find_element(By.CSS_SELECTOR, ".horizontal-search-bar")
    search_bar.click()
    time.sleep(0.4)

    assert "search.html" in driver.current_url
    assert "Search & Discovery" in driver.title

def test_scan_to_explore_modal(driver, base_url):
    driver.get(f"{base_url}/kiosk/home.html")
    time.sleep(0.3)

    # Click Scan to Explore
    driver.find_element(By.ID, "btnScanToExplore").click()
    time.sleep(0.3)

    modal = driver.find_element(By.ID, "scanExploreModal")
    assert modal.is_displayed()
    assert "Scan to Explore on Mobile" in modal.text
    assert "Send SMS Link" in modal.text

    # Close modal
    driver.find_element(By.XPATH, "//div[@id='scanExploreModal']//button[text()='Close']").click()
    time.sleep(0.3)
    assert not modal.is_displayed()

def test_language_and_help_modals(driver, base_url):
    driver.get(f"{base_url}/kiosk/home.html")
    time.sleep(0.3)

    # 1. Language modal
    driver.find_element(By.ID, "btnLanguage").click()
    time.sleep(0.3)
    lang_modal = driver.find_element(By.ID, "languageModal")
    assert lang_modal.is_displayed()
    assert "Select Language" in lang_modal.text
    assert "मराठी" in lang_modal.text

    driver.find_element(By.XPATH, "//div[@id='languageModal']//button[text()='Close']").click()
    time.sleep(0.3)
    assert not lang_modal.is_displayed()

    # 2. Help modal
    driver.find_element(By.ID, "btnHelp").click()
    time.sleep(0.3)
    help_modal = driver.find_element(By.ID, "helpModal")
    assert help_modal.is_displayed()
    assert "Need Assistance?" in help_modal.text
    assert "+91 20 6645 8888" in help_modal.text

    driver.find_element(By.XPATH, "//div[@id='helpModal']//button[text()='Close']").click()
    time.sleep(0.3)
    assert not help_modal.is_displayed()

def test_parking_and_services_modals(driver, base_url):
    driver.get(f"{base_url}/kiosk/home.html")
    time.sleep(0.3)

    # 1. Parking Modal
    driver.find_element(By.ID, "cardParking").click()
    time.sleep(0.3)
    parking_modal = driver.find_element(By.ID, "parkingModal")
    assert parking_modal.is_displayed()
    assert "Live Parking Availability" in parking_modal.text
    assert "240 Slots" in parking_modal.text

    driver.find_element(By.XPATH, "//div[@id='parkingModal']//button[text()='Close']").click()
    time.sleep(0.3)
    assert not parking_modal.is_displayed()

    # 2. Services Modal
    driver.find_element(By.ID, "cardServices").click()
    time.sleep(0.3)
    services_modal = driver.find_element(By.ID, "servicesModal")
    assert services_modal.is_displayed()
    assert "Services & Facilities" in services_modal.text
    assert "Washrooms" in services_modal.text
    assert "ATMs & Banking" in services_modal.text

    driver.find_element(By.XPATH, "//div[@id='servicesModal']//button[text()='Close']").click()
    time.sleep(0.3)
    assert not services_modal.is_displayed()

def test_strict_kiosk_boundaries(driver, base_url):
    driver.get(f"{base_url}/kiosk/home.html")
    page_text = driver.page_source.lower()

    # Boundaries: No admin sidebars, no editing builder, no analytics graphs
    assert "client admin" not in page_text
    assert "company admin" not in page_text
    assert "drag and drop" not in page_text
    assert "visitor analytics" not in page_text
