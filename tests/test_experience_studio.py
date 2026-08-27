import time
from selenium.webdriver.common.by import By

def test_experience_studio_page_loads(driver, base_url):
    driver.get(f"{base_url}/experience-studio.html")
    assert "Experience Studio" in driver.title

    # 1. Verify Top Header & Breadcrumbs
    assert "Experience Studio" in driver.page_source
    active_nav = driver.find_element(By.CSS_SELECTOR, ".sidebar-nav .nav-item.active")
    assert "Experience Studio" in active_nav.text

    # 2. Verify 5 KPI summary boxes
    kpi_boxes = driver.find_elements(By.CLASS_NAME, "kpi-stat-box")
    assert len(kpi_boxes) >= 5
    page_text = driver.page_source
    assert "Total Experiences" in page_text
    assert "Total Screens" in page_text
    assert "Components" in page_text
    assert "Content Items" in page_text
    assert "Experience Health" in page_text

    # 3. Verify Experience Details Card & Preview CTA
    preview_btn = driver.find_element(By.ID, "btnPreviewExperience")
    assert preview_btn.is_displayed()
    assert "Preview Experience" in preview_btn.text

def test_screen_map_and_node_selection(driver, base_url):
    driver.get(f"{base_url}/experience-studio.html")
    time.sleep(0.3)

    # 1. Verify Screen Map root and child nodes
    canvas = driver.find_element(By.ID, "screenMapCanvas")
    assert "01" in canvas.text
    assert "Home" in canvas.text
    assert "03" in canvas.text
    assert "Stores & Brands" in canvas.text
    assert "08" in canvas.text
    assert "Store Detail" in canvas.text

    # 2. Click Store Detail node (08)
    node_08 = driver.find_element(By.ID, "node-08")
    node_08.click()
    time.sleep(0.3)

    # Verify right panel updated to Store Detail
    exp_details = driver.find_element(By.ID, "experienceDetailsPanel")
    assert "Store Detail (SCR-008)" in exp_details.text
    assert "Store Profile" in exp_details.text

def test_context_tabs_navigation(driver, base_url):
    driver.get(f"{base_url}/experience-studio.html")
    time.sleep(0.3)

    # 1. Screens Tab Table
    pane_screens = driver.find_element(By.ID, "paneScreens")
    assert pane_screens.is_displayed()
    assert "SCR-001" in pane_screens.text
    assert "SCR-002" in pane_screens.text

    # 2. Components Tab
    tab_components = driver.find_element(By.ID, "tabBtnComponents")
    tab_components.click()
    time.sleep(0.3)
    pane_components = driver.find_element(By.ID, "paneComponents")
    assert pane_components.is_displayed()
    assert "Store Card" in pane_components.text

    # 3. Content Tab
    tab_content = driver.find_element(By.ID, "tabBtnContent")
    tab_content.click()
    time.sleep(0.3)
    pane_content = driver.find_element(By.ID, "paneContent")
    assert pane_content.is_displayed()
    assert "Store Detail Screen" in pane_content.text

    # 4. Navigation Flow Tab
    tab_nav = driver.find_element(By.ID, "tabBtnNavigation")
    tab_nav.click()
    time.sleep(0.3)
    pane_nav = driver.find_element(By.ID, "paneNavigation")
    assert pane_nav.is_displayed()
    assert "Home → Stores & Brands" in pane_nav.text or "Home" in pane_nav.text

    # 5. Localization Tab
    tab_loc = driver.find_element(By.ID, "tabBtnLocalization")
    tab_loc.click()
    time.sleep(0.3)
    pane_loc = driver.find_element(By.ID, "paneLocalization")
    assert pane_loc.is_displayed()
    assert "English" in pane_loc.text
    assert "Hindi" in pane_loc.text

def test_create_new_screen_draft_journey(driver, base_url):
    driver.get(f"{base_url}/experience-studio.html")
    time.sleep(0.3)

    # Click Quick Action: Create New Screen
    qa_btn = driver.find_element(By.ID, "qaCreateNewScreen")
    qa_btn.click()
    time.sleep(0.3)

    # Modal should be displayed
    modal = driver.find_element(By.ID, "createScreenModal")
    assert modal.is_displayed()

    # Enter custom screen name
    name_input = driver.find_element(By.ID, "newScreenNameInput")
    name_input.clear()
    name_input.send_keys("Summer Festival Screen")

    # Click Save Screen as Draft
    save_btn = driver.find_element(By.ID, "btnSaveScreenDraft")
    save_btn.click()
    time.sleep(0.4)

    # Verify modal closed and draft added to table
    assert not modal.is_displayed()
    table = driver.find_element(By.ID, "screensDataTable")
    assert "Summer Festival Screen" in table.text
    assert "SCR-043" in table.text
    assert "Draft" in table.text

    # Verify counters incremented
    kpi_screens = driver.find_element(By.ID, "kpiTotalScreens").text
    assert kpi_screens == "43"

def test_strict_business_boundaries_experience(driver, base_url):
    driver.get(f"{base_url}/experience-studio.html")
    buttons = driver.find_elements(By.TAG_NAME, "button")
    links = driver.find_elements(By.TAG_NAME, "a")
    interactive_texts = [b.text.strip().lower() for b in buttons + links if b.text]

    # Boundaries: No template or theme creation
    assert "create template" not in interactive_texts
    assert "create new template" not in interactive_texts
    assert "create theme" not in interactive_texts
    assert "create new theme" not in interactive_texts
