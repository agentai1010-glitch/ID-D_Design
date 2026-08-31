import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="module")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def base_url():
    return "http://localhost:8000"

def test_feedback_page_loads_and_header(driver, base_url):
    driver.get(f"{base_url}/kiosk/feedback.html")
    time.sleep(0.5)

    # 1. Title & Branding
    assert "Feedback, Help & Kiosk Session" in driver.title
    assert "GRAND" in driver.page_source
    assert "METRO MALL" in driver.page_source

    # 2. Back button
    back_btn = driver.find_element(By.ID, "btnHeaderBack")
    assert back_btn.is_displayed()
    assert "Back" in back_btn.text

    # 3. Weather & Live Time
    weather = driver.find_element(By.ID, "headerWeather")
    assert "28°C" in weather.text
    clock = driver.find_element(By.ID, "kioskLiveTime")
    assert clock.is_displayed()

    # 4. Heading
    assert "FEEDBACK" in driver.page_source and "KIOSK SESSION" in driver.page_source

def test_five_primary_options_navigation_cards(driver, base_url):
    driver.get(f"{base_url}/kiosk/feedback.html")
    time.sleep(0.5)

    tab_fb = driver.find_element(By.ID, "tabFeedback")
    assert tab_fb.is_displayed()
    assert "Feedback" in tab_fb.text

    tab_help = driver.find_element(By.ID, "tabGetHelp")
    assert "Get Help" in tab_help.text

    tab_issue = driver.find_element(By.ID, "tabReportIssue")
    assert "Report an Issue" in tab_issue.text

    tab_enq = driver.find_element(By.ID, "tabGeneralEnquiry")
    assert "General Enquiry" in tab_enq.text

    tab_session = driver.find_element(By.ID, "tabSessionComplete")
    assert "Session Complete" in tab_session.text

def test_feedback_star_rating_and_submission(driver, base_url):
    driver.get(f"{base_url}/kiosk/feedback.html")
    time.sleep(0.3)

    # Star rating items
    stars = driver.find_elements(By.CSS_SELECTOR, ".star-rate-item")
    assert len(stars) == 5

    # Click 4th star (Very Good)
    stars[3].click()
    time.sleep(0.2)

    # Write comment
    inp = driver.find_element(By.ID, "feedbackCommentInput")
    inp.send_keys("The mall experience was fantastic and very clean!")

    # Submit
    driver.find_element(By.ID, "btnSubmitFeedback").click()
    time.sleep(0.3)

    modal = driver.find_element(By.ID, "feedbackThanksModal")
    assert modal.is_displayed()
    assert "Thank You for Your Feedback!" in modal.text

    driver.find_element(By.XPATH, "//div[@id='feedbackThanksModal']//button[text()='Done']").click()
    time.sleep(0.3)
    assert not modal.is_displayed()

def test_immediate_assistance_and_contacts(driver, base_url):
    driver.get(f"{base_url}/kiosk/feedback.html")
    time.sleep(0.3)

    # Connect Now
    driver.find_element(By.ID, "btnConnectConcierge").click()
    time.sleep(0.3)

    modal = driver.find_element(By.ID, "immediateHelpModal")
    assert modal.is_displayed()
    assert "Guest Concierge Connected" in modal.text

    driver.find_element(By.XPATH, "//div[@id='immediateHelpModal']//button[text()='Dismiss']").click()
    time.sleep(0.3)
    assert not modal.is_displayed()

    # Contacts
    assert "Call Us" in driver.page_source
    assert "+91 123 456 7890" in driver.page_source
    assert "help@grandmetromall.com" in driver.page_source
    assert "Visit Guest Services Desk" in driver.page_source

def test_report_issue_and_general_enquiry_modals(driver, base_url):
    driver.get(f"{base_url}/kiosk/feedback.html")
    time.sleep(0.3)

    # 1. Report an Issue
    driver.find_element(By.ID, "tabReportIssue").click()
    time.sleep(0.3)

    issue_modal = driver.find_element(By.ID, "reportIssueModal")
    assert issue_modal.is_displayed()
    assert "Report an Issue" in issue_modal.text

    driver.find_element(By.ID, "issueNotesInput").send_keys("Screen touch responsiveness test.")
    driver.find_element(By.ID, "btnSubmitIssue").click()
    time.sleep(0.3)

    assert not issue_modal.is_displayed()
    thanks_modal = driver.find_element(By.ID, "feedbackThanksModal")
    assert thanks_modal.is_displayed()
    driver.find_element(By.XPATH, "//div[@id='feedbackThanksModal']//button[text()='Done']").click()
    time.sleep(0.3)

    # 2. General Enquiry
    driver.find_element(By.ID, "tabGeneralEnquiry").click()
    time.sleep(0.3)

    enq_modal = driver.find_element(By.ID, "generalEnquiryModal")
    assert enq_modal.is_displayed()
    assert "General Enquiry" in enq_modal.text

    driver.find_element(By.ID, "enquiryTextInput").send_keys("Where can I purchase mall gift cards?")
    driver.find_element(By.ID, "btnSubmitEnquiry").click()
    time.sleep(0.3)

    assert not enq_modal.is_displayed()
    driver.find_element(By.XPATH, "//div[@id='feedbackThanksModal']//button[text()='Done']").click()
    time.sleep(0.3)

def test_quick_help_topics_and_reassurance(driver, base_url):
    driver.get(f"{base_url}/kiosk/feedback.html")
    time.sleep(0.3)

    # Quick Help Topics
    assert "QUICK HELP TOPICS" in driver.page_source
    assert "How to Navigate the Mall" in driver.page_source
    assert "Parking Assistance" in driver.page_source
    assert "Lost" in driver.page_source and "Found" in driver.page_source
    assert "Wheelchair Assistance" in driver.page_source

    # Reassurance items
    assert "We're here to help" in driver.page_source
    assert "Safe" in driver.page_source and "Secure" in driver.page_source
    assert "Return to Home" in driver.page_source

def test_kiosk_session_countdown_and_end_session(driver, base_url):
    driver.get(f"{base_url}/kiosk/feedback.html")
    time.sleep(0.3)

    # Countdown text
    clock = driver.find_element(By.ID, "sessionCountdownDisplay")
    assert clock.is_displayed()
    assert ":" in clock.text

    # End Session Now
    driver.find_element(By.ID, "btnEndSessionNow").click()
    time.sleep(0.3)

    modal = driver.find_element(By.ID, "sessionDoneModal")
    assert modal.is_displayed()
    assert "Session Completed" in modal.text

    btn_home = driver.find_element(By.ID, "btnSessionReturnHome")
    assert btn_home.is_displayed()
    assert "Return to Home" in btn_home.text

def test_strict_kiosk_feedback_boundaries(driver, base_url):
    driver.get(f"{base_url}/kiosk/feedback.html")
    time.sleep(0.3)

    body_text = driver.find_element(By.TAG_NAME, "body").text.lower()
    assert "csat analytics dashboard" not in body_text
    assert "nps calculation chart" not in body_text
    assert "support ticket queue management" not in body_text
    assert "agent performance table" not in body_text
