import time
from selenium.webdriver.common.by import By

def test_client_dashboard_page_loads(driver, base_url):
    driver.get(f"{base_url}/client-admin/dashboard.html")
    assert "Client Dashboard" in driver.title

    # 1. Verify Top Header & Active Sidebar Item
    assert "Client Dashboard" in driver.page_source
    active_nav = driver.find_element(By.CSS_SELECTOR, ".sidebar-nav .nav-item.active")
    assert "Dashboard" in active_nav.text

    # 2. Strict 8 Sidebar items check
    nav_items = driver.find_elements(By.CSS_SELECTOR, ".sidebar-nav .nav-item")
    assert len(nav_items) == 8
    nav_texts = [item.text.strip() for item in nav_items]
    assert "Dashboard" in nav_texts
    assert "Projects" in nav_texts
    assert "Content" in nav_texts
    assert "Themes" in nav_texts
    assert "Advertisements" in nav_texts
    assert "Analytics" in nav_texts
    assert "Feedback" in nav_texts
    assert "Requests" in nav_texts

    # 3. Verify 6 KPI boxes
    kpi_boxes = driver.find_elements(By.CLASS_NAME, "kpi-box")
    assert len(kpi_boxes) == 6
    page_text = driver.page_source
    assert "Total Visitors" in page_text
    assert "128,450" in page_text
    assert "Total Interactions" in page_text
    assert "321,845" in page_text
    assert "Top Sections Viewed" in page_text
    assert "Active Campaigns" in page_text
    assert "Avg. Satisfaction" in page_text
    assert "Pending Requests" in page_text

def test_client_projects_and_kiosk_status(driver, base_url):
    driver.get(f"{base_url}/client-admin/dashboard.html")
    time.sleep(0.3)

    page_text = driver.page_source
    # Projects
    assert "Phoenix Mall Project" in page_text
    assert "Phoenix Marketcity Project" in page_text
    assert "Phoenix Pallasio Project" in page_text
    assert "Phoenix Citadel Project" in page_text

    # Kiosks
    assert "Kiosk Status Overview" in page_text
    assert "30" in page_text
    assert "Total Kiosks" in page_text
    assert "Online" in page_text
    assert "24 (80%)" in page_text

def test_top_performing_sections_and_campaigns(driver, base_url):
    driver.get(f"{base_url}/client-admin/dashboard.html")
    time.sleep(0.3)

    page_text = driver.page_source
    # Top Sections
    assert "Top Performing Sections" in page_text
    assert "Offers & Deals" in page_text
    assert "18,420" in page_text
    assert "Store Directory" in page_text
    assert "Events" in page_text
    assert "Navigation" in page_text
    assert "Amenities" in page_text

    # Top Campaigns
    assert "Top Advertisement Campaigns" in page_text
    assert "Summer Sale 2025" in page_text
    assert "15,230" in page_text
    assert "Festive Offers" in page_text
    assert "Food Court Specials" in page_text

def test_recent_feedback_and_pending_requests(driver, base_url):
    driver.get(f"{base_url}/client-admin/dashboard.html")
    time.sleep(0.3)

    page_text = driver.page_source
    # Feedback
    assert "Recent Feedback Summary" in page_text
    assert "4.2" in page_text
    assert "Mall Experience" in page_text
    assert "Cleanliness" in page_text
    assert "Navigation" in page_text

    # Pending Requests
    assert "Pending Requests" in page_text
    assert "Add New Retailer: Miniso" in page_text
    assert "Update Food Court Map" in page_text
    assert "Add Summer Sale Advertisement" in page_text

def test_strict_client_admin_boundaries(driver, base_url):
    driver.get(f"{base_url}/client-admin/dashboard.html")
    buttons = driver.find_elements(By.TAG_NAME, "button")
    links = driver.find_elements(By.TAG_NAME, "a")
    interactive_texts = [b.text.strip().lower() for b in buttons + links if b.text]

    # Boundaries: No Company builder controls
    assert "create project" not in interactive_texts
    assert "create screen" not in interactive_texts
    assert "create theme" not in interactive_texts
    assert "create advertisement" not in interactive_texts
    assert "build experience" not in interactive_texts
    assert "edit map" not in interactive_texts
    assert "edit navigation" not in interactive_texts
    assert "publish" not in interactive_texts
    assert "release" not in interactive_texts
    assert "deploy" not in interactive_texts
