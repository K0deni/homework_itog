import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Start_page(Base):

    url = 'https://re-store.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Locators"""
    iphone_button = "//a[@href='/apple-iphone/']"
    iphone_word = "//h1[@class='catalog__title']"
    service_button = "//a[@href='/services/']"
    service_page_title = "//h2[@class='s-title']"

    def get_iphone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.iphone_button)))

    def get_iphone_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.iphone_word)))

    def get_service_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.service_button)))

    def get_service_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.service_page_title)))

    def click_iphone_button(self):
        self.get_iphone().click()
        print("Click iphone button")

    def click_service_button(self):
        self.get_service_page().click()
        print("Click service page button")

    def login(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        time.sleep(2)
        self.get_screenshot()
        self.click_iphone_button()
        self.assert_word(self.get_iphone_word(), "iPhone")

    def start(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        time.sleep(2)
        self.click_service_button()
        self.assert_word(self.get_service_title(), "Услуги")
        self.get_screenshot()


