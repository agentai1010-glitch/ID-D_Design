import time
from selenium.webdriver.common.by import By

def test_client_management_page_and_selection(driver, base_url):
    driver.get(f"{base_url}/clients.html")
    assert "Client Management" in driver.title
    
    # 1. Check 5 KPI Summary cards
    kpi_cards = driver.find_elements(By.CLASS_NAME, "kpi-card")
    assert len(kpi_cards) == 5

    # 2. Check Client Table exists with rows
    table_rows = driver.find_elements(By.CSS_SELECTOR, "#clientsDataTable tbody tr")
    assert len(table_rows) >= 7

    # 3. Test interactive selection of a client row (e.g. Orion Mall)
    orion_row = None
    for r in table_rows:
        if "Orion Mall" in r.text:
            orion_row = r
            break
    assert orion_row is not None
    orion_row.click()
    time.sleep(0.3)

    # Check right preview card updated to Orion Mall
    preview_title = driver.find_element(By.ID, "selClientTitle").text
    assert preview_title == "Orion Mall"

def test_client_detail_navigation_and_tabs(driver, base_url):
    driver.get(f"{base_url}/clients.html")
    
    # Click "View Client Details" button
    view_details_btn = driver.find_element(By.LINK_TEXT, "View Client Details")
    view_details_btn.click()
    time.sleep(0.5)

    assert "client-detail.html" in driver.current_url
    assert "Phoenix Mall" in driver.page_source

    # Click through tabs
    tab_btns = driver.find_elements(By.CLASS_NAME, "detail-tab-btn")
    assert len(tab_btns) >= 5

    # Switch to Organization Info tab
    for btn in tab_btns:
        if "Organization Info" in btn.text:
            btn.click()
            break
    time.sleep(0.3)
    assert "The Phoenix Mills Limited" in driver.page_source

    # Switch to Users & Access tab
    for btn in tab_btns:
        if "Users & Access" in btn.text:
            btn.click()
            break
    time.sleep(0.3)
    assert "admin@phoenixmall.com" in driver.page_source

def test_onboard_new_client_navigation(driver, base_url):
    driver.get(f"{base_url}/clients.html")
    
    onboard_btn = driver.find_element(By.LINK_TEXT, "Onboard New Client")
    onboard_btn.click()
    time.sleep(0.5)

    assert "onboard-client.html" in driver.current_url
