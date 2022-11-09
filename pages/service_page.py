import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base

class Service_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Locators"""
    service_centers = "//h4[@class='s-item__title']"
    alfa_card = "//html/body/div[2]/div[8]/div[2]/a[2]/div[2]/h4"
    loans = "//html/body/div[2]/div[8]/div[2]/a[3]/div[2]/h4"
    loans_sbr = "//html/body/div[2]/div[8]/div[2]/a[4]/div[2]/h4"
    delivery = "//html/body/div[2]/div[8]/div[2]/a[5]/div[2]/h4"
    present = "//html/body/div[2]/div[8]/div[2]/a[6]/div[2]/h4"
    trade_in = "//html/body/div[2]/div[8]/div[2]/a[7]/div[2]/h4"
    buy_product = "//html/body/div[2]/div[8]/div[2]/a[8]/div[2]/h4"
    insurance = "//html/body/div[2]/div[8]/div[2]/a[9]/div[2]/h4"

    def get_service_centers(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.service_centers)))

    def get_alfa_card(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.alfa_card)))

    def get_loans(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.loans)))

    def get_loans_sbr(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.loans_sbr)))

    def get_delivery(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.delivery)))

    def get_present(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.present)))

    def get_trade_in(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.trade_in)))

    def get_buy_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.buy_product)))

    def get_insurance(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.insurance)))

    def service_page_check(self):
        self.get_current_url()
        self.get_screenshot()
        self.assert_word(self.get_service_centers(), "Сервисные центры")
        self.assert_word(self.get_alfa_card(), "Карта от Альфа-Банка")
        self.assert_word(self.get_loans(), "Рассрочка и кредит")
        self.assert_word(self.get_loans_sbr(), "Рассрочка от СберБанка")
        self.assert_word(self.get_delivery(), "Доставка и оплата")
        self.assert_word(self.get_present(), "Подарочные сертификаты")
        self.assert_word(self.get_trade_in(), "Trade-in")
        self.assert_word(self.get_buy_product(), "Выкуп устройства")
        self.assert_word(self.get_insurance(), "Программы страхования вашей техники")




