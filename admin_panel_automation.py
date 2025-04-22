# admin_panel_automation.py
import pyautogui
import subprocess
import time

# Step 1: Launch the dashboard (student.py)
subprocess.Popen(["python", "student.py"])
time.sleep(5)  # Wait for the window to load

# Step 2: Login
# Adjust (x, y) coordinates as per your screen
pyautogui.click(x=400, y=300)  # Username field
pyautogui.write("chirag", interval=0.1)

pyautogui.click(x=400, y=350)  # Password field
pyautogui.write("1234", interval=0.1)

pyautogui.click(x=420, y=400)  # Login button
time.sleep(3)

# Step 3: Click "Start Attendance App" button
pyautogui.click(x=450, y=470)
time.sleep(5)  # Wait for the new Tkinter window to load

# 🎯 Step 4: Interact with Admin Panel buttons
# You must adjust (x, y) coordinates based on your actual layout.

# Click "Register Student"
pyautogui.click(x=300, y=200)
time.sleep(2)

# Click "Train Images"
pyautogui.click(x=300, y=250)
time.sleep(5)  # Let training complete

# Click "View Attendance"
pyautogui.click(x=300, y=300)
time.sleep(2)

# Click "Train Face Model"
pyautogui.click(x=300, y=350)
time.sleep(3)

# Click "Logout" or "Back"
pyautogui.click(x=300, y=400)
time.sleep(2)

print("✅ Admin panel automation completed successfully.")
import pyautogui
import time

print("Move your mouse to the target location...")
time.sleep(5)
while True:
    print(pyautogui.position())
    time.sleep(1)
