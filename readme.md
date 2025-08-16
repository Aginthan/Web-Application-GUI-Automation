# Automating UISP Web application with Playwright.

## Problem

I had to reboot almost 30 Wireless Access points in my company network every morning by hand clicking around the console. This was easy but repetitive and inefficient.

## Constraints

I considered developing a script to automate the reboot process by using SSH to connect to each access point. However, this method presented a significant challenge: all access points were configured with DHCP, meaning their IP addresses could change and cause the script to fail.

## Solution

After researching for about a week on how to automate the process.I thought I would automate the clicking process in GUI of the web application.

## Initial Development.

When searching for tools to automate the clicking process there was pyautogui, selenium,Playwright and other testing tools.

### 1. Pyautogui limitations

- **Dependency on Active Screen:**
PyAutoGUI requires an active graphical user interface (GUI) to operate. It cannot automate tasks on minimized or hidden windows, or without a display.
- **Sensitivity to UI Changes:**
While image recognition helps, significant changes in UI layout, element positions, or screen resolution can still break automation scripts.

### 2. Selenium 

- This is a famous testing tool with great features and has been extensively used across the automation industry.

- he core application required a manual login, which was protected by multi-factor authentication (MFA), to perform the rebooting process. I observed that a manual login allowed the user session to persist, even after the browser was closed. I explored using Selenium to automate this, but despite my research and various attempts, the tool consistently opened the application in a logged-out state and introduced significant complexities, making it an unviable solution.