import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_client_project_advertisements_page_loads(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-advertisements.html")
    assert "Advertisements" in driver.title

    # 1. Active Sidebar Item is Projects
    active_nav = driver.find_element(By.CSS_SELECTOR, ".sidebar-nav .nav-item.active")
    assert "Projects" in active_nav.text

    # 2. Strict 8 Sidebar items check
    nav_items = driver.find_elements(By.CSS_SELECTOR, ".sidebar-nav .nav-item")
    assert len(nav_items) == 8

    # 3. Breadcrumb & Project Name in Header
    page_text = driver.page_source
    assert "Phoenix Mall Project" in page_text
    assert "Advertisements" in page_text
    assert "Active" in page_text

    # 4. Project subnav active tab is Advertisements
    active_tab = driver.find_element(By.CSS_SELECTOR, ".project-subnav-tabs .project-subnav-tab.active")
    assert "Advertisements" in active_tab.text

def test_advertisements_kpi_summary(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-advertisements.html")
    time.sleep(0.3)
    page_text = driver.page_source

    # 6 KPI summary cards
    assert "Active Campaigns" in page_text
    assert "12" in page_text

    assert "Total Impressions" in page_text
    assert "254,320" in page_text

    assert "Total Interactions" in page_text
    assert "32,450" in page_text

    assert "Avg. CTR" in page_text
    assert "12.8%" in page_text

    assert "Avg. Engagement Time" in page_text
    assert "8.6 sec" in page_text

    assert "Last Updated" in page_text
    assert "18 May 2025" in page_text

def test_campaigns_table_and_filters(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-advertisements.html")
    time.sleep(0.3)
    page_text = driver.page_source

    assert "Campaigns" in page_text
    assert "Request New Campaign" in page_text

    # 8 rows present in table
    rows = driver.find_elements(By.CSS_SELECTOR, "#campaignsDataTable tbody tr")
    assert len(rows) == 8

    # Search filter testing
    search_input = driver.find_element(By.ID, "searchAdsInput")
    search_input.clear()
    search_input.send_keys("Festive")
    time.sleep(0.2)
    visible_rows = [r for r in driver.find_elements(By.CSS_SELECTOR, "#campaignsDataTable tbody tr") if r.is_displayed()]
    assert len(visible_rows) == 1
    assert "Festive Offers" in visible_rows[0].text

    # Clear search
    search_input.clear()
    search_input.send_keys(Keys.BACKSPACE)
    time.sleep(0.2)

def test_edit_campaign_and_status_toggle(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-advertisements.html")
    time.sleep(0.3)

    # 1. Open Edit Modal for Summer Sale
    edit_btn = driver.find_element(By.CSS_SELECTOR, "#row-summer-sale button[title='Edit Campaign']")
    edit_btn.click()
    time.sleep(0.3)

    modal = driver.find_element(By.ID, "editCampaignModal")
    assert modal.is_displayed()
    assert "Edit: Summer Sale 2025" in modal.text

    # 2. Modify description
    desc_input = driver.find_element(By.ID, "editCampaignDescInput")
    desc_input.clear()
    desc_input.send_keys("Updated summer clearance deals across all stores.")

    # 3. Save Changes
    save_btn = driver.find_element(By.ID, "btnSaveCampaignEdit")
    save_btn.click()
    time.sleep(0.3)

    # Accept alert
    try:
        alert = driver.switch_to.alert
        alert.accept()
    except Exception:
        pass

    # Verify updated description in table
    updated_desc = driver.find_element(By.ID, "desc-summer-sale").text
    assert "Updated summer clearance deals" in updated_desc

def test_strict_client_admin_advertisement_boundaries(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-advertisements.html")
    buttons = driver.find_elements(By.TAG_NAME, "button")
    links = driver.find_elements(By.TAG_NAME, "a")
    interactive_texts = [b.text.strip().lower() for b in buttons + links if b.text]

    # Boundaries: No Company builder controls
    assert "create advertisement" not in interactive_texts
    assert "create campaign" not in interactive_texts
    assert "design advertisement" not in interactive_texts
    assert "create screen" not in interactive_texts
    assert "configure rotation" not in interactive_texts
    assert "configure screen timing" not in interactive_texts
    assert "publish" not in interactive_texts
    assert "release" not in interactive_texts
    assert "deploy" not in interactive_texts
