from selenium.webdriver.common.by import By

def test_company_dashboard_loads(driver, base_url):
    driver.get(f"{base_url}/dashboard.html")
    assert "Company Dashboard" in driver.title or "Platform" in driver.title
    
    # 1. Verify Top Header Title
    header_title = driver.find_element(By.TAG_NAME, "h1").text
    assert "Company Dashboard" in header_title

    # 2. Verify 6 KPI Cards
    kpi_cards = driver.find_elements(By.CLASS_NAME, "kpi-card")
    assert len(kpi_cards) == 6
    
    kpi_titles = [c.find_element(By.CLASS_NAME, "kpi-title").text for c in kpi_cards]
    assert "Total Clients" in kpi_titles
    assert "Active Projects" in kpi_titles
    assert "Total Kiosks" in kpi_titles
    assert "Pending Requests" in kpi_titles
    assert "Pending Releases" in kpi_titles
    assert "System Health" in kpi_titles

def test_company_dashboard_panels(driver, base_url):
    driver.get(f"{base_url}/dashboard.html")
    
    # Verify Recent Activity
    assert "Recent Activity" in driver.page_source
    assert "Phoenix Mall" in driver.page_source

    # Verify Platform Health Services
    assert "API Service" in driver.page_source
    assert "Storage (S3)" in driver.page_source
    assert "CDN (CloudFront)" in driver.page_source

    # Verify Kiosk Connectivity
    assert "156" in driver.page_source
    assert "Online" in driver.page_source
    assert "Offline" in driver.page_source

    # Verify Top Performing Ads Table
    assert "Top Performing Advertisements" in driver.page_source
    assert "Adidas Festival Offer" in driver.page_source

    # Verify Quick Actions Grid
    assert "Onboard Client" in driver.page_source
    assert "Create Project" in driver.page_source
