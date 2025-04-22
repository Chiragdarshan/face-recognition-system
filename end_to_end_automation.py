from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome WebDriver
chromedriver_path = "C:/path/to/chromedriver.exe"  # Update with correct path
service = Service(chromedriver_path)
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=service, options=options)

# Step 1: Open login page
driver.get("http://127.0.0.1:5000")  # Make sure Flask app is running
driver.find_element(By.NAME, "username").send_keys("chirag")
driver.find_element(By.NAME, "password").send_keys("1234")
driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(2)

# Step 2: Start Attendance App
driver.find_element(By.ID, "start attendance app").click()
time.sleep(2)

# Step 3: Student Registration (optional step, depending on workflow)
driver.get("http://127.0.0.1:5000/student_registration")
driver.find_element(By.NAME, "name").send_keys("John Doe")
driver.find_element(By.NAME, "roll_no").send_keys("12345")
driver.find_element(By.NAME, "department").send_keys("Computer Science")
driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(2)

# Step 4: Face Training
driver.get("http://127.0.0.1:5000/face_training")
driver.find_element(By.ID, "train_faces_button").click()
time.sleep(2)

# Step 5: Run Attendance
driver.get("http://127.0.0.1:5000/run_attendance")
driver.find_element(By.ID, "start_attendance_button").click()
time.sleep(2)

# Step 6: Admin Panel Task
driver.get("http://127.0.0.1:5000/admin_panel")
driver.find_element(By.NAME, "username").send_keys("admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//input[@type='submit']").click()
time.sleep(2)

# Validate if all steps passed
print("✅ End-to-end test completed!")

# Optional: Close the driver when done
driver.quit()
