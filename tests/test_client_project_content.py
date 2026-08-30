import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def test_client_project_content_page_loads(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-content.html")
    assert "Content" in driver.title

    # 1. Active Sidebar Item is Projects
    active_nav = driver.find_element(By.CSS_SELECTOR, ".sidebar-nav .nav-item.active")
    assert "Projects" in active_nav.text

    # 2. Strict 8 Sidebar items check
    nav_items = driver.find_elements(By.CSS_SELECTOR, ".sidebar-nav .nav-item")
    assert len(nav_items) == 8

    # 3. Breadcrumb & Project Name in Header
    page_text = driver.page_source
    assert "Phoenix Mall Project" in page_text
    assert "Content" in page_text
    assert "Active" in page_text

    # 4. Project subnav active tab is Content
    active_tab = driver.find_element(By.CSS_SELECTOR, ".project-subnav-tabs .project-subnav-tab.active")
    assert "Content" in active_tab.text

def test_content_category_switching(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-content.html")
    time.sleep(0.3)
    body_text = driver.find_element(By.TAG_NAME, "body").text

    # Default Stores & Brands list
    assert "Adidas" in body_text
    assert "Lifestyle" in body_text
    assert "Zara" in body_text
    assert "Reliance Digital" in body_text

    # Switch to Amenities
    driver.find_element(By.ID, "catTabAmenities").click()
    time.sleep(0.3)
    body_text = driver.find_element(By.TAG_NAME, "body").text
    assert "Restrooms & Washrooms" in body_text
    assert "Basement Parking" in body_text

    # Switch to Offers & Promotions
    driver.find_element(By.ID, "catTabOffers").click()
    time.sleep(0.3)
    body_text = driver.find_element(By.TAG_NAME, "body").text
    assert "Summer End of Season Sale" in body_text

    # Switch to Events
    driver.find_element(By.ID, "catTabEvents").click()
    time.sleep(0.3)
    body_text = driver.find_element(By.TAG_NAME, "body").text
    assert "Live Acoustic Weekend" in body_text

    # Switch to Movies
    driver.find_element(By.ID, "catTabMovies").click()
    time.sleep(0.3)
    body_text = driver.find_element(By.TAG_NAME, "body").text
    assert "Avengers: Secret Wars" in body_text

    # Switch to General Information
    driver.find_element(By.ID, "catTabInfo").click()
    time.sleep(0.3)
    body_text = driver.find_element(By.TAG_NAME, "body").text
    assert "Mall Operating Hours & Policies" in body_text

def test_store_details_panel_and_edit_flow(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-content.html")
    time.sleep(0.3)

    # 1. Verify Adidas Details initially visible
    body_text = driver.find_element(By.TAG_NAME, "body").text
    assert "Adidas" in body_text
    assert "ST-0001" in body_text
    assert "Ground Floor, Near Entry Gate 2" in body_text

    # 2. Click Edit Store
    driver.find_element(By.ID, "btnEditStore").click()
    time.sleep(0.3)

    modal = driver.find_element(By.ID, "editContentModal")
    assert modal.is_displayed()

    # 3. Update Contact
    contact_input = driver.find_element(By.ID, "editItemContactInput")
    contact_input.clear()
    contact_input.send_keys("+91 99999 88888")

    # 4. Save Changes
    driver.find_element(By.ID, "btnSaveContentEdit").click()
    time.sleep(0.3)

    # Handle alert
    try:
        alert = driver.switch_to.alert
        alert.accept()
    except Exception:
        pass

    # 5. Verify updated detail in right panel
    updated_text = driver.find_element(By.ID, "detailContact").text
    assert "+91 99999 88888" in updated_text

def test_view_on_kiosk_modal(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-content.html")
    time.sleep(0.3)

    # Click View on Kiosk
    driver.find_element(By.XPATH, "//span[contains(., 'View on Kiosk')]").click()
    time.sleep(0.3)

    modal = driver.find_element(By.ID, "viewOnKioskModal")
    assert modal.is_displayed()
    assert "Kiosk Display 01 · Portrait 4K" in modal.text
    assert "Adidas" in modal.text

    # Close modal
    driver.find_element(By.XPATH, "//button[contains(., 'Exit Kiosk Preview')]").click()
    time.sleep(0.3)
    assert not modal.is_displayed()

def test_add_new_store_routes_to_company_requests(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-content.html")
    time.sleep(0.3)

    # Click + Add New Store
    driver.find_element(By.ID, "btnAddCategoryItem").click()
    time.sleep(0.3)

    modal = driver.find_element(By.ID, "addContentModal")
    assert modal.is_displayed()
    assert "Company Admin" in modal.text

    # Fill and submit
    driver.find_element(By.ID, "newStoreNameInput").send_keys("Uniqlo Store")
    driver.find_element(By.ID, "btnSubmitNewStoreReq").click()
    time.sleep(0.3)

    # Handle alert
    try:
        alert = driver.switch_to.alert
        alert.accept()
    except Exception:
        pass

    # Should redirect to requests.html
    time.sleep(0.5)
    assert "project-requests.html" in driver.current_url

def test_strict_content_boundaries(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-content.html")
    page_text = driver.page_source.lower()

    # Boundaries: No content analytics, no pie charts, no map path drawing tools
    assert "visitor analytics" not in page_text
    assert "content engagement rate" not in page_text
    assert "pie chart" not in page_text
    assert "draw route" not in page_text
    assert "screen builder" not in page_text
