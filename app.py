from selenium import webdriver
from flask_cors import CORS
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os


options = Options()

user_data_path = os.path.join(os.getcwd(), "chrome_user_data")
options.add_argument(f"--user-data-dir={user_data_path}")
options.add_argument('--disk-cache-size=1048576')  # Limit to 1MB (1MB = 1024*1024)

#options.add_argument("--headless=new")       # Uncomment this to run Chrome in headless mode (no UI)

# Launch Chrome using WebDriver Manager
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)
def script():
 print("Script has started running...")
# Open the target website
 driver.get("https://aternos.org/server/")
 print("Opened the Aternos server page.")
 button = WebDriverWait(driver, 615).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-tiny.btn-success.server-extend-end"))
 )
 button.click()
 print("Button found, clicking it...")



 script()
 print("recursion called...")

 
 driver.quit()
 print("Driver quit, script finished.")
script()

