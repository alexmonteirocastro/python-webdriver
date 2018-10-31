from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

class Navigate():

    def __init__(self):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_argument('--headless')
        self.browserProfile.add_argument('window-size=2024,1024')
        self.driver = webdriver.Chrome(options=self.browserProfile)
        self.actions = ActionChains(self.driver)
        dimensions = self.driver.get_window_size()
        print(dimensions)

    def land(self):
        self.driver.get('https://smartcinema.co/')
        print('Initialized successfully')
        time.sleep(2)

    def carousel(self):
        next_arr = self.driver.find_element_by_class_name('et-pb-arrow-next')
        prev_arr = self.driver.find_element_by_class_name('et-pb-arrow-prev')
        next_arr.click()
        print('clicked the next button')
        time.sleep(1)
        next_arr.click()
        print('clicked the next button')
        time.sleep(1)
        prev_arr.click()
        print('clicked the previous button')
        time.sleep(2)
        print('Let\'s rage click the show detail button')
        time.sleep(2)
        detail_btn = self.driver.find_element_by_class_name('et_pb_more_button')
        print('Let\'s mouse over the detail button')
        self.actions.move_to_element(detail_btn).perform()
        detail_btn = self.driver.find_element_by_xpath('//*[@id="et-boc"]/div/div[1]/div/div/div/div[1]/div[2]/div/div/div/div[2]/a')
        detail_btn.click()
        time.sleep(1)
        print('Cicked the show detail btton')
        time.sleep(1)
        detail_btn.click()
        print('Cicked the show detail btton')
        time.sleep(1)
        detail_btn.click()
        print('Cicked the show detail btton')
        detail_btn.click()
        time.sleep(1)

    def show_programe(self):
        programe_header = self.driver.find_element_by_class_name('et_pb_text_inner')
        self.actions.move_to_element(programe_header).perform()
        print('moved to the header')
        time.sleep(1)
        show_programe_btn = self.driver.find_element_by_class_name('et_pb_button_0')
        show_programe_btn.click()
        print('clicked the show programe button')
        time.sleep(2)
        # self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(3)

    def descend(self):
        page = self.driver.find_element_by_tag_name('body')
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

    def mouse_over_movies(self):
        print('Let\'s check those movies!')
        movies = self.driver.find_elements_by_class_name('product-type-simple')
        for i in range(len(movies)):
            hover = ActionChains(self.driver).move_to_element(movies[i])
            hover.perform()
            time.sleep(1)

    def pick_movie(self, which):
        movie = self.driver.find_elements_by_class_name('product-type-simple')[which]
        movie.click()
        time.sleep(1)

    def pony(self):
        search_icon = self.driver.find_element_by_id('et_top_search')
        search_icon.click()
        time.sleep(1)
        search_input = self.driver.find_element_by_class_name('et-search-field')
        search_input.send_keys('Pony')
        search_input.send_keys(Keys.ENTER)
        time.sleep(1)

    def finish(self):
        self.driver.quit()
