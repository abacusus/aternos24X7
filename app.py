from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import os


options = Options()

user_data_path = os.path.join(os.getcwd(), "chrome_user_data")
options.add_argument(f"--user-data-dir={user_data_path}")
options.add_argument('--disk-cache-size=1048576')  # Limit to 1MB (1MB = 1024*1024)



#options.add_argument("--headless")       # Uncomment this to run Chrome in headless mode (no UI)

# Launch Chrome using WebDriver Manager
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# Open the target website
def script():
    driver.get("https://aternos.org/server/")
    time.sleep(5) 
    driver.execute_script("document.getElementById('start').click();")
    time.sleep(5)  
 



#  Close the browser
driver.quit()
