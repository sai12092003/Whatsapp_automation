from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import sys
import time

def setup_chrome():
    try:
        user_data_dir = os.path.join(os.environ['USERPROFILE'], 'AppData', 'Local', 'Google', 'Chrome', 'User Data')
        
        options = Options()
        options.add_argument(f'user-data-dir={user_data_dir}')
        options.add_argument('--profile-directory=Default')
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-notifications')
        options.add_argument('--no-sandbox')
        options.add_argument('--start-maximized')
        
        service = Service('D:/Python_Projects/web-auto/chromedriver.exe')
        driver = webdriver.Chrome(service=service, options=options)
        return driver
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

def quick_send_message(driver, contact_name, message, count):
    try:
        # Load WhatsApp Web
        driver.get('https://web.whatsapp.com/')
        time.sleep(5)  # Quick initial wait
        
        # Use XPATH to find and click search box
        search_xpath = '//div[@contenteditable="true"][@data-tab="3"]'
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, search_xpath))
        )
        search_box.click()
        search_box.send_keys(contact_name)
        time.sleep(2)
        
        # Click the first matching contact
        contact_xpath = f"//span[@title='{contact_name}']"
        contact = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, contact_xpath))
        )
        contact.click()
        time.sleep(1)
        
        # Find message box and send messages
        msg_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="10"]')
        
        for i in range(count):
            msg_box.send_keys(message)
            msg_box.send_keys(Keys.ENTER)
            time.sleep(0.5)
            
        return True
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

def main():
    driver = setup_chrome()
    if driver:
        try:
            quick_send_message(driver, "Amma", "Hi", 5)
            time.sleep(2)  # Brief wait to ensure messages are sent
        finally:
            driver.quit()

if __name__ == "__main__":
    main()
