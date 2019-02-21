from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

mobile_emulation = { "deviceName": "iPad" }

browserProfile = webdriver.ChromeOptions()

browserProfile.add_experimental_option("mobileEmulation", mobile_emulation)

browserProfile.add_argument('--headless')

driver = webdriver.Chrome(options=browserProfile)

driver.get('https://smartcinema.co/')

time.sleep(2)

page = driver.find_element_by_tag_name('body')
page.send_keys(Keys.ARROW_DOWN)
print('scrolled down!')
time.sleep(0.5)
page.send_keys(Keys.ARROW_DOWN)
print('scrolled down!')
time.sleep(0.5)
page.send_keys(Keys.ARROW_DOWN)
print('scrolled down!')
time.sleep(0.5)
page.send_keys(Keys.ARROW_DOWN)
time.sleep(0.5)
page.send_keys(Keys.ARROW_DOWN)
time.sleep(0.5)
page.send_keys(Keys.ARROW_DOWN)
time.sleep(0.5)
page.send_keys(Keys.ARROW_DOWN)
time.sleep(0.5)
page.send_keys(Keys.ARROW_DOWN)
time.sleep(0.5)
page.send_keys(Keys.ARROW_DOWN)
time.sleep(0.5)
page.send_keys(Keys.ARROW_DOWN)
time.sleep(0.5)
page.send_keys(Keys.ARROW_DOWN)
time.sleep(0.5)
page.send_keys(Keys.ARROW_DOWN)
time.sleep(0.5)
page.send_keys(Keys.ARROW_DOWN)
time.sleep(0.5)
page.send_keys(Keys.ARROW_DOWN)
time.sleep(0.5)
page.send_keys(Keys.ARROW_DOWN)
print('descended further down the page')
time.sleep(2)

driver.quit()