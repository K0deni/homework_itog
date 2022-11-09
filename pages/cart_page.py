import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Locators"""
    iphone_14_price = "//span[@class='product__price']"
    iphone_14_buy = "//button[@class='button-buy button button-animated add-to-basket button-animated--no-after js-add-to-basket-detail ']"
    iphone_14_basket = "//a[@class='pink-bttn-normal js-basket-order-btn']"

    def get_iphone_14_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.iphone_14_price)))

    def get_iphone_14_buy(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.iphone_14_buy)))

    def get_iphone_14_basket(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.iphone_14_basket)))

    def click_iphone_14_buy(self):
        self.get_iphone_14_buy().click()
        print("Buy iphone 14 button")

    def click_iphone_14_basket(self):
        self.get_iphone_14_basket().click()
        print("Open basket page")

    def cart(self):
        self.get_current_url()
        self.get_screenshot()
        self.get_iphone_14_price()
        self.assert_word(self.get_iphone_14_price(), '79 990 ₽')
        self.click_iphone_14_buy()
        self.click_iphone_14_basket()



