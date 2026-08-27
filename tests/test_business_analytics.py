import time
from selenium.webdriver.common.by import By

def test_analytics_page_loads(driver, base_url):
    driver.get(f"{base_url}/analytics.html")
    assert "Analytics" in driver.title

    # 1. Verify Top Header & Active Sidebar Item
    assert "Analytics" in driver.page_source
    active_nav = driver.find_element(By.CSS_SELECTOR, ".sidebar-nav .nav-item.active")
    assert "Analytics" in active_nav.text

    # 2. Verify 6 KPI summary boxes
    kpi_boxes = driver.find_elements(By.CLASS_NAME, "kpi-stat-box")
    assert len(kpi_boxes) >= 6
    page_text = driver.page_source
    assert "Total Sessions" in page_text
    assert "Unique Visitors" in page_text
    assert "Total Interactions" in page_text
    assert "Avg. Session Time" in page_text
    assert "Screens / Session" in page_text
    assert "Bounce Rate" in page_text

def test_analytics_sessions_and_top_screens(driver, base_url):
    driver.get(f"{base_url}/analytics.html")
    time.sleep(0.3)

    page_text = driver.page_source
    # Verify Sessions by Project Breakdown
    assert "Sessions by Project" in page_text
    assert "Phoenix Mall Project" in page_text
    assert "Orion Mall Project" in page_text
    assert "Skyline Mall Project" in page_text

    # Verify Top Screens
    assert "Top Screens by Views" in page_text
    assert "Search" in page_text
    assert "Map" in page_text

def test_visitor_journey_gate_explorer_modal(driver, base_url):
    driver.get(f"{base_url}/analytics.html")
    time.sleep(0.3)

    # Click View Detailed Report Quick Action
    qa_btn = driver.find_element(By.ID, "qaViewDetailedReport")
    qa_btn.click()
    time.sleep(0.3)

    # Verify modal is open and shows journey gates
    modal = driver.find_element(By.ID, "journeyModal")
    assert modal.is_displayed()
    assert "#A82F91" in modal.text
    assert "Gate 1: Home Screen Viewed" in modal.text
    assert "Gate 2: Ad Section Clicked" in modal.text
    assert "Gate 5: Navigation Requested" in modal.text
    assert "Gate 6: QR / WhatsApp Share Requested" in modal.text
    assert "Gate 7: Feedback Submitted" in modal.text

def test_ad_campaign_intelligence_modal(driver, base_url):
    driver.get(f"{base_url}/analytics.html")
    time.sleep(0.3)

    # Trigger ad modal via script or clickable element
    driver.execute_script("openAdCampaignModal('Adidas Summer Offer')")
    time.sleep(0.3)

    modal = driver.find_element(By.ID, "adCampaignModal")
    assert modal.is_displayed()
    assert "Adidas Summer Offer" in modal.text
    assert "48,240" in modal.text
    assert "Summer Discount" in modal.text
    assert "New Launch" in modal.text
    assert "Shop Now" in modal.text

def test_store_engagement_analytics_modal(driver, base_url):
    driver.get(f"{base_url}/analytics.html")
    time.sleep(0.3)

    # Trigger store modal
    driver.execute_script("openStoreDetailsModal('Adidas Store')")
    time.sleep(0.3)

    modal = driver.find_element(By.ID, "storeDetailsModal")
    assert modal.is_displayed()
    assert "Store Engagement Analytics" in modal.text
    assert "Direct Searches" in modal.text
    assert "Navigation Requests" in modal.text
    assert "Physical Visit Distinction" in modal.text

def test_strict_business_boundaries_analytics(driver, base_url):
    driver.get(f"{base_url}/analytics.html")
    buttons = driver.find_elements(By.TAG_NAME, "button")
    links = driver.find_elements(By.TAG_NAME, "a")
    interactive_texts = [b.text.strip().lower() for b in buttons + links if b.text]

    # Boundaries: No template or theme creation
    assert "create template" not in interactive_texts
    assert "create theme" not in interactive_texts
