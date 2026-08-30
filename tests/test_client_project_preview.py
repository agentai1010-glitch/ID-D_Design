import time
from selenium.webdriver.common.by import By

def test_client_project_preview_page_loads(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-preview.html")
    assert "Preview" in driver.title

    # 1. Active Sidebar Item is Projects
    active_nav = driver.find_element(By.CSS_SELECTOR, ".sidebar-nav .nav-item.active")
    assert "Projects" in active_nav.text

    # 2. Strict 8 Sidebar items check
    nav_items = driver.find_elements(By.CSS_SELECTOR, ".sidebar-nav .nav-item")
    assert len(nav_items) == 8

    # 3. Breadcrumb & Project Name in Header
    page_text = driver.page_source
    assert "Phoenix Mall Project" in page_text
    assert "Preview" in page_text
    assert "Active" in page_text

    # 4. Project subnav active tab is Preview
    active_tab = driver.find_element(By.CSS_SELECTOR, ".project-subnav-tabs .project-subnav-tab.active")
    assert "Preview" in active_tab.text

def test_preview_controls_and_options(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-preview.html")
    time.sleep(0.3)
    body_text = driver.find_element(By.TAG_NAME, "body").text

    # Controls
    assert "Preview Controls" in body_text
    assert "Kiosk Screen" in body_text
    assert "Mobile View" in body_text
    assert "Tablet View" in body_text
    assert "Portrait (27\")" in body_text
    assert "Landscape (32\")" in body_text
    assert "Live Experience" in body_text
    assert "Refresh Content" in body_text

    # Switch device to Mobile View
    driver.find_element(By.ID, "optDevMobile").click()
    time.sleep(0.3)
    bezel = driver.find_element(By.ID, "mainKioskBezel")
    assert "mobile-mode" in bezel.get_attribute("class")

    # Switch orientation to Landscape
    driver.find_element(By.ID, "optOriLandscape").click()
    time.sleep(0.3)
    assert "landscape-mode" in bezel.get_attribute("class")

def test_kiosk_preview_home_and_interaction_flow(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-preview.html")
    time.sleep(0.3)
    body_text = driver.find_element(By.TAG_NAME, "body").text

    # Kiosk elements
    assert "PHOENIX MALL" in body_text
    assert "SUMMER" in body_text
    assert "SALE" in body_text
    assert "Stores & Brands" in body_text
    assert "Amenities" in body_text
    assert "Food Court" in body_text
    assert "Offers & Promotions" in body_text

    # 1. Click on Stores & Brands tile -> should open Store Details
    driver.find_element(By.XPATH, "//div[@class='kiosk-tile']//span[text()='Stores & Brands']").click()
    time.sleep(0.3)
    kiosk_text = driver.find_element(By.ID, "kioskScreenContainer").text
    assert "ADIDAS" in kiosk_text
    assert "Take Me There" in kiosk_text

    # 2. Click Take Me There -> should open Interactive Wayfinding Map
    driver.find_element(By.XPATH, "//button[contains(., 'Take Me There')]").click()
    time.sleep(0.3)
    kiosk_text = driver.find_element(By.ID, "kioskScreenContainer").text
    assert "Interactive Wayfinding" in kiosk_text
    assert "Route: You Are at Kiosk 01" in kiosk_text

    # 3. Click Kiosk Bottom Nav Home -> returns to Home
    driver.find_element(By.ID, "kioskBtnHome").click()
    time.sleep(0.3)
    kiosk_text = driver.find_element(By.ID, "kioskScreenContainer").text
    assert "SUMMER" in kiosk_text

def test_screen_navigation_shortcuts(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-preview.html")
    time.sleep(0.3)

    # Click Map & Navigation shortcut on right panel
    driver.find_element(By.ID, "navItemMap").click()
    time.sleep(0.3)
    kiosk_text = driver.find_element(By.ID, "kioskScreenContainer").text
    assert "Interactive Wayfinding" in kiosk_text

    # Click Feedback shortcut
    driver.find_element(By.ID, "navItemFeedback").click()
    time.sleep(0.3)
    kiosk_text = driver.find_element(By.ID, "kioskScreenContainer").text
    assert "Visitor Feedback" in kiosk_text

def test_share_preview_modal(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-preview.html")
    time.sleep(0.3)

    # Click Share Preview
    driver.find_element(By.ID, "btnSharePreview").click()
    time.sleep(0.3)

    modal = driver.find_element(By.ID, "sharePreviewModal")
    assert modal.is_displayed()
    assert "Share Kiosk Preview" in modal.text

    # Close modal
    driver.find_element(By.XPATH, "//div[@id='sharePreviewModal']//button[text()='Close']").click()
    time.sleep(0.3)
    assert not modal.is_displayed()

def test_strict_preview_boundaries(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-preview.html")
    page_text = driver.page_source.lower()

    # Boundaries: Read-only simulation, no builders, no map editor, no analytics charts
    assert "drag and drop" not in page_text
    assert "screen builder" not in page_text
    assert "theme builder" not in page_text
    assert "draw route" not in page_text
    assert "visitor analytics" not in page_text
