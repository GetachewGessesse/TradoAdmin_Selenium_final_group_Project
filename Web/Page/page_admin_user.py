import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

from Web.Locator.locator_admin_user import Admin_users_locators


class Admin_users_page():

    def __init__(self, driver):
        self.driver = driver
        self.website = Admin_users_locators.website
        self.user_page_xpath = Admin_users_locators.user_page_xpath
        self.detail_xpath = Admin_users_locators.detail_xpath
        self.drop_menu_xpath = Admin_users_locators.drop_menu_xpath
        self.drop_menu_add_xpath = Admin_users_locators.drop_menu_add_xpath
        self.drop_menu_export_xpath = Admin_users_locators.drop_menu_export_xpath
        self.list_xpath= Admin_users_locators.list_xpath
        self.next_page_xpath = Admin_users_locators.next_page_xpath
        self.fast_next_xpath = Admin_users_locators.fast_next_xpath
        self.user1_xpath = Admin_users_locators.user1_xpath
        self.search_box_xpath = Admin_users_locators.search_box_xpath
        self.language_xpath = Admin_users_locators.language_xpath
        self.option1_xpath = Admin_users_locators.option1_xpath
        self.option2_xpath = Admin_users_locators.option2_xpath
        self.login_button = Admin_users_locators.login_button
        self.click_xpath = Admin_users_locators.click_xpath
        self.search_button = Admin_users_locators.search_button




    @allure.step
    @allure.description('Navigate to trado Admin website')
    def open_admin_trado(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.website)
        self.driver.maximize_window()
        time.sleep(3)


    @allure.step
    @allure.description('click option1')
    def click_phone(self):
        self.driver.find_element(By.XPATH, self.option1_xpath).send_keys("1950000000")
        self.driver.find_element(By.XPATH, self.click_xpath).click()
        time.sleep(3)


    @allure.step
    @allure.description('click option2')
    def click_code(self):
        self.driver.find_element(By.XPATH, self.option2_xpath).send_keys("1234")
        self.driver.find_element(By.XPATH, self.login_button).click()
        time.sleep(3)


    @allure.step
    @allure.description('save button')
    def click_save_button(self):
        self.driver.find_element(By.XPATH, self.login_button).click()
        self.driver.implicitly_wait(10)

    @allure.step
    @allure.description('user page works')
    def click_on_user_page(self):
        self.driver.find_element(By.XPATH, self.user_page_xpath).click()
        time.sleep(3)

    @allure.step
    @allure.description('displaying detail page')
    def click_on_detail_page(self):
        self.driver.find_element(By.XPATH, self.detail_xpath).click()
        self.driver.implicitly_wait(10)

    @allure.step
    @allure.description('displaying drop menu')
    def click_on_drop_menu(self):
        self.driver.find_element(By.XPATH, self.drop_menu_xpath).click()
        self.driver.implicitly_wait(10)


    @allure.step
    @allure.description('add user')
    def click_on_drop_menu_add(self):
        self.driver.find_element(By.XPATH, self.drop_menu_add_xpath).click()
        self.driver.implicitly_wait(10)

    @allure.step
    @allure.description('exporting data')
    def click_on_drop_menu_export(self):
        self.driver.find_element(By.XPATH, self.drop_menu_export_xpath).click()
        self.driver.implicitly_wait(10)

    @allure.step
    @allure.description('clicking on list')
    def click_on_list(self):
        self.driver.find_element(By.XPATH, self.list_xpath).click()
        self.driver.implicitly_wait(10)



    @allure.step
    @allure.description('clicking on language')
    def click_on_language(self):
        self.driver.find_element(By.XPATH, self.language_xpath).click()
        self.driver.implicitly_wait(10)

    @allure.step
    @allure.description('clicking on user')
    def click_on_user(self):
        self.driver.find_element(By.XPATH, self.user1_xpath).click()
        self.driver.implicitly_wait(10)

    @allure.step
    @allure.description('clicking on search')
    def click_on_search(self):
        self.driver.find_element(By.XPATH, self.search_box_xpath).click()
        self.driver.implicitly_wait(10)

    @allure.step
    @allure.description('search existing user')
    def click_search_existing(self):
        self.driver.find_element(By.XPATH, self.search_box_xpath).send_keys("slamonnn")
        self.driver.find_element(By.XPATH, self.search_button).click()
        self.driver.implicitly_wait(10)

    @allure.step
    @allure.description('search non-existing user')
    def click_search_non_existing(self):
        self.driver.find_element(By.XPATH, self.search_box_xpath).send_keys("drake")
        self.driver.find_element(By.XPATH, self.search_button).click()
        self.driver.implicitly_wait(10)

    @allure.step
    @allure.description('search number')
    def click_search_number(self):
        self.driver.find_element(By.XPATH, self.search_box_xpath).send_keys("1234")
        self.driver.find_element(By.XPATH, self.search_button).click()
        self.driver.implicitly_wait(10)

    @allure.step
    @allure.description('search null')
    def click_search_null(self):
        self.driver.find_element(By.XPATH, self.search_box_xpath).send_keys("")
        self.driver.find_element(By.XPATH, self.search_button).click()
        self.driver.implicitly_wait(10)

    @allure.step
    @allure.description('search single character')
    def click_search_single_character(self):
        self.driver.find_element(By.XPATH, self.search_box_xpath).send_keys("a")
        self.driver.find_element(By.XPATH, self.search_button).click()
        self.driver.implicitly_wait(10)

    @allure.step
    @allure.description('search upper case')
    def click_search_upper_case(self):
        self.driver.find_element(By.XPATH, self.search_box_xpath).send_keys("AMAN")
        self.driver.find_element(By.XPATH, self.search_button).click()
        self.driver.implicitly_wait(10)

    @allure.step
    @allure.description('select 20 no')
    def select_20_users(self):
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]/div[1]/input[1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]/div[2]/div[1]/div[1]").click()
        time.sleep(2)

    @allure.step
    @allure.description('select 50 no')
    def select_50_users(self):
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]/div[1]/input[1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]/div[2]/div[1]/div[2]").click()
        time.sleep(2)



    @allure.step
    @allure.description('select 100 no')
    def select_100_users(self):
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]/div[1]/input[1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "// div[contains(text(), '100')]").click()
        time.sleep(2)

    @allure.step
    @allure.description('next list')
    def select_next_list(self):
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]/div[1]/input[1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]/div[2]/div[1]/div[1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.next_page_xpath).click()
        time.sleep(2)

    @allure.step
    @allure.description('fast next list')
    def select_fast_next_list(self):
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]/div[1]/input[1]").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[2]/div[1]/div[1]/span[1]/div[2]/div[1]/div[1]").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, self.fast_next_xpath).click()
        self.driver.implicitly_wait(10)










    @property
    @allure.step
    @allure.description('verify the admin page displayed')
    def admin_assertion(self):
        return self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/span[1]/form[1]/div[1]/div[1]/label[1]").text

    @property
    @allure.step
    @allure.description('verify if the trado page views')
    def trado_page_assertion(self):
        return self.driver.find_element(By.TAG_NAME, "h4").text

    @property
    @allure.step
    @allure.description('verify if the trado user displayed')
    def trado_user_assertion(self):
        return self.driver.find_element(By.TAG_NAME, "h4").text

    @property
    @allure.step
    @allure.description('verify if the drop box views')
    def drop_box_assertion(self):
        return self.driver.find_element(By.XPATH, "//span[contains(text(),'הוספה')]").text

    @property
    @allure.step
    @allure.description('verify if the user adding displayed ')
    def add_user_assertion(self):
        return self.driver.find_element(By.XPATH, "//span[contains(text(),'משתמש מערכת')]").text


    @property
    @allure.step
    @allure.description('verify if the user list is displayed ')
    def list_no_assertion(self):
        return self.driver.find_element(By.XPATH, "//div[contains(text(),'הכל')]").text

    @property
    @allure.step
    @allure.description('verify if the user list next slide is displayed ')
    def list_next_assertion(self):
        return self.driver.find_element(By.XPATH, "//tbody/tr[1]/td[1]").text

    @property
    @allure.step
    @allure.description('verify if the user list fast next slide is displayed ')
    def list_fast_next_assertion(self):
        return self.driver.find_element(By.XPATH, "//div[contains(text(),'amazon')]").text

    @property
    @allure.step
    @allure.description('verify if the language is changed ')
    def language_assertion(self):
        return self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[2]/div[1]/nav[1]/div[1]/div[1]/span[2]").text

    @property
    @allure.step
    @allure.description('verify if the user is displayed ')
    def user_check_assertion(self):
        return self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[4]/div[1]/div[1]/form[1]/div[1]/div[1]/label[1]").text

    @property
    @allure.step
    @allure.description('verify if the user is displayed ')
    def check_search_assertion(self):
        return self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[1]/span[1]/span[1]/div[1]/input[1]").text

    @property
    @allure.step
    @allure.description('verify if the existing user is displayed ')
    def check_search_existing_assertion(self):
        return self.driver.find_element(By.XPATH, "//tbody/tr/td[3]").text


    @property
    @allure.step
    @allure.description('verify if the existing user is displayed ')
    def check_search_non_existing_assertion(self):
        return self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[2]/div[2]").text

    @property
    @allure.step
    @allure.description('verify if the number is displayed ')
    def check_search_number_assertion(self):
        return self.driver.find_element(By.XPATH, "// tbody / tr / td[4]").text

    @property
    @allure.step
    @allure.description('verify if the single character is displayed ')
    def check_single_character_assertion(self):
        return self.driver.find_element(By.XPATH, "// tbody / tr[1] / td[1]").text

    @property
    @allure.step
    @allure.description('verify if the upper case is displayed ')
    def check_upper_case_assertion(self):
        return self.driver.find_element(By.XPATH, "//body/div[@id='root']/div[1]/div[2]/main[1]/div[2]/div[1]/div[2]/div[2]/div[2]").text

    

