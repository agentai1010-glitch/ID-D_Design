import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_client_project_themes_page_loads(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-themes.html")
    assert "Themes" in driver.title

    # 1. Active Sidebar Item is Projects
    active_nav = driver.find_element(By.CSS_SELECTOR, ".sidebar-nav .nav-item.active")
    assert "Projects" in active_nav.text

    # 2. Strict 8 Sidebar items check
    nav_items = driver.find_elements(By.CSS_SELECTOR, ".sidebar-nav .nav-item")
    assert len(nav_items) == 8

    # 3. Breadcrumb & Project Name in Header
    page_text = driver.page_source
    assert "Phoenix Mall Project" in page_text
    assert "Themes" in page_text
    assert "Active" in page_text

    # 4. Project subnav active tab is Themes
    active_tab = driver.find_element(By.CSS_SELECTOR, ".project-subnav-tabs .project-subnav-tab.active")
    assert "Themes" in active_tab.text

def test_theme_summary_kpis(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-themes.html")
    time.sleep(0.3)
    page_text = driver.page_source

    # 5 KPI summary cards
    assert "Total Themes" in page_text
    assert "Available themes" in page_text

    assert "Active Theme" in page_text
    assert "Summer 2025" in page_text
    assert "Currently applied" in page_text

    assert "Last Applied" in page_text
    assert "18 May 2025" in page_text

    assert "Applied On Kiosks" in page_text
    assert "12 / 12" in page_text
    assert "All kiosks updated" in page_text

    assert "Theme Impact" in page_text
    assert "+18.6%" in page_text

def test_available_themes_table_and_filtering(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-themes.html")
    time.sleep(0.3)
    page_text = driver.page_source

    assert "Available Themes" in page_text
    assert "Request New Theme" in page_text

    # 8 rows present in table
    rows = driver.find_elements(By.CSS_SELECTOR, "#themesDataTable tbody tr")
    assert len(rows) == 8

    # Search filter testing
    search_input = driver.find_element(By.ID, "searchThemesInput")
    search_input.clear()
    search_input.send_keys("Diwali")
    time.sleep(0.2)
    visible_rows = [r for r in driver.find_elements(By.CSS_SELECTOR, "#themesDataTable tbody tr") if r.is_displayed()]
    assert len(visible_rows) == 1
    assert "Diwali 2024" in visible_rows[0].text

    # Clear search
    search_input.clear()
    search_input.send_keys(Keys.BACKSPACE)
    time.sleep(0.2)

def test_theme_selection_and_apply_flow(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-themes.html")
    time.sleep(0.3)

    # 1. Select "New Year 2025" row
    new_year_row = driver.find_element(By.ID, "row-new-year-2025")
    new_year_row.click()
    time.sleep(0.2)

    # 2. Details panel updates
    dt_name = driver.find_element(By.ID, "dtThemeName").text
    assert "New Year 2025" in dt_name

    # 3. Apply Theme button is clickable
    apply_btn = driver.find_element(By.ID, "btnApplyThemeAction")
    assert "Apply Theme" in apply_btn.text
    apply_btn.click()
    time.sleep(0.2)

    # 4. Confirmation modal opens
    modal = driver.find_element(By.ID, "applyThemeModal")
    assert modal.is_displayed()
    assert 'Apply "New Year 2025"?' in modal.text

    # 5. Confirm apply
    confirm_btn = driver.find_element(By.ID, "btnConfirmApply")
    confirm_btn.click()
    time.sleep(0.3)

    # Accept any alert popup if present
    try:
        alert = driver.switch_to.alert
        alert.accept()
    except Exception:
        pass

    # 6. Active theme KPI updated
    kpi_active = driver.find_element(By.ID, "kpiActiveThemeName").text
    assert "New Year 2025" in kpi_active

def test_strict_client_admin_theme_boundaries(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-themes.html")
    buttons = driver.find_elements(By.TAG_NAME, "button")
    links = driver.find_elements(By.TAG_NAME, "a")
    interactive_texts = [b.text.strip().lower() for b in buttons + links if b.text]

    # Boundaries: No Company builder controls
    assert "create theme" not in interactive_texts
    assert "design theme" not in interactive_texts
    assert "edit theme" not in interactive_texts
    assert "theme builder" not in interactive_texts
    assert "add component" not in interactive_texts
    assert "publish" not in interactive_texts
    assert "release" not in interactive_texts
    assert "deploy" not in interactive_texts
