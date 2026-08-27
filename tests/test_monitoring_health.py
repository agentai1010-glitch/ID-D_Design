import time
from selenium.webdriver.common.by import By

def test_monitoring_page_loads(driver, base_url):
    driver.get(f"{base_url}/monitoring.html")
    assert "Monitoring" in driver.title

    # 1. Verify Top Header & Active Sidebar Item
    assert "Monitoring" in driver.page_source
    active_nav = driver.find_element(By.CSS_SELECTOR, ".sidebar-nav .nav-item.active")
    assert "Monitoring" in active_nav.text

    # 2. Verify 6 KPI summary boxes
    kpi_boxes = driver.find_elements(By.CLASS_NAME, "kpi-stat-box")
    assert len(kpi_boxes) >= 6
    page_text = driver.page_source
    assert "System Health" in page_text
    assert "Online Devices" in page_text
    assert "Active Kiosks" in page_text
    assert "Errors" in page_text
    assert "Alerts" in page_text
    assert "Avg. Response Time" in page_text

    # 3. Verify Selected Alert Card is displayed
    sel_panel = driver.find_element(By.ID, "selectedAlertPanel")
    assert sel_panel.is_displayed()
    assert "Phoenix Mall - K03 Offline" in sel_panel.text

def test_monitoring_alerts_table_and_selection(driver, base_url):
    driver.get(f"{base_url}/monitoring.html")
    time.sleep(0.3)

    # 1. Verify Table Rows
    rows = driver.find_elements(By.CSS_SELECTOR, "#alertsTableBody tr")
    assert len(rows) >= 5

    # 2. Select Westend Mall Low Storage alert (row-alrt-103)
    row_103 = driver.find_element(By.ID, "row-alrt-103")
    row_103.click()
    time.sleep(0.3)

    # Verify right panel updated to Westend Low Storage
    sel_panel = driver.find_element(By.ID, "selectedAlertPanel")
    assert "Westend Mall - K02 Low Storage" in sel_panel.text
    assert "Low Storage Space" in sel_panel.text
    assert "Westend Mall Project" in sel_panel.text
    assert "High" in sel_panel.text

    # 3. Select Skyline Mall Content Sync Failed (row-alrt-105)
    row_105 = driver.find_element(By.ID, "row-alrt-105")
    row_105.click()
    time.sleep(0.3)
    assert "Skyline Mall - K01 Content Sync Failed" in sel_panel.text
    assert "Sync Failure" in sel_panel.text

def test_alert_acknowledgement_flow(driver, base_url):
    driver.get(f"{base_url}/monitoring.html")
    time.sleep(0.3)

    # Select Phoenix Mall K03 (New)
    row_102 = driver.find_element(By.ID, "row-alrt-102")
    row_102.click()
    time.sleep(0.3)

    # Click Acknowledge
    ack_btn = driver.find_element(By.ID, "btnAcknowledgeAlert")
    ack_btn.click()
    time.sleep(0.3)

    # Accept alert dialog if present
    try:
        alert_dialog = driver.switch_to.alert
        alert_dialog.accept()
    except Exception:
        pass
    time.sleep(0.3)

    # Verify status changed to Acknowledged
    sel_status = driver.find_element(By.ID, "selAlertStatus").text
    assert "Acknowledged" in sel_status
    badge = driver.find_element(By.ID, "status-badge-alrt-102").text
    assert "Acknowledged" in badge

def test_monitoring_system_performance_and_breakdowns(driver, base_url):
    driver.get(f"{base_url}/monitoring.html")
    time.sleep(0.3)

    page_text = driver.page_source
    # Verify Performance indicators
    assert "API Response Time" in page_text
    assert "Content Delivery (CDN)" in page_text
    assert "Database Performance" in page_text
    assert "Sync Success Rate" in page_text

    # Verify Breakdowns
    assert "Alerts by Severity" in page_text
    assert "Alerts by Category" in page_text
    assert "Top Issues" in page_text

def test_strict_business_boundaries_monitoring(driver, base_url):
    driver.get(f"{base_url}/monitoring.html")
    buttons = driver.find_elements(By.TAG_NAME, "button")
    links = driver.find_elements(By.TAG_NAME, "a")
    interactive_texts = [b.text.strip().lower() for b in buttons + links if b.text]

    # Boundaries: No template or theme creation
    assert "create template" not in interactive_texts
    assert "create theme" not in interactive_texts
