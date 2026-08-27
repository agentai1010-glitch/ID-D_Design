import time
from selenium.webdriver.common.by import By

def test_template_management_page_loads(driver, base_url):
    driver.get(f"{base_url}/templates.html")
    assert "Templates" in driver.title or "Kiosk Platform" in driver.title

    # 1. Verify Top Header and Breadcrumbs
    assert "Templates" in driver.page_source
    active_nav = driver.find_element(By.CSS_SELECTOR, ".sidebar-nav .nav-item.active")
    assert "Templates" in active_nav.text

    # 2. Verify 5 KPI summary cards
    kpi_boxes = driver.find_elements(By.CLASS_NAME, "kpi-stat-box")
    assert len(kpi_boxes) == 5
    page_text = driver.page_source
    assert "Total Templates" in page_text
    assert "Assigned Clients" in page_text
    assert "Active Projects" in page_text
    assert "Available Themes" in page_text
    assert "Latest Version" in page_text

    # 3. Verify top CTA button
    view_exp_btn = driver.find_element(By.LINK_TEXT, "View Template Experience")
    assert view_exp_btn.is_displayed()

def test_template_table_and_details(driver, base_url):
    driver.get(f"{base_url}/templates.html")
    
    # Verify primary template row
    table = driver.find_element(By.ID, "templatesDataTable")
    assert "Mall / Indoor Venue" in table.text
    assert "Mall" in table.text
    assert "v2.1" in table.text
    assert "Active" in table.text
    assert "18" in table.text  # Assigned Clients
    assert "27" in table.text  # Active Projects
    assert "4" in table.text   # Themes

    # Verify right preview card
    assert "Product Engineering Team" in driver.page_source
    assert "Version 2.1" in driver.page_source

def test_template_seven_tabs_navigation(driver, base_url):
    driver.get(f"{base_url}/templates.html")
    time.sleep(0.3)

    # 1. Overview Tab (Default active)
    pane_overview = driver.find_element(By.ID, "paneOverview")
    assert pane_overview.is_displayed()
    assert "About This Template" in pane_overview.text
    assert "Core Modules" in pane_overview.text
    assert "Key Capabilities" in pane_overview.text

    # 2. Switch to Template Experience Tab
    tab_exp = driver.find_element(By.ID, "tabBtnExperience")
    tab_exp.click()
    time.sleep(0.3)
    pane_exp = driver.find_element(By.ID, "paneExperience")
    assert pane_exp.is_displayed()
    assert "Launch Full Interactive Kiosk Simulator" in pane_exp.text

    # 3. Switch to Features & Capabilities Tab
    tab_feat = driver.find_element(By.ID, "tabBtnFeatures")
    tab_feat.click()
    time.sleep(0.3)
    pane_feat = driver.find_element(By.ID, "paneFeatures")
    assert pane_feat.is_displayed()
    assert "Detailed Architecture & Feature Matrix" in pane_feat.text
    assert "2.5D Indoor Maps" in pane_feat.text

    # 4. Switch to Themes Tab
    tab_themes = driver.find_element(By.ID, "tabBtnThemes")
    tab_themes.click()
    time.sleep(0.3)
    pane_themes = driver.find_element(By.ID, "paneThemes")
    assert pane_themes.is_displayed()
    assert "Default Mall Luxury" in pane_themes.text
    assert "Diwali Festive 2024" in pane_themes.text

    # 5. Switch to Clients Tab
    tab_clients = driver.find_element(By.ID, "tabBtnClients")
    tab_clients.click()
    time.sleep(0.3)
    pane_clients = driver.find_element(By.ID, "paneClients")
    assert pane_clients.is_displayed()
    assert "Phoenix Mills Ltd." in pane_clients.text

    # 6. Switch to Projects Tab
    tab_proj = driver.find_element(By.ID, "tabBtnProjects")
    tab_proj.click()
    time.sleep(0.3)
    pane_proj = driver.find_element(By.ID, "paneProjects")
    assert pane_proj.is_displayed()
    assert "Phoenix Mall Main Atrium" in pane_proj.text

    # 7. Switch to Changelog Tab
    tab_log = driver.find_element(By.ID, "tabBtnChangelog")
    tab_log.click()
    time.sleep(0.3)
    pane_log = driver.find_element(By.ID, "paneChangelog")
    assert pane_log.is_displayed()
    assert "Version 2.1" in pane_log.text
    assert "Version 2.0" in pane_log.text

def test_strict_business_boundaries(driver, base_url):
    driver.get(f"{base_url}/templates.html")
    buttons = driver.find_elements(By.TAG_NAME, "button")
    links = driver.find_elements(By.TAG_NAME, "a")
    interactive_texts = [b.text.strip().lower() for b in buttons + links if b.text]

    # Strict Company Admin rules: No template or theme creation buttons
    assert "create template" not in interactive_texts
    assert "create new template" not in interactive_texts
    assert "build template" not in interactive_texts
    assert "create theme" not in interactive_texts
    assert "create new theme" not in interactive_texts
    assert "add theme" not in interactive_texts
