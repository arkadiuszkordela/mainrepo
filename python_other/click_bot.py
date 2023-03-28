#The application was created only for testing. It is not fair and illegal to use it for commercial purposes!

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from datetime import datetime

PATH = '/home/<username>/chromedriver'
driver = webdriver.Chrome(PATH)
#We have to download a Chromedriver and move it to the directory above. Download link below:
#https://sites.google.com/chromium.org/driver/
 
driver.get('https://timebucks.com/publishers/index.php?pg=earn&tab=view_content_ads')

wait = WebDriverWait(driver, 5)

login = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Log in with facebook')))
login.click()

facebook_login = wait.until(EC.element_to_be_clickable((By.ID, 'email')))
facebook_login.send_keys('<login>')
facebook_login.send_keys(Keys.TAB)
facebook_password = wait.until(EC.element_to_be_clickable((By.ID, 'pass')))
facebook_password.send_keys('<password>')
facebook_password.send_keys(Keys.RETURN)

driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get('https://timebucks.com/publishers/index.php?pg=earn&tab=view_content_ads')


for x in range(86400):
    try:
        click = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btnClickAdd")))
        click.click()
        sleep(55)
        driver.switch_to.window(driver.window_handles[2])
        driver.close()
        driver.switch_to.window(driver.window_handles[1])
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(current_time)
        continue
    except:
        sleep(55)
        driver.refresh()
    
sleep(86400)