import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def test_client_project_requests_page_loads(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-requests.html")
    assert "Requests" in driver.title

    # 1. Active Sidebar Item is Projects
    active_nav = driver.find_element(By.CSS_SELECTOR, ".sidebar-nav .nav-item.active")
    assert "Projects" in active_nav.text

    # 2. Strict 8 Sidebar items check
    nav_items = driver.find_elements(By.CSS_SELECTOR, ".sidebar-nav .nav-item")
    assert len(nav_items) == 8

    # 3. Breadcrumb & Project Name in Header
    page_text = driver.page_source
    assert "Phoenix Mall Project" in page_text
    assert "Requests" in page_text
    assert "Active" in page_text

    # 4. Project subnav active tab is Requests
    active_tab = driver.find_element(By.CSS_SELECTOR, ".project-subnav-tabs .project-subnav-tab.active")
    assert "Requests" in active_tab.text

def test_requests_kpi_summary(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-requests.html")
    time.sleep(0.3)
    body_text = driver.find_element(By.TAG_NAME, "body").text

    # 5 KPI summary cards
    assert "Total Requests" in body_text
    assert "156" in body_text

    assert "Pending" in body_text
    assert "42" in body_text

    assert "In Progress" in body_text
    assert "38" in body_text

    assert "Under Review" in body_text
    assert "22" in body_text

    assert "Completed" in body_text
    assert "54" in body_text

    # Bottom metrics
    assert "Average Resolution Time" in body_text
    assert "3d 14h" in body_text
    assert "Completion Rate" in body_text
    assert "34.6%" in body_text
    assert "SLA Compliance" in body_text
    assert "92.3%" in body_text

def test_requests_table_and_filtering(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-requests.html")
    time.sleep(0.3)
    body_text = driver.find_element(By.TAG_NAME, "body").text

    # 6 Mock Requests Present
    assert "Update store information" in body_text
    assert "Navigation to Food Court" in body_text
    assert "Add new store - H&M" in body_text
    assert "Change kiosk welcome screen" in body_text
    assert "Fix map near Parking Area" in body_text
    assert "Advertisement content change" in body_text

    # Filter by Status: "Under Review"
    status_select = Select(driver.find_element(By.ID, "requestStatusFilter"))
    status_select.select_by_value("Under Review")
    time.sleep(0.3)

    visible_rows = [r for r in driver.find_elements(By.CSS_SELECTOR, "#requestsDataTable tbody tr") if r.is_displayed()]
    assert len(visible_rows) == 1
    assert "Navigation to Food Court" in visible_rows[0].text

    # Clear filters
    driver.find_element(By.XPATH, "//button[contains(., 'Clear Filters')]").click()
    time.sleep(0.3)
    all_rows = [r for r in driver.find_elements(By.CSS_SELECTOR, "#requestsDataTable tbody tr") if r.is_displayed()]
    assert len(all_rows) == 6

def test_new_request_modal_flow_and_submission(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-requests.html")
    time.sleep(0.3)

    # 1. Open New Request Modal
    driver.find_element(By.ID, "btnNewRequest").click()
    time.sleep(0.3)

    modal = driver.find_element(By.ID, "newRequestModal")
    assert modal.is_displayed()

    # 2. Fill form
    type_select = Select(driver.find_element(By.ID, "modalRequestType"))
    type_select.select_by_value("Navigation & Map")

    driver.find_element(By.ID, "modalRequestTitle").send_keys("Add EV Charging Station to Map")
    driver.find_element(By.ID, "modalRequestDesc").send_keys("Include 6 new EV charging bays near Basement B2.")

    # 3. Submit Form
    driver.find_element(By.ID, "btnSubmitNewRequest").click()
    time.sleep(0.3)

    # Handle alert
    try:
        alert = driver.switch_to.alert
        alert.accept()
    except Exception:
        pass

    # 4. Verify new item in list
    body_text = driver.find_element(By.TAG_NAME, "body").text
    assert "Add EV Charging Station to Map" in body_text

    # 5. Verify Total Requests incremented to 157
    total_kpi = driver.find_element(By.ID, "kpiTotalRequests")
    assert total_kpi.text == "157"

def test_request_detail_modal_and_timeline(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-requests.html")
    time.sleep(0.3)

    # 1. Click on row 2 (Navigation to Food Court)
    driver.find_element(By.ID, "req-row-2").click()
    time.sleep(0.3)

    modal = driver.find_element(By.ID, "requestDetailModal")
    assert modal.is_displayed()
    assert "Navigation to Food Court" in modal.text
    assert "Request Timeline" in modal.text
    assert "Under Review" in modal.text

    # 2. Close modal
    driver.find_element(By.XPATH, "//button[contains(., 'Close')]").click()
    time.sleep(0.3)
    assert not modal.is_displayed()

def test_strict_client_admin_requests_boundaries(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-requests.html")
    page_text = driver.page_source.lower()

    # Boundaries: No Company technical / code deployment tools
    assert "code deployment" not in page_text
    assert "release pipeline" not in page_text
    assert "engineering task board" not in page_text
    assert "assign developer" not in page_text
    assert "sla management engine" not in page_text
    assert "database migration" not in page_text
    assert "git commit" not in page_text
