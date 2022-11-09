import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Iphone_14_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Locators"""
    iphone_14_memory = "/html/body/div[3]/div[4]/div[2]/div[2]/div[2]/div[2]/form/div[4]/div[1]/div/label/span[1]"
    iphone_14_color = "//*[@id='sticky-parent']/form/div[5]/div[4]/div/label/span[2]"
    iphone_14_low_value = "//input[@id='min_price']"
    iphone_14_high_value = "//input[@id='max_price']"
    iphone_14_use_button = "//button[@id='submit_filters_btn']"
    iphone_14_new_page_word = "//html/body/div[3]/div[4]/div[2]/div[1]/div[1]/h1"
    iphone_14_cart_page = "//html/body/div[3]/div[4]/div[2]/div[2]/div[1]/div[2]/a/span[2]"

    def get_iphone_14_memory(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.iphone_14_memory)))

    def get_iphone_14_color(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.iphone_14_color)))

    def get_iphone_14_low_value(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.iphone_14_low_value)))

    def get_iphone_14_high_value(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.iphone_14_high_value)))

    def get_iphone_14_use_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.iphone_14_use_button)))

    def get_iphone_14_cart_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.iphone_14_cart_page)))

    def click_iphone_14_memory(self):
        self.get_iphone_14_memory().click()
        print("Select iphone 14 memory size")

    def click_iphone_14_color(self):
        self.get_iphone_14_color().click()
        print("Select iphone 14 color")

    def click_iphone_14_cart_page(self):
        self.get_iphone_14_cart_page().click()
        print("Cart page open")

    def input_iphone_14_low_value(self, low_value):
        self.get_iphone_14_low_value().send_keys(low_value)
        print("Input iphone 14 low cost value" + ' ' + low_value)

    def input_iphone_14_high_value(self, high_value):
        self.get_iphone_14_high_value().send_keys(high_value)
        print("Input iphone 14 high cost value" + ' ' + high_value)

    def click_iphone_14_use(self):
        self.get_iphone_14_use_button().click()
        print("Select iphone 14 use button")

    def iphone_14_search(self):
        self.get_current_url()
        self.click_iphone_14_memory()
        self.click_iphone_14_color()
        self.input_iphone_14_low_value("79000")
        self.input_iphone_14_high_value("90000")
        self.click_iphone_14_use()
        time.sleep(2)
        self.click_iphone_14_cart_page()


