import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def test_client_projects_page_loads(driver, base_url):
    driver.get(f"{base_url}/client-admin/projects.html")
    assert "Projects" in driver.title

    # 1. Active Sidebar Item
    active_nav = driver.find_element(By.CSS_SELECTOR, ".sidebar-nav .nav-item.active")
    assert "Projects" in active_nav.text

    # 2. Strict 8 Sidebar items check
    nav_items = driver.find_elements(By.CSS_SELECTOR, ".sidebar-nav .nav-item")
    assert len(nav_items) == 8
    nav_texts = [item.text.strip() for item in nav_items]
    assert "Dashboard" in nav_texts
    assert "Projects" in nav_texts
    assert "Content" in nav_texts
    assert "Themes" in nav_texts
    assert "Advertisements" in nav_texts
    assert "Analytics" in nav_texts
    assert "Feedback" in nav_texts
    assert "Requests" in nav_texts

    # 3. 5 KPI Summary Boxes
    kpi_boxes = driver.find_elements(By.CLASS_NAME, "kpi-stat-box")
    assert len(kpi_boxes) == 5
    page_text = driver.page_source
    assert "Total Projects" in page_text
    assert "Total Kiosks" in page_text
    assert "Avg. Uptime" in page_text
    assert "98.6%" in page_text
    assert "Total Visitors" in page_text
    assert "128,450" in page_text
    assert "Total Interactions" in page_text
    assert "321,845" in page_text

def test_my_projects_list_and_selection(driver, base_url):
    driver.get(f"{base_url}/client-admin/projects.html")
    time.sleep(0.3)

    cards = driver.find_elements(By.CSS_SELECTOR, "#projectsListContainer .project-card-item")
    assert len(cards) == 4

    # Default selected is Phoenix Mall
    ov_title = driver.find_element(By.ID, "ovProjectTitle").text
    assert "Phoenix Mall Project" in ov_title

    # Select second card (Phoenix Marketcity Project)
    cards[1].click()
    time.sleep(0.2)
    new_ov_title = driver.find_element(By.ID, "ovProjectTitle").text
    assert "Phoenix Marketcity Project" in new_ov_title
    assert "Marketcity" in driver.find_element(By.ID, "ovProjectSub").text

def test_project_search_and_filters(driver, base_url):
    driver.get(f"{base_url}/client-admin/projects.html")
    time.sleep(0.3)

    # 1. Search Filter
    search_input = driver.find_element(By.ID, "leftSearchProjects")
    search_input.clear()
    search_input.send_keys("Marketcity")
    driver.execute_script("filterProjectCards()")
    time.sleep(0.2)

    cards = driver.find_elements(By.CSS_SELECTOR, "#projectsListContainer .project-card-item")
    visible_cards = [c for c in cards if c.is_displayed()]
    assert len(visible_cards) == 1
    assert "Phoenix Marketcity Project" in visible_cards[0].text

    # 2. Reset Search and Filter by Status "Upcoming"
    search_input.clear()
    status_select_el = driver.find_element(By.ID, "projectStatusFilter")
    select_obj = Select(status_select_el)
    select_obj.select_by_value("Upcoming")
    driver.execute_script("filterProjectCards()")
    time.sleep(0.2)

    cards = driver.find_elements(By.CSS_SELECTOR, "#projectsListContainer .project-card-item")
    visible_cards = [c for c in cards if c.is_displayed()]
    assert len(visible_cards) == 1
    assert "Phoenix Palladium Project" in visible_cards[0].text

    # 3. Reset Filter to "All"
    select_obj.select_by_value("All")
    driver.execute_script("filterProjectCards()")
    time.sleep(0.2)
    cards = driver.find_elements(By.CSS_SELECTOR, "#projectsListContainer .project-card-item")
    visible_cards = [c for c in cards if c.is_displayed()]
    assert len(visible_cards) == 4

def test_project_overview_tabs_and_open_action(driver, base_url):
    driver.get(f"{base_url}/client-admin/projects.html")
    time.sleep(0.3)

    # Overview Tabs
    tabs = driver.find_elements(By.CSS_SELECTOR, ".overview-nav-tabs .overview-tab")
    tab_names = [t.text.strip() for t in tabs]
    assert "Overview" in tab_names
    assert "Kiosks" in tab_names
    assert "Experience" in tab_names
    assert "Content" in tab_names
    assert "Themes" in tab_names
    assert "Advertisements" in tab_names
    assert "Analytics" in tab_names

    # View Full Details button
    btn_open = driver.find_element(By.ID, "btnOpenFullProject")
    assert "View Full Details" in btn_open.text

def test_strict_client_admin_boundaries_projects(driver, base_url):
    driver.get(f"{base_url}/client-admin/projects.html")
    buttons = driver.find_elements(By.TAG_NAME, "button")
    links = driver.find_elements(By.TAG_NAME, "a")
    interactive_texts = [b.text.strip().lower() for b in buttons + links if b.text]

    # Boundaries: No Company builder controls
    assert "create project" not in interactive_texts
    assert "new project" not in interactive_texts
    assert "project wizard" not in interactive_texts
    assert "create screen" not in interactive_texts
    assert "create theme" not in interactive_texts
    assert "create advertisement" not in interactive_texts
    assert "build experience" not in interactive_texts
    assert "edit map" not in interactive_texts
    assert "edit navigation" not in interactive_texts
    assert "publish" not in interactive_texts
    assert "release" not in interactive_texts
    assert "deploy" not in interactive_texts
