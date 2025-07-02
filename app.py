from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome options (optional)
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--incognito")

# Start Chrome with the correct driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open a webpage to test
driver.get("https://www.google.com")

# Wait a few seconds
time.sleep(25)

# Close the browser
driver.quit()
