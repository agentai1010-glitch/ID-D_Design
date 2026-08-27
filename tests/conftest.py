import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set cache and temp to D: drive since C: drive has 0 space
os.environ["SE_CACHE_PATH"] = r"D:\selenium_cache"
os.environ["TEMP"] = r"D:\temp"
os.environ["TMP"] = r"D:\temp"

if not os.path.exists(r"D:\selenium_cache"):
    os.makedirs(r"D:\selenium_cache", exist_ok=True)
if not os.path.exists(r"D:\temp"):
    os.makedirs(r"D:\temp", exist_ok=True)

@pytest.fixture(scope="session")
def base_url():
    return "http://localhost:8000"

@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(4)
    yield driver
    driver.quit()
