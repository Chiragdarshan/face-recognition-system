from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import traceback

# Setup Chrome options
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # Keeps browser open after script finishes

# Initialize driver with webdriver-manager (auto updates chromedriver)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Maximize window and open the Flask app
driver.maximize_window()
driver.get("http://127.0.0.1:5000")  # Make sure your Flask server is running

try:
    print("🔒 Logging in...")

    # Wait and enter login credentials
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    password_input = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, '//input[@type="submit"]')

    username_input.send_keys("chirag")
    password_input.send_keys("1234")
    login_button.click()
    print("✅ Login successful")

    # Wait for 'Start Attendance App' button
    print("⏳ Waiting for 'Start Attendance App' button...")
    start_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Start Attendance App']"))
    )
    start_button.click()
    print("🚀 Attendance App started!")

    # Optional: Wait for main page content to load
    time.sleep(5)
    print("⏳ Waiting for page to load...")
    try:
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//h1[text()='Home Page']"))
        )
        print("✅ Page loaded")
    except TimeoutException:
        print("❌ Timeout while waiting for page")
        print(driver.page_source)

    # Wait for and click 'Student Details'
    print("📋 Opening Student Registration form...")
    student_details_button = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//p[text()='Student Details']/.."))
    )
    student_details_button.click()

    # Wait for student form inputs
    student_name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "student_name"))
    )
    roll_no_input = driver.find_element(By.NAME, "roll_no")
    department_input = driver.find_element(By.NAME, "department")
    save_button = driver.find_element(By.XPATH, "//button[text()='Save']")

    # Fill in form
    print("✍️ Filling student details...")
    student_name_input.send_keys("John Doe")
    roll_no_input.send_keys("12345")
    department_input.send_keys("Computer Science")
    save_button.click()
    print("✅ Student details saved")

except Exception as e:
    print("❌ An error occurred:")
    traceback.print_exc()

finally:
    time.sleep(5)
    # Uncomment to close the browser after automation
    # driver.quit()
