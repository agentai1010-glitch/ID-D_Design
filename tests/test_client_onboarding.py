import time
from selenium.webdriver.common.by import By

def test_client_onboarding_page_loads(driver, base_url):
    driver.get(f"{base_url}/onboard-client.html")
    assert "Client Onboarding" in driver.title or "Kiosk Platform" in driver.title
    
    # Verify header and breadcrumb
    assert "Client Onboarding" in driver.page_source
    assert "New Client" in driver.page_source
    
    # Verify Active sidebar
    active_nav = driver.find_element(By.CSS_SELECTOR, ".sidebar-nav .nav-item.active")
    assert "Onboarding" in active_nav.text

    # Verify 6 Stepper nodes present
    stepper_nodes = driver.find_elements(By.CLASS_NAME, "stepper-node")
    assert len(stepper_nodes) == 6

    # Verify Initial Progress Donut shows 16% (Step 1 of 6)
    progress_text = driver.find_element(By.ID, "donutProgressText").text
    assert "16%" in progress_text

def test_onboarding_complete_six_step_journey(driver, base_url):
    driver.get(f"{base_url}/onboard-client.html")
    time.sleep(0.3)

    # -------------------------------------------------------------
    # Step 1: Organization Information
    # -------------------------------------------------------------
    org_name = driver.find_element(By.ID, "orgNameInput")
    org_name.clear()
    org_name.send_keys("Phoenix Mills Ltd.")

    org_brand = driver.find_element(By.ID, "orgBrandInput")
    org_brand.clear()
    org_brand.send_keys("Phoenix Mall")

    # Click Save & Continue from Step 1
    step1_btn = driver.find_element(By.XPATH, "//button[contains(., 'Save & Continue')]")
    step1_btn.click()
    time.sleep(0.4)

    # -------------------------------------------------------------
    # Step 2: Client Admin Setup
    # -------------------------------------------------------------
    assert driver.find_element(By.ID, "stepPane2").is_displayed()
    progress_text = driver.find_element(By.ID, "donutProgressText").text
    assert "33%" in progress_text

    admin_name = driver.find_element(By.ID, "adminNameInput")
    admin_name.clear()
    admin_name.send_keys("Rahul Mehta")

    admin_email = driver.find_element(By.ID, "adminEmailInput")
    admin_email.clear()
    admin_email.send_keys("admin@phoenixmall.com")

    # Click Save & Continue from Step 2
    step2_btns = driver.find_elements(By.XPATH, "//button[contains(., 'Save & Continue')]")
    for btn in step2_btns:
        if btn.is_displayed():
            btn.click()
            break
    time.sleep(0.4)

    # -------------------------------------------------------------
    # Step 3: Template Assignment
    # -------------------------------------------------------------
    assert driver.find_element(By.ID, "stepPane3").is_displayed()
    progress_text = driver.find_element(By.ID, "donutProgressText").text
    assert "50%" in progress_text

    # Verify Approved Template "Mall / Indoor Venue" is present
    assert "Mall / Indoor Venue" in driver.page_source
    # Verify business rule: NO "Create Template" button exists
    assert "Create Template" not in driver.page_source
    assert "Create New Template" not in driver.page_source

    # Click Save & Continue from Step 3
    step3_btns = driver.find_elements(By.XPATH, "//button[contains(., 'Save & Continue')]")
    for btn in step3_btns:
        if btn.is_displayed():
            btn.click()
            break
    time.sleep(0.4)

    # -------------------------------------------------------------
    # Step 4: Theme Assignment
    # -------------------------------------------------------------
    assert driver.find_element(By.ID, "stepPane4").is_displayed()
    progress_text = driver.find_element(By.ID, "donutProgressText").text
    assert "66%" in progress_text

    # Verify approved themes
    assert "Default Mall Luxury" in driver.page_source
    assert "Diwali Festive 2024" in driver.page_source
    # Verify business rule: NO "Create Theme" button exists
    assert "Create Theme" not in driver.page_source

    # Click Save & Continue from Step 4
    step4_btns = driver.find_elements(By.XPATH, "//button[contains(., 'Save & Continue')]")
    for btn in step4_btns:
        if btn.is_displayed():
            btn.click()
            break
    time.sleep(0.4)

    # -------------------------------------------------------------
    # Step 5: Initial Project Setup
    # -------------------------------------------------------------
    assert driver.find_element(By.ID, "stepPane5").is_displayed()
    progress_text = driver.find_element(By.ID, "donutProgressText").text
    assert "83%" in progress_text

    proj_name = driver.find_element(By.ID, "projNameInput")
    assert proj_name.get_attribute("value") == "Phoenix Mall"

    # Click Save & Continue from Step 5
    step5_btns = driver.find_elements(By.XPATH, "//button[contains(., 'Save & Continue')]")
    for btn in step5_btns:
        if btn.is_displayed():
            btn.click()
            break
    time.sleep(0.4)

    # -------------------------------------------------------------
    # Step 6: Review & Complete
    # -------------------------------------------------------------
    assert driver.find_element(By.ID, "stepPane6").is_displayed()
    progress_text = driver.find_element(By.ID, "donutProgressText").text
    assert "100%" in progress_text

    # Verify populated review details
    assert driver.find_element(By.ID, "revOrgName").text == "Phoenix Mills Ltd."
    assert driver.find_element(By.ID, "revOrgBrand").text == "Phoenix Mall"
    assert driver.find_element(By.ID, "revAdminName").text == "Rahul Mehta"
    assert driver.find_element(By.ID, "revAdminEmail").text == "admin@phoenixmall.com"
    assert driver.find_element(By.ID, "revProjName").text == "Phoenix Mall"

    # Click Complete Onboarding
    complete_btn = driver.find_element(By.ID, "btnCompleteOnboarding")
    complete_btn.click()
    time.sleep(0.5)

    # Verify Success Modal
    success_modal = driver.find_element(By.ID, "onboardSuccessModal")
    assert success_modal.is_displayed()
    assert "Client Successfully Onboarded" in success_modal.text
    assert "Phoenix Mills Ltd." in success_modal.text

def test_step_back_navigation_preserves_state(driver, base_url):
    driver.get(f"{base_url}/onboard-client.html")
    time.sleep(0.3)

    # Modify Organization Name on Step 1
    org_name = driver.find_element(By.ID, "orgNameInput")
    org_name.clear()
    org_name.send_keys("Orion Commercial Corp.")

    # Move to Step 2
    step1_btn = driver.find_element(By.XPATH, "//button[contains(., 'Save & Continue')]")
    step1_btn.click()
    time.sleep(0.4)
    assert driver.find_element(By.ID, "stepPane2").is_displayed()

    # Click Back button on Step 2
    back_btn = driver.find_element(By.XPATH, "//div[@id='stepPane2']//button[contains(., 'Back')]")
    back_btn.click()
    time.sleep(0.4)

    # Verify we are back on Step 1 and the entered state is preserved
    assert driver.find_element(By.ID, "stepPane1").is_displayed()
    assert driver.find_element(By.ID, "orgNameInput").get_attribute("value") == "Orion Commercial Corp."
