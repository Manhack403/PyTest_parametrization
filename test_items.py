import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Test_Diff_lang:
    def test_cart_button_different_lang(self, browser):

        browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
        time.sleep(30)
        search_for_add_to_cart_button = len(browser.find_elements(
            By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']"))
        assert search_for_add_to_cart_button > 0, 'There is no button'
