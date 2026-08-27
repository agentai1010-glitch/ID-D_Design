import time
from selenium.webdriver.common.by import By

def test_device_management_page_loads(driver, base_url):
    driver.get(f"{base_url}/devices.html")
    assert "Device Management" in driver.title

    # 1. Verify Top Header & Active Sidebar Item
    assert "Device Management" in driver.page_source
    active_nav = driver.find_element(By.CSS_SELECTOR, ".sidebar-nav .nav-item.active")
    assert "Devices" in active_nav.text

    # 2. Verify 5 KPI summary boxes
    kpi_boxes = driver.find_elements(By.CLASS_NAME, "kpi-stat-box")
    assert len(kpi_boxes) >= 5
    page_text = driver.page_source
    assert "Total Devices" in page_text
    assert "Online Devices" in page_text
    assert "Offline Devices" in page_text
    assert "Needs Attention" in page_text
    assert "Avg. Device Health" in page_text

    # 3. Verify Selected Device Card
    sel_panel = driver.find_element(By.ID, "selectedDevicePanel")
    assert sel_panel.is_displayed()
    assert "Phoenix Mall - K01" in sel_panel.text

def test_device_table_and_selection(driver, base_url):
    driver.get(f"{base_url}/devices.html")
    time.sleep(0.3)

    # 1. Verify Table Rows
    rows = driver.find_elements(By.CSS_SELECTOR, "#devicesTableBody tr")
    assert len(rows) >= 7

    # 2. Select Westend Mall - K02 (Warning / Low Storage)
    dev_westend = driver.find_element(By.ID, "dev-westend-k02")
    dev_westend.click()
    time.sleep(0.3)

    # Verify right panel updated to Westend Mall - K02
    sel_panel = driver.find_element(By.ID, "selectedDevicePanel")
    assert "Westend Mall - K02" in sel_panel.text
    assert "KM-WND-0002" in sel_panel.text
    assert "Warning" in sel_panel.text
    assert "Low Storage" in sel_panel.text

    # 3. Select Phoenix Mall - K03 (Offline)
    dev_phoenix_k03 = driver.find_element(By.ID, "dev-phoenix-k03")
    dev_phoenix_k03.click()
    time.sleep(0.3)
    assert "Phoenix Mall - K03" in sel_panel.text
    assert "Offline" in sel_panel.text
    assert "KM-PMN-0003" in sel_panel.text

def test_device_details_modal_inspection(driver, base_url):
    driver.get(f"{base_url}/devices.html")
    time.sleep(0.3)

    # Click View Device Details CTA
    btn_details = driver.find_element(By.ID, "btnViewDeviceDetails")
    btn_details.click()
    time.sleep(0.3)

    # Verify modal is open and shows telemetry metrics
    modal = driver.find_element(By.ID, "deviceDetailsModal")
    assert modal.is_displayed()
    assert "Operational Status" in modal.text
    assert "Running Release" in modal.text
    assert "Telemetry Activity" in modal.text

def test_register_new_device_flow(driver, base_url):
    driver.get(f"{base_url}/devices.html")
    time.sleep(0.3)

    # Click Header Action: Register New Device
    reg_btn = driver.find_element(By.ID, "btnHeaderRegisterDevice")
    reg_btn.click()
    time.sleep(0.3)

    modal = driver.find_element(By.ID, "registerDeviceModal")
    assert modal.is_displayed()

    # Enter custom device details
    name_input = driver.find_element(By.ID, "newDevNameInput")
    name_input.clear()
    name_input.send_keys("Orion Mall - K03")

    id_input = driver.find_element(By.ID, "newDevIdInput")
    id_input.clear()
    id_input.send_keys("KM-ORN-0003")

    # Submit
    submit_btn = driver.find_element(By.ID, "btnSubmitRegisterDevice")
    submit_btn.click()
    time.sleep(0.4)

    # Verify modal closed and injected to table
    assert not modal.is_displayed()
    table = driver.find_element(By.ID, "devicesDataTable")
    assert "Orion Mall - K03" in table.text
    assert "KM-ORN-0003" in table.text
    assert "Pending" in table.text

    # Verify KPI counters updated
    total_kpi = driver.find_element(By.ID, "kpiTotalDevices").text
    assert total_kpi == "157"

def test_strict_business_boundaries_devices(driver, base_url):
    driver.get(f"{base_url}/devices.html")
    buttons = driver.find_elements(By.TAG_NAME, "button")
    links = driver.find_elements(By.TAG_NAME, "a")
    interactive_texts = [b.text.strip().lower() for b in buttons + links if b.text]

    # Boundaries: No template or theme creation
    assert "create template" not in interactive_texts
    assert "create theme" not in interactive_texts
