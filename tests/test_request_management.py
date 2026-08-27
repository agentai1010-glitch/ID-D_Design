import time
from selenium.webdriver.common.by import By

def test_request_management_page_loads(driver, base_url):
    driver.get(f"{base_url}/requests.html")
    assert "Request Management" in driver.title or "Requests" in driver.title

    # 1. Verify Top Header & Active Sidebar Item
    assert "Requests" in driver.page_source
    active_nav = driver.find_element(By.CSS_SELECTOR, ".sidebar-nav .nav-item.active")
    assert "Requests" in active_nav.text

    # 2. Verify 5 KPI summary boxes
    kpi_boxes = driver.find_elements(By.CLASS_NAME, "kpi-stat-box")
    assert len(kpi_boxes) >= 5
    page_text = driver.page_source
    assert "Total Requests" in page_text
    assert "Pending Review" in page_text
    assert "In Progress" in page_text
    assert "Approved" in page_text
    assert "Rejected" in page_text

def test_request_table_and_selection(driver, base_url):
    driver.get(f"{base_url}/requests.html")
    time.sleep(0.3)

    # 1. Verify Prototype Rows
    page_text = driver.page_source
    assert "REQ-2025-0156" in page_text
    assert "Add New Retailer: Miniso" in page_text
    assert "Update Food Court Map" in page_text
    assert "Add Summer Sale Banner" in page_text
    assert "Enable WhatsApp QR Share" in page_text

    # 2. Select Row 2 (REQ-2025-0155)
    rows = driver.find_elements(By.CLASS_NAME, "request-row")
    assert len(rows) >= 7
    rows[1].click()
    time.sleep(0.3)

    # 3. Verify Selected Request Panel Updates
    sel_card = driver.find_element(By.ID, "selectedRequestCard")
    assert "REQ-2025-0155" in sel_card.text
    assert "Update Food Court Map" in sel_card.text
    assert "Orion Mall" in sel_card.text

def test_request_details_deep_modal(driver, base_url):
    driver.get(f"{base_url}/requests.html")
    time.sleep(0.3)

    # Click View Details Button
    btn_details = driver.find_element(By.ID, "btnViewDetails")
    btn_details.click()
    time.sleep(0.3)

    # Verify Details Modal
    modal = driver.find_element(By.ID, "requestDetailsModal")
    assert modal.is_displayed()
    assert "Existing State vs. Requested Change" in modal.text
    assert "Execution Workflow Routing & Dependencies" in modal.text
    assert "Experience Studio" in modal.text
    assert "Project Maps" in modal.text
    assert "Activity & Clarification Timeline" in modal.text

def test_review_decision_and_clarification_workflow(driver, base_url):
    driver.get(f"{base_url}/requests.html")
    time.sleep(0.3)

    # Click Review Request Button
    btn_review = driver.find_element(By.ID, "btnReviewRequest")
    btn_review.click()
    time.sleep(0.3)

    modal = driver.find_element(By.ID, "reviewDecisionModal")
    assert modal.is_displayed()
    assert "Company Request Decision" in modal.text

    # Switch to Request Clarification tab
    tab_clarify = driver.find_element(By.ID, "tabClarify")
    tab_clarify.click()
    time.sleep(0.2)
    clarify_form = driver.find_element(By.ID, "decisionClarifyForm")
    assert clarify_form.is_displayed()
    assert "Missing Information / Asset Required" in clarify_form.text

    # Switch to Approve tab
    tab_approve = driver.find_element(By.ID, "tabApprove")
    tab_approve.click()
    time.sleep(0.2)
    approve_form = driver.find_element(By.ID, "decisionApproveForm")
    assert approve_form.is_displayed()
    assert "Assign Team" in approve_form.text
    assert "Target Release" in approve_form.text

def test_client_guided_request_creation_simulator(driver, base_url):
    driver.get(f"{base_url}/requests.html")
    time.sleep(0.3)

    # Click Create New Request Quick Action
    qa_btn = driver.find_element(By.ID, "qaCreateNewRequest")
    qa_btn.click()
    time.sleep(0.3)

    modal = driver.find_element(By.ID, "clientCreateRequestModal")
    assert modal.is_displayed()
    assert "Create Structured Request" in modal.text
    assert "Request Category" in modal.text
    assert "Upload Attachments / Creative Assets" in modal.text

def test_strict_business_boundaries_requests(driver, base_url):
    driver.get(f"{base_url}/requests.html")
    buttons = driver.find_elements(By.TAG_NAME, "button")
    links = driver.find_elements(By.TAG_NAME, "a")
    interactive_texts = [b.text.strip().lower() for b in buttons + links if b.text]

    # Boundaries: No direct client-side template build tool inside requests
    assert "build template" not in interactive_texts
    assert "deploy directly to kiosk" not in interactive_texts
