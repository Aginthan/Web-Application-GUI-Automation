from playwright.sync_api import sync_playwright
import time

with sync_playwright() as playwright:
    #//open browser 
    appdata ="C:\\Users\\Aginthan\\AppData\\Local\\Google\\Chrome\\User Data" 
    browser = playwright.chromium.launch_persistent_context(appdata, headless=False, slow_mo=1000)
    #//open a page
    page = browser.new_page()
    #//visit UISP Portal
    page.goto("https://skamgq.uisp.com/nms/devices")
    
    
#//VALAR_1
    valar = page.locator("xpath=//td[contains(@data-autotest,'tableColumn:identification.displayName')]//div//div//span//span//div[contains(text(),'VALAR')]")
    valar.click()
    manage = page.locator("xpath=//button[contains(@data-testid,'Manage')]//span//div")
    manage.click()
    restart = page.locator("xpath=//span[normalize-space()='Restart']")
    restart.click()

#//followup Function
    def follow_up():
        manage.click()
        if restart.is_visible():
            restart.click()
        else:
            print(Name+" cannot be restarted because it's OFFLINE")
            
            





#//FINISHING CHUNK

print("!")
print("  !!!")
print("      !!!")
print("           !!!! ALL REBOOTED !!!!!!")
print("!!YOU CAN FIND ALL THE RECORDS ABOVE !!!")





#browser.close()         