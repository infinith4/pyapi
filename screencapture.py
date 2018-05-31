import os
from selenium import webdriver

# URL & File Name
URL = "https://www.google.com"
FILENAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screen.png")

# Open Web Browser & Resize 720P
driver = webdriver.Firefox()
driver.set_window_size(1280, 720)
driver.get(URL)

# Get Screen Shot
driver.save_screenshot(FILENAME)

# Close Web Browser
driver.quit()
