import time
import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import  Options

from pages.service_page import Service_page
from pages.start_page import Start_page
from pages.iphone_page import Iphone_page
from pages.iphone_14_page import Iphone_14_page
from pages.cart_page import Cart_page
from pages.basket_page import Basket_page

def test_store_services_14():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='C:\\Users\\Dench\\Desktop\\Stepik\\Chrome\\chromedriver.exe', chrome_options=options)
    print("\nStart test")
    start = Start_page(driver)
    start.start()

    service = Service_page(driver)
    service.service_page_check()





