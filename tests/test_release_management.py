import time
from selenium.webdriver.common.by import By

def test_release_management_page_loads(driver, base_url):
    driver.get(f"{base_url}/releases.html")
    assert "Release Management" in driver.title

    # 1. Verify Top Header & Active Sidebar Item
    assert "Release Management" in driver.page_source
    active_nav = driver.find_element(By.CSS_SELECTOR, ".sidebar-nav .nav-item.active")
    assert "Releases" in active_nav.text

    # 2. Verify 5 KPI summary boxes
    kpi_boxes = driver.find_elements(By.CLASS_NAME, "kpi-stat-box")
    assert len(kpi_boxes) >= 5
    page_text = driver.page_source
    assert "Total Releases" in page_text
    assert "Active Releases" in page_text
    assert "Scheduled Releases" in page_text
    assert "Release Health" in page_text
    assert "Failed Releases" in page_text

    # 3. Verify Selected Release Card
    sel_panel = driver.find_element(By.ID, "selectedReleasePanel")
    assert sel_panel.is_displayed()
    assert "Phoenix Mall Release" in sel_panel.text

def test_release_table_and_selection(driver, base_url):
    driver.get(f"{base_url}/releases.html")
    time.sleep(0.3)

    # 1. Verify Table Rows
    rows = driver.find_elements(By.CSS_SELECTOR, "#releasesTableBody tr")
    assert len(rows) >= 7

    # 2. Select Lakeside Mall Release (Failed deployment)
    rel_lakeside = driver.find_element(By.ID, "rel-lakeside")
    rel_lakeside.click()
    time.sleep(0.3)

    # Verify right panel updated to Lakeside
    sel_panel = driver.find_element(By.ID, "selectedReleasePanel")
    assert "Lakeside Mall Release" in sel_panel.text
    assert "v1.8.7" in sel_panel.text
    assert "Failed" in sel_panel.text
    assert "3 / 12 Deployment Failed" in sel_panel.text

    # 3. Select Orion Mall Release (Theme Release)
    rel_orion = driver.find_element(By.ID, "rel-orion")
    rel_orion.click()
    time.sleep(0.3)
    assert "Orion Mall Release" in sel_panel.text
    assert "Theme Release" in sel_panel.text
    assert "18 / 18 Kiosks Online" in sel_panel.text

def test_release_details_modal_and_manifest(driver, base_url):
    driver.get(f"{base_url}/releases.html")
    time.sleep(0.3)

    # Click View Release Details CTA
    btn_details = driver.find_element(By.ID, "btnViewReleaseDetails")
    btn_details.click()
    time.sleep(0.3)

    # Verify modal is open and shows manifest artifacts
    modal = driver.find_element(By.ID, "releaseDetailsModal")
    assert modal.is_displayed()
    assert "Manifest Artifacts" in modal.text
    assert "SHA256" in modal.text
    assert "Verification Status" in modal.text

def test_create_new_release_flow(driver, base_url):
    driver.get(f"{base_url}/releases.html")
    time.sleep(0.3)

    # Click Quick Action: Create New Release
    qa_btn = driver.find_element(By.ID, "qaCreateNewRelease")
    qa_btn.click()
    time.sleep(0.3)

    modal = driver.find_element(By.ID, "createReleaseModal")
    assert modal.is_displayed()

    # Enter custom release name & version
    name_input = driver.find_element(By.ID, "newRelNameInput")
    name_input.clear()
    name_input.send_keys("Phoenix Autumn Festive Release")

    ver_input = driver.find_element(By.ID, "newRelVersionInput")
    ver_input.clear()
    ver_input.send_keys("v2.3.0")

    # Submit
    submit_btn = driver.find_element(By.ID, "btnSubmitNewRelease")
    submit_btn.click()
    time.sleep(0.4)

    # Verify modal closed and injected to table
    assert not modal.is_displayed()
    table = driver.find_element(By.ID, "releasesDataTable")
    assert "Phoenix Autumn Festive Release" in table.text
    assert "v2.3.0" in table.text
    assert "Ready" in table.text

    # Verify KPI counters updated
    total_kpi = driver.find_element(By.ID, "kpiTotalReleases").text
    assert total_kpi == "19"

def test_strict_business_boundaries_releases(driver, base_url):
    driver.get(f"{base_url}/releases.html")
    buttons = driver.find_elements(By.TAG_NAME, "button")
    links = driver.find_elements(By.TAG_NAME, "a")
    interactive_texts = [b.text.strip().lower() for b in buttons + links if b.text]

    # Boundaries: No template or theme creation
    assert "create template" not in interactive_texts
    assert "create theme" not in interactive_texts
