from selenium import webdriver
from flask_cors import CORS
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import os
from flask import Flask, jsonify

app = Flask(__name__)
CORS(app)
@app.route('/trigger', methods=['GET'])


def script():
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
 

 driver.get("https://aternos.org/server/")
 driver.minimize_window()
 
 button = driver.find_element(By.ID, "start")
 button.click()
   
 driver.quit()
 print("Script has been triggered!")
 return jsonify({"status": "Script executed!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
