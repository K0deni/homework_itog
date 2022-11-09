import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Basket_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Locators"""
    basket_title = "//span[@class='big-title']"
    basket_price_1 = "//span[@class='current-price']"
    basket_price_2 = "//td[@class='table-item table-item__second basket-total']"
    basket_next_page = "//button[@id='order-auth-button']"

    def get_basket_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.basket_title)))

    def get_basket_price_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.basket_price_1)))

    def get_basket_price_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.basket_price_2)))

    def get_basket_new_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.basket_next_page)))

    def click_basket_next_page(self):
        self.get_basket_new_page().click()
        print("New page button")

    def basket(self):
        time.sleep(1)
        self.get_current_url()
        self.get_screenshot()
        self.assert_elements(self.get_basket_price_1(), self.get_basket_price_2())
        self.click_basket_next_page()


