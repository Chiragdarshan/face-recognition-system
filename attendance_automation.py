# attendance_automation.py
import pyautogui
import subprocess
import time

# Step 1: Launch the app (student.py)
subprocess.Popen(["python", "student.py"])
time.sleep(5)  # Wait for login window

# Step 2: Fill Login Credentials
# Replace (x, y) with correct coordinates using pyautogui.position()

# Click username
pyautogui.click(x=400, y=300)
pyautogui.write("chirag", interval=0.1)

# Click password
pyautogui.click(x=400, y=350)
pyautogui.write("1234", interval=0.1)

# Click Login button
pyautogui.click(x=420, y=400)
time.sleep(3)

# Step 3: Click on 'Start Attendance App' button
pyautogui.click(x=450, y=470)
time.sleep(5)

# Step 4: Wait for face recognition window (simulate camera test)
print("📸 Camera started... waiting for face recognition")
time.sleep(10)

# Step 5: Close camera window if you want to automate it
pyautogui.press("esc")  # Or click on close button

print("✅ Attendance automation completed.")
