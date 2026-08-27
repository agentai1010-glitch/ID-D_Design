import time
from selenium.webdriver.common.by import By

def test_project_management_page_loads(driver, base_url):
    driver.get(f"{base_url}/projects.html")
    assert "Project Management" in driver.page_source or "Projects" in driver.title

    # 1. Verify Top Header and Breadcrumbs
    assert "Project Management" in driver.page_source
    active_nav = driver.find_element(By.CSS_SELECTOR, ".sidebar-nav .nav-item.active")
    assert "Projects" in active_nav.text

    # 2. Verify 5 KPI summary cards
    kpi_boxes = driver.find_elements(By.CLASS_NAME, "kpi-stat-box")
    assert len(kpi_boxes) >= 5
    page_text = driver.page_source
    assert "Total Projects" in page_text
    assert "Total Kiosks" in page_text
    assert "Active Releases" in page_text
    assert "Pending Requests" in page_text
    assert "Avg. Experience Health" in page_text

    # 3. Verify top CTA button
    init_btn = driver.find_element(By.ID, "btnInitNewProject")
    assert init_btn.is_displayed()
    assert "Initialize New Project" in init_btn.text

def test_project_table_and_selection(driver, base_url):
    driver.get(f"{base_url}/projects.html")
    time.sleep(0.3)

    # 1. Verify Projects table contains primary entries
    table = driver.find_element(By.ID, "projectsDataTable")
    assert "Phoenix Mall Project" in table.text
    assert "Orion Mall Project" in table.text
    assert "Skyline Mall Project" in table.text
    assert "Mall / Indoor Venue" in table.text

    # 2. Verify default selected project in right panel
    sel_panel = driver.find_element(By.ID, "selectedProjectPanel")
    assert "Phoenix Mall Project" in sel_panel.text
    assert "Phoenix Mills, Lower Parel, Mumbai" in sel_panel.text
    assert "Mall / Indoor Venue (v2.1)" in sel_panel.text
    assert "28 (26 Online / 2 Offline)" in sel_panel.text
    assert "98% (Excellent)" in sel_panel.text

    # 3. Click Orion Mall row and verify selected panel updates
    row_orion = driver.find_element(By.ID, "row-orion")
    row_orion.click()
    time.sleep(0.3)

    sel_panel_after = driver.find_element(By.ID, "selectedProjectPanel")
    assert "Orion Mall Project" in sel_panel_after.text
    assert "Brigade Gateway, Rajajinagar, Bangalore" in sel_panel_after.text
    assert "Vikram Sen" in sel_panel_after.text

def test_project_detail_navigation_and_tabs(driver, base_url):
    driver.get(f"{base_url}/projects.html")
    time.sleep(0.3)

    # Click View Project Details button
    view_details_btn = driver.find_element(By.ID, "btnViewProjectDetails")
    view_details_btn.click()
    time.sleep(0.5)

    # Verify Project Details page loaded
    assert "Phoenix Mall Project" in driver.page_source
    assert "Project Details" in driver.page_source

    # 1. Overview Tab
    pane_overview = driver.find_element(By.ID, "pPaneOverview")
    assert pane_overview.is_displayed()
    assert "Experience Configuration" in pane_overview.text
    assert "Venue Content" in pane_overview.text
    assert "2.5D Indoor Maps" in pane_overview.text

    # 2. Switch to Experience Tab
    tab_exp = driver.find_element(By.ID, "pTabExperience")
    tab_exp.click()
    time.sleep(0.3)
    pane_exp = driver.find_element(By.ID, "pPaneExperience")
    assert pane_exp.is_displayed()
    assert "Project Experience Configuration" in pane_exp.text

    # 3. Switch to Maps Tab
    tab_maps = driver.find_element(By.ID, "pTabMaps")
    tab_maps.click()
    time.sleep(0.3)
    pane_maps = driver.find_element(By.ID, "pPaneMaps")
    assert pane_maps.is_displayed()
    assert "Ground Floor" in pane_maps.text
    assert "First Floor" in pane_maps.text

    # 4. Switch to Navigation Tab
    tab_nav = driver.find_element(By.ID, "pTabNavigation")
    tab_nav.click()
    time.sleep(0.3)
    pane_nav = driver.find_element(By.ID, "pPaneNavigation")
    assert pane_nav.is_displayed()
    assert "Wayfinding & Routing Configuration" in pane_nav.text

    # 5. Switch to Releases Tab
    tab_rel = driver.find_element(By.ID, "pTabReleases")
    tab_rel.click()
    time.sleep(0.3)
    pane_rel = driver.find_element(By.ID, "pPaneReleases")
    assert pane_rel.is_displayed()
    assert "Release v2.1.0" in pane_rel.text

def test_strict_business_boundaries_projects(driver, base_url):
    driver.get(f"{base_url}/projects.html")
    buttons = driver.find_elements(By.TAG_NAME, "button")
    links = driver.find_elements(By.TAG_NAME, "a")
    interactive_texts = [b.text.strip().lower() for b in buttons + links if b.text]

    # Company Admin rules: No template creation or theme creation actions
    assert "create template" not in interactive_texts
    assert "create new template" not in interactive_texts
    assert "build template" not in interactive_texts
    assert "create theme" not in interactive_texts
    assert "create new theme" not in interactive_texts
