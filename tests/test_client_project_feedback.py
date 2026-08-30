import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def test_client_project_feedback_page_loads(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-feedback.html")
    assert "Feedback" in driver.title

    # 1. Active Sidebar Item is Projects
    active_nav = driver.find_element(By.CSS_SELECTOR, ".sidebar-nav .nav-item.active")
    assert "Projects" in active_nav.text

    # 2. Strict 8 Sidebar items check
    nav_items = driver.find_elements(By.CSS_SELECTOR, ".sidebar-nav .nav-item")
    assert len(nav_items) == 8

    # 3. Breadcrumb & Project Name in Header
    page_text = driver.page_source
    assert "Phoenix Mall Project" in page_text
    assert "Feedback" in page_text
    assert "Active" in page_text

    # 4. Project subnav active tab is Feedback
    active_tab = driver.find_element(By.CSS_SELECTOR, ".project-subnav-tabs .project-subnav-tab.active")
    assert "Feedback" in active_tab.text

def test_feedback_kpi_summary(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-feedback.html")
    time.sleep(0.3)
    body_text = driver.find_element(By.TAG_NAME, "body").text

    # 6 KPI summary cards
    assert "Total Feedback" in body_text
    assert "1,245" in body_text

    assert "Average Rating" in body_text
    assert "4.2" in body_text

    assert "Positive Feedback" in body_text
    assert "887" in body_text

    assert "Negative Feedback" in body_text
    assert "132" in body_text

    assert "Avg. Response Time" in body_text
    assert "4h 32m" in body_text

    assert "Resolved Feedback" in body_text
    assert "1,113" in body_text

def test_feedback_visualizations_and_tables(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-feedback.html")
    time.sleep(0.3)
    body_text = driver.find_element(By.TAG_NAME, "body").text

    # Trend & Category
    assert "Feedback Trend" in body_text
    assert "Feedback by Category" in body_text
    assert "Navigation & Map" in body_text
    assert "Content & Information" in body_text
    assert "Cleanliness" in body_text

    # Rating distribution
    assert "Rating Distribution" in body_text
    assert "5 Stars" in body_text
    assert "4 Stars" in body_text
    assert "1 Star" in body_text

    # Recent Feedback Table
    rows = driver.find_elements(By.CSS_SELECTOR, "#recentFeedbackTable tbody tr")
    assert len(rows) == 5
    assert "Sarah Johnson" in body_text
    assert "Amit Verma" in body_text
    assert "Priya Sharma" in body_text

    # Top Feedback Themes
    assert "Top Feedback Themes" in body_text
    assert "Navigation Difficult" in body_text
    assert "More Offers Needed" in body_text

def test_respond_modal_and_status_update(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-feedback.html")
    time.sleep(0.3)

    # 1. Click respond on Priya Sharma row (id 3)
    action_btn = driver.find_element(By.CSS_SELECTOR, "#row-fb-3 button")
    action_btn.click()
    time.sleep(0.3)

    modal = driver.find_element(By.ID, "respondFeedbackModal")
    assert modal.is_displayed()
    assert "Priya Sharma" in modal.text

    # 2. Select Resolved status and submit
    status_select = Select(driver.find_element(By.ID, "respondStatusSelect"))
    status_select.select_by_value("Resolved")

    submit_btn = driver.find_element(By.ID, "btnSubmitFeedbackResponse")
    submit_btn.click()
    time.sleep(0.3)

    # Handle alert
    try:
        alert = driver.switch_to.alert
        alert.accept()
    except Exception:
        pass

    # 3. Verify status updated in table
    status_el = driver.find_element(By.ID, "status-fb-3")
    assert status_el.text == "Resolved"

def test_strict_client_admin_feedback_boundaries(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-feedback.html")
    page_text = driver.page_source.lower()

    # Boundaries: No Company technical debugging or form builder controls
    assert "feedback form builder" not in page_text
    assert "configure feedback questions" not in page_text
    assert "configure feedback placement" not in page_text
    assert "session replay" not in page_text
    assert "gate-by-gate" not in page_text
    assert "tracking configuration" not in page_text
    assert "device logs" not in page_text
