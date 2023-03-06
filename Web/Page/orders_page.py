import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support.select import Select
from Web.Locator.orders_locators import locatorsAdmin


class Orders_page():

    def __init__(self, driver):
        self.driver = driver
        self.website = locatorsAdmin.website
        self.orders_click_on_orders_button = locatorsAdmin.Orders
        self.orders_click_on_search_bar = locatorsAdmin.Search
        self.orders_click_on_icon_bar = locatorsAdmin.Icon_bar
        self.orders_click_on_exit_button = locatorsAdmin.Exit_button
        self.orders_click_on_interval_number = locatorsAdmin. Interval_number
        self.orders_click_on_Interval_lower = locatorsAdmin.Interval_lower
        self.orders_click_on_Interval_mid = locatorsAdmin.Interval_mid
        self.orders_click_on_Interval_higher = locatorsAdmin.Interval_higher
        self.orders_click_on_Telephone_field = locatorsAdmin.Telephone_field
        self.orders_click_on_Send_code_button = locatorsAdmin.Send_code_button
        self.orders_click_on_Code_field = locatorsAdmin.Code_field
        self.orders_click_on_connection_button = locatorsAdmin.connection_button
        self.orders_click_on_Admin_Login_phone = locatorsAdmin.Admin_Login_phone
        self.orders_click_on_someone_order = locatorsAdmin.someone_locator
        self.orders_click_on_in_shipping = locatorsAdmin.in_shipping
        self.orders_click_on_ready = locatorsAdmin.ready
        self.orders_click_on_finished = locatorsAdmin.finished
        self.orders_click_on_single_next_arrow = locatorsAdmin.single_next_arrow
        self.orders_click_on_single_previus_arrow =locatorsAdmin.single_previues_arrow
        self.orders_click_on_double_next_arrow = locatorsAdmin.double_next_arrow
        self.orders_click_on_double_back_arrow = locatorsAdmin.double_back_arrow
        self.orders_click_on_page_number_1 = locatorsAdmin.page_number_1
        self.orders_click_on_page_number_2 = locatorsAdmin.page_number_2
        self.orders_click_on_page_number_3 = locatorsAdmin.page_number_3
        self.orders_click_on_page_number_4 = locatorsAdmin.page_number_4
        self.orders_click_on_page_number_5 = locatorsAdmin.page_number_5
        self.orders_click_received_orders = locatorsAdmin.recieved_orders
        self.orders_click_on_email = locatorsAdmin.email

    @allure.step
    @allure.description('Navigate to qa.trado.co.il website')
    def open_website(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.website)
        self.driver.maximize_window()

    def click_on_orders(self):
        self.driver.find_element(By.XPATH, self.orders_click_on_orders_button).click()

    def click_on_search_button(self):
        self.driver.find_element(By.XPATH, self.orders_click_on_search_bar).click()

    def click_on_icon_button(self):
        self.driver.find_element(By.XPATH, self.orders_click_on_icon_bar).click()

    def click_on_exit_button(self):
        self.driver.find_element(By.XPATH, self.orders_click_on_exit_button).click()

    def click_on_interval_number(self):
        self.driver.find_element(By.XPATH, self.orders_click_on_interval_number).click()

    def click_on_Interval_lower(self):
        self.driver.find_element(By.XPATH, self.orders_click_on_Interval_lower).click()

    def click_on_Interval_mid(self):
        self.driver.find_element(By.XPATH, self.orders_click_on_Interval_mid).click()

    def click_on_Interval_higher(self):
        self.driver.find_element(By.XPATH, self.orders_click_on_Interval_higher).click()

    def click_on_Telephone_field(self, phone):
        time.sleep(4)
        self.driver.find_element(By.XPATH, self.orders_click_on_Telephone_field).clear()
        self.driver.find_element(By.XPATH, self.orders_click_on_Telephone_field).send_keys(phone)
        time.sleep(3)
    def click_on_Send_code_button(self):
        self.driver.find_element(By.XPATH, self.orders_click_on_Send_code_button).click()
        time.sleep(2)

    def click_on_Code_field(self, code):
        self.driver.find_element(By.XPATH, self.orders_click_on_Code_field).send_keys(code)
        time.sleep(2)

    def click_on_connection_button(self):
        self.driver.find_element(By.XPATH, self.orders_click_on_connection_button).click()
        time.sleep(2)

    def click_on_Admin_Login_phone(self):
        self.driver.find_element(By.XPATH, self.orders_click_on_Admin_Login_phone).click()

        time.sleep(2)

    def click_On_someone_order(self):
        self.driver.find_element(By.XPATH, self.orders_click_on_someone_order).click()

        time.sleep(2)

    def click_on_search_button_accept(self, string):
        self.driver.find_element(By.XPATH, self.orders_click_on_search_bar).clear()
        self.driver.find_element(By.XPATH, self.orders_click_on_search_bar).sendkeys(string)
        time.sleep(2)

    def click_on_in_shiping(self):
        self.driver.find_element(By.XPATH, self.orders_click_on_in_shiping).click()

        time.sleep(2)

    def click_on_ready(self):
        self.driver.find_element(By.XPATH, self.orders_click_on_ready).click()
        time.sleep(2)

    def click_on_finished(self):
        self.driver.find_element(By.XPATH, self.orders_click_on_finished).click()
        time.sleep(2)

    def click_single_next_arrow(self):
        self.driver.find_element(By.XPATH, self.orders_click_on_single_next_arrow).click()
        time.sleep(2)
    def click_single_previus_arrow(self):
        self.driver.find_element(By.XPATH, self.orders_click_on_single_previus_arrow).click()
        time.sleep(2)
    def click_double_next_arrow(self):
        self.driver.find_element(By.XPATH, self.orders_click_on_double_next_arrow).click()
        time.sleep(2)
    def click_double_back_arrow(self):
        self.driver.find_element(By.XPATH, self.orders_click_on_double_back_arrow).click()
        time.sleep(2)
    def click_page_number_1(self):
        self.driver.find_element(By.XPATH, self.orders_click_on_page_number_1).click()
        time.sleep(2)
    def click_page_number_2(self):
        self.driver.find_element(By.XPATH, self.orders_click_on_page_number_2).click()
        time.sleep(2)
    def click_page_number_3(self):
        self.driver.find_element(By.XPATH, self.orders_click_on_page_number_3).click()
        time.sleep(2)
    def click_page_number_4(self):
        self.driver.find_element(By.XPATH, self.orders_click_on_page_number_4).click()
        time.sleep(2)
    def click_page_number_5(self):
        self.driver.find_element(By.XPATH, self.orders_click_on_page_number_5).click()
        time.sleep(2)

    def click_received_orders(self):
        self.driver.find_element(By.XPATH, self.orders_click_received_orders).click()
        time.sleep(2)

    def click_on_email(self):
        self.driver.find_element(By.XPATH, self.orders_click_on_email).click()
        time.sleep(2)





