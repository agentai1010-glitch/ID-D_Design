import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def test_client_project_analytics_page_loads(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-analytics.html")
    assert "Analytics" in driver.title

    # 1. Active Sidebar Item is Projects
    active_nav = driver.find_element(By.CSS_SELECTOR, ".sidebar-nav .nav-item.active")
    assert "Projects" in active_nav.text

    # 2. Strict 8 Sidebar items check
    nav_items = driver.find_elements(By.CSS_SELECTOR, ".sidebar-nav .nav-item")
    assert len(nav_items) == 8

    # 3. Breadcrumb & Project Name in Header
    page_text = driver.page_source
    assert "Phoenix Mall Project" in page_text
    assert "Analytics" in page_text
    assert "Active" in page_text

    # 4. Project subnav active tab is Analytics
    active_tab = driver.find_element(By.CSS_SELECTOR, ".project-subnav-tabs .project-subnav-tab.active")
    assert "Analytics" in active_tab.text

def test_analytics_kpi_summary(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-analytics.html")
    time.sleep(0.3)
    page_text = driver.page_source

    # 6 KPI summary cards
    assert "Total Visitors" in page_text
    assert "54,320" in page_text

    assert "Total Interactions" in page_text
    assert "132,450" in page_text

    assert "Avg. Session Time" in page_text
    assert "2m 48s" in page_text

    assert "Unique Visitors" in page_text
    assert "38,750" in page_text

    assert "New Visitors" in page_text
    assert "18,620" in page_text

    assert "Satisfaction Score" in page_text
    assert "4.2" in page_text

def test_visualizations_and_breakdowns(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-analytics.html")
    time.sleep(0.3)
    body_text = driver.find_element(By.TAG_NAME, "body").text

    # Charts and Heatmap
    assert "Visitor Trend" in body_text
    assert "Visitors by Time of Day" in body_text

    # Top Sections Viewed
    assert "Top Sections Viewed" in body_text
    assert "Directory" in body_text
    assert "Offers & Deals" in body_text
    assert "Events" in body_text
    assert "Food & Dining" in body_text
    assert "Amenities" in body_text
    assert "Navigation" in body_text

    # Top Content
    assert "Top Content" in body_text
    assert "Adidas Store" in body_text
    assert "Summer Sale Offer" in body_text
    assert "Music Night Event" in body_text
    assert "PVR Cinemas" in body_text

    # Top Campaigns
    assert "Top Campaigns" in body_text
    assert "Summer Sale 2025" in body_text
    assert "Festive Offers" in body_text
    assert "Food Court Specials" in body_text

    # Device Usage & Visitor Types
    assert "Device Usage" in body_text
    assert "Visitors by Visitor Type" in body_text

def test_engagement_summary_and_date_filtering(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-analytics.html")
    time.sleep(0.3)
    page_text = driver.page_source

    # 5 Engagement metrics
    assert "Engagement Summary" in page_text
    assert "Total Touches" in page_text
    assert "98,320" in page_text

    assert "Screen Views" in page_text
    assert "78,450" in page_text

    assert "Searches" in page_text
    assert "12,860" in page_text

    assert "Map Views" in page_text
    assert "8,920" in page_text

    assert "Take Me There" in page_text
    assert "6,420" in page_text

    # Test Date Range dropdown update
    selector = Select(driver.find_element(By.ID, "dateRangeSelector"))
    selector.select_by_value("last-30-days")
    time.sleep(0.3)

    visitors_el = driver.find_element(By.ID, "kpiTotalVisitors")
    assert visitors_el.text == "218,450"

def test_strict_client_admin_analytics_boundaries(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-analytics.html")
    page_text = driver.page_source.lower()

    # Boundaries: No Company technical debugging or tracking configuration
    assert "raw event logs" not in page_text
    assert "event stream" not in page_text
    assert "session replay" not in page_text
    assert "journey debugging" not in page_text
    assert "configure tracking" not in page_text
    assert "tracking configuration" not in page_text
    assert "gate analysis" not in page_text
