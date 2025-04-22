from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode (no UI)
chrome_options.add_argument("--disable-gpu")  # Disable GPU for headless mode
chrome_options.add_argument("--no-sandbox")  # Disable sandboxing for better performance

# Set up the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Open the web page
driver.get("http://127.0.0.1:5000")

# Wait for the page to load and the username field to be present
wait = WebDriverWait(driver, 10)
username_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
password_field = wait.until(EC.presence_of_element_located((By.ID, "password")))

# Enter login credentials
username_field.send_keys("chirag")
password_field.send_keys("1234")

# Find the login button and click it
login_button = driver.find_element(By.ID, "login")
login_button.click()

# Wait for the dashboard to load
wait.until(EC.presence_of_element_located((By.ID, "start attendance app")))

# Find the 'Start Attendance App' button and click it
start_attendance_button = driver.find_element(By.ID, "start attendance app")
start_attendance_button.click()

# Wait for the next page to load (you may need to adjust the time based on the actual load time)
time.sleep(5)

# Close the browser
driver.quit()
