import time
from selenium.webdriver.common.by import By

def test_client_project_workspace_loads(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-overview.html")
    assert "Project Workspace" in driver.title

    # 1. Active Sidebar Item
    active_nav = driver.find_element(By.CSS_SELECTOR, ".sidebar-nav .nav-item.active")
    assert "Projects" in active_nav.text

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

    # 3. Breadcrumb & Project Name in Header
    page_text = driver.page_source
    assert "Phoenix Mall Project" in page_text
    assert "Active" in page_text

def test_project_workspace_tabs_and_subnavigation(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-overview.html")
    time.sleep(0.3)

    tabs = driver.find_elements(By.CSS_SELECTOR, ".project-subnav-tabs .project-subnav-tab")
    tab_names = [t.text.strip() for t in tabs]
    assert "Overview" in tab_names
    assert "Experience" in tab_names
    assert "Content" in tab_names
    assert "Themes" in tab_names
    assert "Advertisements" in tab_names
    assert "Preview" in tab_names
    assert "Analytics" in tab_names
    assert "Feedback" in tab_names
    assert "Requests" in tab_names

    # Overview is active
    active_tab = driver.find_element(By.CSS_SELECTOR, ".project-subnav-tabs .project-subnav-tab.active")
    assert "Overview" in active_tab.text

def test_project_hero_and_health_summary(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-overview.html")
    time.sleep(0.3)

    page_text = driver.page_source
    # Hero Info
    assert "Phoenix Mills, Mumbai, Maharashtra" in page_text
    assert "12 Kiosks" in page_text
    assert "v2.2.0" in page_text
    assert "18 May 2025" in page_text

    # Health Card
    assert "Project Health" in page_text
    assert "Excellent" in page_text
    assert "10 / 12" in page_text
    assert "100%" in page_text
    assert "98.6%" in page_text

def test_project_kpis_and_breakdowns(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-overview.html")
    time.sleep(0.3)

    page_text = driver.page_source
    # 6 KPIs
    assert "54,320" in page_text
    assert "132,450" in page_text
    assert "Top Sections Viewed" in page_text
    assert "Active Campaigns" in page_text
    assert "Avg. Satisfaction" in page_text
    assert "Pending Requests" in page_text

    # Kiosk Status
    assert "Kiosk Status" in page_text
    assert "10 (83.3%)" in page_text

    # Top Sections
    assert "Top Performing Sections" in page_text
    assert "Offers & Deals" in page_text
    assert "18,420" in page_text
    assert "Store Directory" in page_text

    # Top Campaigns
    assert "Top Advertisement Campaigns" in page_text
    assert "Summer Sale 2025" in page_text
    assert "15,230" in page_text
    assert "Festive Offers" in page_text

def test_strict_client_admin_workspace_boundaries(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-overview.html")
    buttons = driver.find_elements(By.TAG_NAME, "button")
    links = driver.find_elements(By.TAG_NAME, "a")
    interactive_texts = [b.text.strip().lower() for b in buttons + links if b.text]

    # Boundaries: No Company builder controls
    assert "create project" not in interactive_texts
    assert "delete project" not in interactive_texts
    assert "create screen" not in interactive_texts
    assert "create theme" not in interactive_texts
    assert "create advertisement" not in interactive_texts
    assert "build experience" not in interactive_texts
    assert "edit map" not in interactive_texts
    assert "create release" not in interactive_texts
    assert "deploy" not in interactive_texts
