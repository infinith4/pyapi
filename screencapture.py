import os
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import subprocess

# URL & File Name
URL = "https://www.google.com"
FILENAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screen.png")

# Open Web Browser & Resize 720P
useragent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36"
profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", useragent)
caps = DesiredCapabilities.FIREFOX
caps["firefox_profile"] = profile.encoded
caps["marionette"] = True
caps["binary"] = str(subprocess.check_output(["which", "firefox"]),
                        "utf-8").strip()
driver = webdriver.Firefox()
driver.set_window_size(1280, 720)
driver.get(URL)

# Get Screen Shot
driver.save_screenshot(FILENAME)

# Close Web Browser
driver.quit()
