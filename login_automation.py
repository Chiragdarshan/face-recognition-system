from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome WebDriver
options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(), options=options)

# Open the login page
driver.get("http://127.0.0.1:5000")  # Make sure Flask app is running

# Fill in the login credentials
driver.find_element(By.NAME, "username").send_keys("chirag")
driver.find_element(By.NAME, "password").send_keys("1234")

# Click the login button
driver.find_element(By.XPATH, "//input[@type='submit']").click()

# Wait for navigation
time.sleep(2)

# Validate login
if "home" in driver.current_url:
    print("✅ Login successful!")
else:
    print("❌ Login failed!")

# You can close the driver when done or let it stay open
# driver.quit()
