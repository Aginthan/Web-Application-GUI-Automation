from playwright.sync_api import sync_playwright
import time

with sync_playwright() as playwright:
    #//open browser 
    appdata ="C:\\Users\\Aginthan\\AppData\\Local\\Google\\Chrome\\User Data" 
    browser = playwright.chromium.launch_persistent_context(appdata, headless=False, slow_mo=2000)
    #//open a page
    page = browser.new_page()
    #//visit UISP Portal
    page.goto("https://skamgq.uisp.com/nms/devices")
    
    
#//VALAR_1
    valar = page.locator("xpath=//td[contains(@data-autotest,'tableColumn:identification.displayName')]//div//div//span//span//div[contains(text(),'AMAIA')]")
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

#//FINANCE
    Name = "Swimming-Pool"
    fin_ap = page.locator("xpath=//div[contains(text(),'SWIMMING-POOL')]")
    fin_ap.click()
    follow_up()

#//FL-UNIT
    Name = "FL-UNIT"
    fl_unit = page.locator("xpath=//div[contains(text(),'SKA-FL UNIT')]")
    fl_unit.click()
    follow_up()
    
#//BAIDOA-OUTDOOR
    Name = "BAIDOA-OUTDOOR"
    baidoa_out = page.locator("xpath=//div[contains(text(),'Baidoa - Workshop Outdoor AP')]")
    baidoa_out.click()
    follow_up()

#//PAE
    Name = "PAE"
    pae = page.locator("xpath=//td[contains(@data-autotest,'tableColumn:identification.displayName')]//div//div//span//span//div[contains(text(),'PAE')]")
    pae.click()
    follow_up()


#//ska-fuelfarm
    Name = "ska-fuelfarm"
    ska_fuelfarm = page.locator("xpath=(//div[contains(text(),'SKA FUEL FARM')])[1]")
    ska_fuelfarm.click()
    follow_up()

#//AMK9-ACCOM
    Name = "AMK9-ACCOM"
    amk9_accom = page.locator("xpath=//td[contains(@data-autotest,'tableColumn:identification.displayName')]//div//div//span//span//div[contains(text(),'AMK9-ACCOM')]")
    amk9_accom.click()
    follow_up()

#//CONSTRUCTION-AP
    Name = "Construction-AP"
    cons_ap = page.locator("xpath=//div[contains(text(),'CONSTRUCTION AP')]")
    cons_ap.click()
    follow_up()

#//BAIDOA AP1
    Name = "BAIDOA-AP1"
    baidoa_ap1 = page.locator("xpath=//div[contains(text(),'BAIDOA-AP1')]")
    baidoa_ap1.click()
    follow_up()

#//BC2
    Name = "BC2"
    bc2 = page.locator("xpath=//td[contains(@data-autotest,'tableColumn:identification.displayName')]//div//div//span//span//div[contains(text(),'BC2')]")
    bc2.click()
    follow_up()

#//BAIDOA-AP2
    Name = "BAIDOA-AP2"
    baidoa_ap2 = page.locator("xpath=//div[contains(text(),'BAIDOA-AP2')]")
    baidoa_ap2.click()
    follow_up()
    
#//OLD FUEL ACCOM
    Name = "Old Fuel Accom AP"
    old_fuelap = page.locator("xpath=//div[contains(text(),'FUEL ACCOMMODATION')]")
    old_fuelap.click()
    follow_up()

#//Picostation M2
    Name = "Picostation M2"
    pico_m2 = page.locator("xpath=//div[contains(text(),'PicoStation M2')]")
    pico_m2.click()
    follow_up()

#//BC1
    Name = "BC1"
    bc1 = page.locator("xpath=//td[contains(@data-autotest,'tableColumn:identification.displayName')]//div//div//span//span//div[contains(text(),'BC1')]")
    bc1.click()
    follow_up()

#//TOYOTA-AP
    Name = "TOYOTA-AP"
    toyota_ap = page.locator("xpath=//div[contains(text(),'TOYOTA AP')]")
    toyota_ap.click()
    follow_up()

#//WORKSHOP
    Name = "WORKSHOP"
    workshop = page.locator("xpath=//td[@data-autotest='tableColumn:identification.displayName']//div//div//span//span//div[contains(text(),'WORKSHOP')]")
    workshop.click()
    follow_up()

#//CRC-M2
    Name = "CRC-M2"
    crc_m2 = page.locator("xpath=//div[contains(text(),'CRC-M2')]")
    crc_m2.click()
    follow_up()

#//GAMES ROOM
    Name = "Games Room"
    games_ap = page.locator("xpath=//div[contains(text(),'Games Room')]")
    games_ap.click()
    follow_up()

#//VIP-MEETING
    Name = "VIP-MEETING"
    vip_ap = page.locator("xpath=//div[contains(text(),'MEETING VIP')]")
    vip_ap.click()
    follow_up()

#//NEW VEES LOUNGE
    Name = "NEW VEES LOUNGE"
    vees2_ap = page.locator("xpath=//div[contains(text(),'NEW VEES LOUNGE')]")
    vees2_ap.click()
    follow_up()
    
#//FC2
    Name = "FC2"
    fc2 = page.locator("xpath=//td[@data-autotest='tableColumn:identification.displayName']//div//div//span//span//div[contains(text(),'FC2')]")
    fc2.click()
    follow_up()

#//MEETING White
    Name = "White Meeting AP"
    white_ap = page.locator("xpath=//div[contains(text(),'MEETING WHITE')]")
    white_ap.click()
    follow_up()

#//SAIC Office
    Name = "SAIC office"
    saic_ap = page.locator("xpath=//div[contains(text(),'SAIC OFFICE')]")
    saic_ap.click()
    follow_up()

#//FC5
    Name = "FC5"
    fc5 = page.locator("xpath=//div[contains(text(),'FC-5')]")
    fc5.click()
    follow_up()

#//PROCUREMENT
    Name = "Procurement AP"
    procure_ap = page.locator("xpath=//div[contains(text(),'PROCUREMENT AP')]")
    procure_ap.click()
    follow_up()

#//BC4
    Name = "BC4"
    bc4 = page.locator("xpath=//div[contains(text(),'BC4')]")
    bc4.click()
    follow_up()

#//BUNKER
    Name = "BUNKER"
    bunker = page.locator("xpath=//td[@data-autotest='tableColumn:identification.displayName']//div//div//span//span//div[contains(text(),'BUNKER')]")
    bunker.click()
    follow_up()

#//GIZ-AP
    Name = "GIZ-AP"
    giz_ap = page.locator("xpath=//div[contains(text(),'GIZ-AP')]")
    giz_ap.click()
    follow_up()

#//NEW UNION
    Name = "NEW UNION"
    new_union = page.locator("xpath=//td[@data-autotest='tableColumn:identification.displayName']//div//div//span//span//div[contains(text(),'NEW UNION')]")
    new_union.click()
    follow_up()

#//BF FUEL ACCOMODATION
    Name = "BF-FUEL AP"
    bf_ap = page.locator("xpath=//div[contains(text(),'BF-FUEL ACCOMMODATION')]")
    bf_ap.click()
    follow_up()

#//BC3
    Name = "BC3"
    bc3 = page.locator("xpath=//td[@data-autotest='tableColumn:identification.displayName']//div//div//span//span//div[contains(text(),'BC3')]")
    bc3.click()
    follow_up()

#//CMT OFFICE
    Name = "CMT OFFICE"
    cmt_ap = page.locator("xpath=//div[contains(text(),'CMT Office')]")
    cmt_ap.click()
    follow_up()

#//PAE ARMSTORE
    Name = "PAE ARMSTORE"
    pae_arm = page.locator("xpath=//div[contains(text(),'PAE ARMS STORE')]")
    pae_arm.click()
    follow_up()

#//BC5
    Name = "BC5"
    bc5 = page.locator("xpath=//td[@data-autotest='tableColumn:identification.displayName']//div//div//span//span//div[contains(text(),'BC5')]")
    bc5.click()
    follow_up()

#//FLB-WORKSHOP TEST
    Name = "FLB-WORKSHOP AP"
    flb_work = page.locator("xpath=//div[contains(text(),'FLB- WORKSHOP TEST')]")
    flb_work.click()
    follow_up()

#//UNION 3
    Name = "UNION 3"
    union_3 = page.locator("xpath=//td[@data-autotest='tableColumn:identification.displayName']//div//div//span//span//div[contains(text(),'UNION 3')]")
    union_3.click()
    follow_up()

#//BAIDOA-AP3
    Name = "BAIDOA-AP3"
    baidoa_ap3 = page.locator("xpath=//div[contains(text(),'BAIDOA-AP3')]")
    baidoa_ap3.click()
    follow_up()

#//PAE-MEETING
    Name = "PAE-MEETING"
    pae_meeting = page.locator("xpath=//td[@data-autotest='tableColumn:identification.displayName']//div//div//span//span//div[contains(text(),'PAE-MEETING')]")
    pae_meeting.click()
    follow_up()

#//DFAC
    Name = "DFAC"
    dfac = page.locator("xpath=//td[@data-autotest='tableColumn:identification.displayName']//div//div//span//span//div[contains(text(),'DFAC')]")
    dfac.click()
    follow_up()

#//BAIDOA BLUECOM
    Name = "BAIDOA BLUECOM"
    baidoa_blue = page.locator("xpath=//div[contains(text(),'Baidoa- Bluecom')]")
    baidoa_blue.click()
    follow_up()

#//BAIDOA CLIENT-AP
    Name = "BAIDOA CLIENT-AP"
    baidoa_client = page.locator("xpath=//div[contains(text(),'BAIDOA-CLIENT AP')]")
    baidoa_client.click()
    follow_up()

#//Meeting Green
    Name = "MEETING GREEN"
    meeting_green = page.locator("xpath=//div[contains(text(),'MEETING GREEN')]")
    meeting_green.click()
    follow_up()



#//FINISHING CHUNK

print("!")
print("  !!!")
print("      !!!")
print("           !!!! ALL REBOOTED !!!!!!")
print("!!YOU CAN FIND ALL THE RECORDS ABOVE !!!")





#browser.close()         