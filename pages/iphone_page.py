import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Iphone_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Locators"""
    iphone_14_button = "//img[@src='https://static.re-store.ru/upload/iblock/303/303178466d37b01000e71e89b9c6e1be.png']"
    iphone_14_word = "//html/body/div[3]/div[4]/div[2]/div[1]/div[1]/h1"

    def get_iphone_14(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.iphone_14_button)))

    def get_iphone_14_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.iphone_14_word)))

    def click_iphone_14_button(self):
        self.get_iphone_14().click()
        print("Click iphone 14 button")

    def selection(self):
        self.get_current_url()
        self.assert_url('https://re-store.ru/apple-iphone/')
        self.click_iphone_14_button()
