import time
import pytest as pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import  Options
from pages.start_page import Start_page
from pages.iphone_page import Iphone_page
from pages.iphone_14_page import Iphone_14_page
from pages.cart_page import Cart_page
from pages.basket_page import Basket_page

def test_buy_iphone_14():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='C:\\Users\\Dench\\Desktop\\Stepik\\Chrome\\chromedriver.exe', chrome_options=options)
    print("\nStart test")
    start = Start_page(driver)
    start.login()

    iphone_14 = Iphone_page(driver)
    iphone_14.selection()

    iphone_14_find = Iphone_14_page(driver)
    iphone_14_find.iphone_14_search()

    cart_iphone_14 = Cart_page(driver)
    cart_iphone_14.cart()

    basket_ip_14 = Basket_page(driver)
    basket_ip_14.basket()

    print("\nFinish Test ")
    # time.sleep(10)
    driver.quit()


