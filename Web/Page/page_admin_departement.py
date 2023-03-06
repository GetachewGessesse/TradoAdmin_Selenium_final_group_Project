import time
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from Web.Locator.locators_admin_departement import locatorsAdmin


class Admin_page():

    def __init__(self, driver):
        self.driver = driver
        self.Department = locatorsAdmin.Department
        self.Search = locatorsAdmin.Search

        self.Icon_bar = locatorsAdmin.Icon_bar
        self.Add_button = locatorsAdmin.Add_button
        self.Add_name_button = locatorsAdmin.Add_name_button
        self.Add_name_insert = locatorsAdmin.Add_name_insert
        self.ADD_BUTTON = locatorsAdmin.ADD_BUTTON
        self.Add_image = locatorsAdmin.Add_image
        self.Exit_button = locatorsAdmin.Exit_button
        self.telphon = locatorsAdmin.telphon
        self.send_button = locatorsAdmin.send_button

        self.Interval_number = locatorsAdmin.Interval_number
        self.Interval_lower = locatorsAdmin.Interval_lower
        self.Interval_mid = locatorsAdmin.Interval_mid
        self.Interval_higher = locatorsAdmin.Interval_higher

        self.Sample_update_image_name = locatorsAdmin.Sample_update_image_name
        self.Update_name_place = locatorsAdmin.Update_name_place
        self.Update = locatorsAdmin.Update

        self.Telephone_field = locatorsAdmin.Telephone_field
        self.Send_code_button = locatorsAdmin.Send_code_button
        self.Code_field = locatorsAdmin.Code_field
        self.connection_button = locatorsAdmin.connection_button
        self.Admin_Login_phone = locatorsAdmin.Admin_Login_phone

    def open(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://qa-admin.trado.co.il/#/departments')
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)

    @allure.description('Enter phone number of admin')
    @pytest.mark.sanity
    def phone_number_inter(self, phoneno):
        self.driver.find_element(By.XPATH, self.Telephone_field).clear()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Telephone_field).send_keys(phoneno)
        time.sleep(2)

    def send_telphon_button(self):
        self.driver.find_element(By.XPATH, self.Send_code_button).click()
        time.sleep(2)

    @allure.description('Enter code number of admin')
    @pytest.mark.sanity
    def Code_number_inter(self, code):
        self.driver.find_element(By.XPATH, self.Code_field).clear()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Code_field).send_keys(code)
        time.sleep(3)
        self.driver.find_element(By.XPATH, self.connection_button).click()
        time.sleep(2)

    @allure.description('check search clickable')
    @pytest.mark.sanity
    def Search_clickable_check(self):
        self.driver.find_element(By.XPATH, self.Search).click()
        time.sleep(2)

    @allure.description('Navigat Qa admin website and open')
    @pytest.mark.sanity
    def admin_department(self):
        self.driver.find_element(By.XPATH, self.Department).click()
        time.sleep(3)

    @allure.description('Enter phone number of admin')
    @pytest.mark.sanity
    def search_enter_value(self, search):
        self.driver.find_element(By.XPATH, self.Search).clear()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Search).send_keys(search)
        time.sleep(2)


    @allure.description('Icone bar')
    @pytest.mark.sanity
    def Icon_bar_Add(self):
        self.driver.find_element(By.XPATH, self.Icon_bar).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Add_button).click()
        time.sleep(2)

    @allure.description('Icone bar')
    @pytest.mark.sanity
    def Icon_bar_Add_name_field(self,NEWNAME):

        self.driver.find_element(By.XPATH, self.Add_name_insert).clear()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Add_name_insert).send_keys(NEWNAME)
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.ADD_BUTTON).click()
        time.sleep(3)

    @allure.description('Icone bar')
    @pytest.mark.sanity
    def Icon_bar_Exit(self):
        self.driver.find_element(By.XPATH, self.Icon_bar).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Exit_button).click()
        time.sleep(2)

    @allure.description('Icone bar')
    @pytest.mark.sanity
    def Interval_bar_button(self):
        self.driver.find_element(By.XPATH, self.Interval_number).click()
        time.sleep(2)

    @allure.description('Icone bar')
    @pytest.mark.sanity
    def Interval_lower_20(self):
        self.driver.find_element(By.XPATH, self.Interval_lower).click()
        time.sleep(2)

    @allure.description('Icone bar higher')
    @pytest.mark.sanity
    def Interval_medium_50(self):
        self.driver.find_element(By.XPATH, self.Interval_mid).click()
        time.sleep(2)

    @allure.description('Icone bar higher')
    @pytest.mark.sanity
    def Interval_lower_200(self):
        self.driver.find_element(By.XPATH, self.Interval_higher).click()
        time.sleep(2)

    @allure.description('Icone bar higher')
    @pytest.mark.sanity
    def Sample_update_name(self, newName):
        self.driver.find_element(By.XPATH, self.Sample_update_image_name).click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Update_name_place).clear()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Update_name_place).send_keys(newName)
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.Update).click()
        time.sleep(2)
    @property
    def assertion_for_negative_search(self):
        return self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[2]").text






