from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import traceback
import time

# Setup Chrome options
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Initialize driver with webdriver-manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.maximize_window()
driver.get("http://127.0.0.1:5000")  # Make sure Flask app is running

try:
    print("🔒 Logging in...")

    # Login page interactions
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    password_input = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, '//input[@type="submit"]')

    username_input.send_keys("chirag")
    password_input.send_keys("1234")
    login_button.click()
    print("✅ Login successful")

    # Wait for the "Start Attendance App" button on home.html
    print("⏳ Waiting for 'Start Attendance App' button...")
    start_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Start Attendance App']"))
    )
    start_button.click()
    print("🚀 Attendance App started!")

except Exception as e:
    print("❌ An error occurred:")
    traceback.print_exc()

finally:
    time.sleep(5)
    driver.quit()
