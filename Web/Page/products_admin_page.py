import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from Web.Locator.products_admin_locators import AdminProductLocators
import allure


class ProductAdmin():

    def __init__(self, driver):
        self.driver = driver
        self.url = AdminProductLocators.website
        self.phone_xpath = AdminProductLocators.phone_xpath
        self.send_code_button = AdminProductLocators.click_xpath
        self.code_field_xpath = AdminProductLocators.code_xpath
        self.login_btn_xpath = AdminProductLocators.login_button
        self.product_button_xpath = AdminProductLocators.product_button_xpath
        self.single_next_arrow_xpath = AdminProductLocators.single_next_arrow_xpath
        self.double_next_arrow_xpath = AdminProductLocators.double_next_arrow_xpath
        self.double_back_arrow_xpath = AdminProductLocators.double_back_arrow_xpath
        self. amount_Display = AdminProductLocators.amount_Display
        self.add_xpath = AdminProductLocators.add_xpath
        self.add_product_xpath = AdminProductLocators.add_product_xpath
        self.us_language_xpath = AdminProductLocators.us_language_xpath
        self.Il_language_xpath = AdminProductLocators.Il_language_xpath
        self.product_search_xpath = AdminProductLocators.product_search_xpath
        self.bar_code_xpath = AdminProductLocators.bar_code_xpath
        self.name_xpath = AdminProductLocators.name_xpath
        self.price_xpath = AdminProductLocators.price_xpath
        self.date_xpath = AdminProductLocators.date_xpath
        self.description_xpath = AdminProductLocators.description_xpath
        self. next_xpath = AdminProductLocators.next_xpath


    def open_trado_admin(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(6)

    def click_phone(self):
        self.driver.find_element(By.XPATH, self.phone_xpath).send_keys("1950000000")
        self.driver.find_element(By.XPATH, self.send_code_button).click()
        time.sleep(2)
    def click_code(self):
        self.driver.find_element(By.XPATH, self.code_field_xpath).send_keys("1234")
        self.driver.find_element(By.XPATH, self.login_btn_xpath).click()
        self.driver.implicitly_wait(10)

    def click_product_option(self):
        self.driver.find_element(By.XPATH, self.product_button_xpath).click()
        self.driver.find_element(By.XPATH, self.add_xpath).click()
        self.driver.find_element(By.XPATH, self.add_product_xpath).click()
        self.driver.find_element(By.XPATH, self.product_search_xpath).send_keys("temmm")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.bar_code_xpath).send_keys("1234")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.name_xpath).send_keys("milk")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.price_xpath).send_keys("20")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.date_xpath).send_keys("21/12/2023")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.description_xpath).send_keys("hvjfbfkllkkllkkbkll")
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.next_xpath).click()
        time.sleep(2)



    def click_single_next_arrow(self):
        self.driver.find_element(By.XPATH, self.single_next_arrow_xpath).click()
        time.sleep(2)

    def click_double_next_arrow(self):
        self.driver.find_element(By.XPATH, self.double_next_arrow_xpath).click()
        time.sleep(2)

    def click_double_back_arrow(self):
        self.driver.find_element(By.XPATH, self.double_back_arrow_xpath).click()
        time.sleep(2)

    def click_amount_display(self):
        self.driver.find_element(By.XPATH, self.amount_Display).click()
        self.driver.find_element(By.XPATH, self.amount_Display).click()
        time.sleep(2)

    def click_add_product(self):
        self.driver.find_element(By.XPATH, self.product_button_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.add_xpath).click()
        time.sleep(4)

    def click_to_change_language(self):
        self.driver.find_element(By.XPATH, self.us_language_xpath).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Il_language_xpath).click()
        time.sleep(4)










