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

# Initialize driver with webdriver-manager (this handles chromedriver updates)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Maximize window and navigate to the app URL
driver.maximize_window()
driver.get("http://127.0.0.1:5000")  # Ensure Flask app is running

try:
    print("🔒 Logging in...")

    # Wait for and interact with login fields
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    password_input = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.XPATH, '//input[@type="submit"]')

    username_input.send_keys("chirag")
    password_input.send_keys("1234")
    login_button.click()
    print("✅ Login successful")

    # Wait for the "Start Attendance App" button on the home page
    print("⏳ Waiting for 'Start Attendance App' button...")
    start_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Start Attendance App']"))
    )
    start_button.click()
    print("🚀 Attendance App started!")

    # Wait for page transition and ensure the page is fully loaded before looking for the 'Student Details' button
    time.sleep(5)

    print("⏳ Waiting for 'Student Details' button to be clickable...")

    # Check for visibility and try clicking with different strategies

    try:
        # 1. Check if the 'Student Details' button is visible and clickable
        student_details_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Student Details')]"))
        )
        student_details_button.click()
        print("📋 Opened Student Registration form")
        
    except TimeoutException:
        # If the first method fails, we check the image element and click on its parent
        try:
            student_details_button = WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable((By.XPATH, "//img[@src='students.jpeg']/Student Details"))
            )
            student_details_button.click()
            print("📋 Opened Student Registration form via image parent")
        except TimeoutException:
            print("❌ Timeout while waiting for 'Student Details' button")
            print(driver.page_source)  # Log the page source for debugging

    # Wait for the Student Details form to appear
    student_name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "student_name"))
    )
    roll_no_input = driver.find_element(By.NAME, "roll_no")
    department_input = driver.find_element(By.NAME, "department")
    save_button = driver.find_element(By.XPATH, "//button[text()='Save']")

    # Fill in the student details form
    print("⏳ Filling student details...")
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
    # Uncomment if you want the browser to close automatically after completion
    driver.quit()
