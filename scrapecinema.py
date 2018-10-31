from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

class Smartcinema():
    def __init__(self, browsingMode):
        self.browsingMode = browsingMode
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_argument(browsingMode)
        self.browser = webdriver.Chrome(chrome_options=self.browserProfile)


    def goToPage(self):
        self.browser.get('https://smartcinema.co/')
        print('Browser initialized successfully')
        time.sleep(2)
        self.browser.maximize_window()
        print('Maximized')
        time.sleep(1)


    def clickAround(self):
        driver = self.browser
        actions = ActionChains(driver)
        browsingMode = self.browsingMode
        detailBtn = driver.find_element_by_css_selector('.et_pb_more_button')
        arrowNext = driver.find_element_by_css_selector('.et-pb-arrow-next')
        arrowPrev = driver.find_element_by_css_selector('.et-pb-arrow-prev')
        showPrograme = driver.find_element_by_xpath("//*[contains(text(), 'Show programe')]")

        time.sleep(2)
        detailBtn.click()
        print('Clicked the detail button')
        time.sleep(1)
        detailBtn.click()
        print('Clicked the detail button')
        time.sleep(1)
        arrowNext.click()
        print('Clicked the right arrow button')
        time.sleep(3)
        arrowNext.click()
        print('Clicked the right arrow button')
        time.sleep(3)
        arrowPrev.click()
        print('Clicked the left arrow button')
        time.sleep(3)
        time.sleep(2)
        print(showPrograme.location)
        if(browsingMode == '--kiosk'):
            showPrograme.click()
            print('Clicked the show programe button')
            buyFilms = driver.find_element_by_id('menu-item-48')
            buyFilms.click()
            print('Clicked the buy films button')
        if(browsingMode == 'headless'):
            burgerMenu = driver.find_element_by_class_name('mobile_menu_bar_toggle')
            burgerMenu.click()
            print('Clicked the burger nav menu')
            time.sleep(1)
            buyFilms = driver.find_element_by_id('menu-item-48')
            print(buyFilms.location)
            actions.move_to_element(buyFilms)
            driver.save_screenshot('tablet.png')
            # buyFilms.click()
            # print('Clicked the buy films button')

        time.sleep(2)

    def closeBrowser(self):
        self.browser.close()
        print('Browser closed successfully')

def browse_on_desktop():
    auto = Smartcinema('--kiosk')
    auto.goToPage()
    auto.clickAround()
    auto.closeBrowser()

def browse_on_tablet():
    auto = Smartcinema('headless')
    auto.goToPage()
    auto.clickAround()
    auto.closeBrowser()

browse_on_desktop()
time.sleep(2)
browse_on_tablet()