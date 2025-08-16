from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
import time
from selenium.webdriver.chrome.options import Options
#import chrome options

# System.setProperty("webdriver.chrome.driver","C:\Users\Aginthan\Desktop\Automation\chromedriver.exe")
ChromeOptions =Options()
Options.add_argument("user-data-dir=C:/Users/Aginthan/AppData/Local/Google/Chrome/User Data/Default")
Options.add_argument("--start-maximized")
driver=wedriver.chrome(options)


# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://skamgq.uisp.com/nms/devices")

time.sleep(30)

driver.quit()