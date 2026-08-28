import time
from selenium.webdriver.common.by import By

def test_client_project_experience_loads(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-experience.html")
    assert "Experience" in driver.title

    # 1. Active Sidebar Item is Projects
    active_nav = driver.find_element(By.CSS_SELECTOR, ".sidebar-nav .nav-item.active")
    assert "Projects" in active_nav.text

    # 2. Strict 8 Sidebar items check
    nav_items = driver.find_elements(By.CSS_SELECTOR, ".sidebar-nav .nav-item")
    assert len(nav_items) == 8

    # 3. Breadcrumb & Project Name in Header
    page_text = driver.page_source
    assert "Phoenix Mall Project" in page_text
    assert "Experience" in page_text
    assert "Active" in page_text

    # 4. Project subnav active tab is Experience
    active_tab = driver.find_element(By.CSS_SELECTOR, ".project-subnav-tabs .project-subnav-tab.active")
    assert "Experience" in active_tab.text

def test_experience_status_summary_cards(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-experience.html")
    time.sleep(0.3)
    page_text = driver.page_source

    # 5 KPI summary cards
    assert "Experience Status" in page_text
    assert "Published" in page_text
    assert "Running on all kiosks" in page_text

    assert "Current Release" in page_text
    assert "v2.2.0" in page_text

    assert "Total Screens" in page_text
    assert "26" in page_text

    assert "Navigation Nodes" in page_text
    assert "112" in page_text

    assert "Last Updated" in page_text
    assert "18 May 2025" in page_text

def test_experience_structure_canvas_and_nodes(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-experience.html")
    time.sleep(0.3)
    page_text = driver.page_source

    assert "Experience Structure" in page_text
    assert "Map View" in page_text

    # 8 sections present in sidebar list
    section_btns = driver.find_elements(By.CSS_SELECTOR, ".section-list-sidebar .section-list-btn")
    assert len(section_btns) == 8
    btn_texts = [b.text for b in section_btns]
    assert any("Home" in t for t in btn_texts)
    assert any("Directory" in t for t in btn_texts)
    assert any("Offers & Deals" in t for t in btn_texts)
    assert any("Events" in t for t in btn_texts)
    assert any("Food & Dining" in t for t in btn_texts)
    assert any("Amenities" in t for t in btn_texts)
    assert any("Services" in t for t in btn_texts)
    assert any("Navigation" in t for t in btn_texts)

    # 8 node cards on map
    node_cards = driver.find_elements(By.CSS_SELECTOR, ".exp-node-card")
    assert len(node_cards) == 8

    # Click on "Offers & Deals" section
    offers_btn = [b for b in section_btns if "Offers & Deals" in b.text][0]
    offers_btn.click()
    time.sleep(0.2)
    selected_node = driver.find_element(By.CSS_SELECTOR, ".exp-node-card.selected")
    assert "Offers & Deals" in selected_node.text

def test_experience_info_and_quick_actions(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-experience.html")
    time.sleep(0.3)
    page_text = driver.page_source

    # Info panel
    assert "Phoenix Mall Experience" in page_text
    assert "Mall / Indoor Venue" in page_text
    assert "Company Admin" in page_text

    # 4 Quick Actions
    assert "Preview Experience" in page_text
    assert "View Experience Analytics" in page_text
    assert "Request Experience Change" in page_text
    assert "View Release History" in page_text

    # View on Kiosk button
    kiosk_btn = driver.find_element(By.ID, "btnViewOnKiosk")
    assert "View on Kiosk" in kiosk_btn.text

    # Health & Notes
    assert "Experience Health" in page_text
    assert "Excellent" in page_text
    assert "26 / 26" in page_text
    assert "112 / 112" in page_text
    assert "Experience Notes" in page_text
    assert "The experience structure is managed by" in page_text

def test_strict_client_admin_experience_boundaries(driver, base_url):
    driver.get(f"{base_url}/client-admin/project-experience.html")
    buttons = driver.find_elements(By.TAG_NAME, "button")
    links = driver.find_elements(By.TAG_NAME, "a")
    interactive_texts = [b.text.strip().lower() for b in buttons + links if b.text]

    # Boundaries: No Company builder controls
    assert "create screen" not in interactive_texts
    assert "delete screen" not in interactive_texts
    assert "edit screen" not in interactive_texts
    assert "add component" not in interactive_texts
    assert "create navigation" not in interactive_texts
    assert "publish" not in interactive_texts
    assert "release" not in interactive_texts
    assert "deploy" not in interactive_texts
