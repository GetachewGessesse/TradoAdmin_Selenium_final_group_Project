import time
import pytest
from selenium.webdriver.common.by import By
from Web.Page.page_admin_departement import Admin_page
import allure


class Test_admin():

    @allure.description('log in admin with phone and passsword')
    @pytest.mark.sanity
    def test_admin_open_page(self):
        department_page = Admin_page(self)
        department_page.open()
        department_page.phone_number_inter('1950000000')
        department_page.send_telphon_button()
        department_page.Code_number_inter('1234')
        time.sleep(3)


    @allure.description('log in admin with phone and incorectpasssword')
    @pytest.mark.sanity
    def test_admin_incorrect_password_open_page(self):
        department_page = Admin_page(self)
        department_page.open()
        department_page.phone_number_inter('1950000000')
        department_page.send_telphon_button()
        time.sleep(3)
        department_page.Code_number_inter('2345')
        assertion_text = department_page.driver.find_element(By.XPATH, "//div[contains(text(),'faild to login')]").text
        assert assertion_text == "faild to login"
        time.sleep(3)


    @allure.description('log in admin with phone and incorectpasssword')
    @pytest.mark.sanity
    def test_admin_incorrect_pnoneNo_open_page(self):
        department_page = Admin_page(self)
        department_page.open()
        department_page.phone_number_inter('1953456758')
        department_page.send_telphon_button()
        time.sleep(3)
        department_page.Code_number_inter('1234')
        assertion_text = department_page.driver.find_element(By.XPATH,
                                                  "//body/div[@id='root']/div[1]/div[2]/div[1]/span[1]/form[1]/div[2]").text
        assert assertion_text == "no such user"
        time.sleep(3)

    @allure.description('Chech who we are link')
    @pytest.mark.sanity
    def test_admin_link_click(self):
        department_page = Admin_page(self)
        department_page.open()
        department_page.phone_number_inter('1950000000')
        department_page.send_telphon_button()
        department_page.Code_number_inter('1234')
        department_page.admin_department()

    @allure.description('verify search bar clickable')
    @pytest.mark.sanity
    def test_search_link_click(self):
        department_page = Admin_page(self)
        department_page.open()
        department_page.phone_number_inter('1950000000')
        department_page.send_telphon_button()
        department_page.Code_number_inter('1234')
        department_page.admin_department()
        department_page.Search_clickable_check()
        time.sleep(2)


    @allure.description('verify search bar send correct product name')
    @pytest.mark.sanity
    def test_search_enser_correct_product_name_click(self):
        department_page = Admin_page(self)
        department_page.open()
        department_page.phone_number_inter('1950000000')
        department_page.send_telphon_button()
        department_page.Code_number_inter('1234')
        department_page.admin_department()
        department_page.Search_clickable_check()
        department_page.search_enter_value('dawon')
        time.sleep(2)

    @allure.description('verify search bar send numbers')
    @pytest.mark.sanity
    def test_search_enser_link_click(self):
        department_page = Admin_page(self)
        department_page.open()
        department_page.phone_number_inter('1950000000')
        department_page.send_telphon_button()
        department_page.Code_number_inter('1234')
        department_page.admin_department()
        department_page.Search_clickable_check()
        department_page.search_enter_value('0000')
        time.sleep(2)

    @allure.description('verify search bar by send capital letter')
    @pytest.mark.sanity
    def test_search_by_single_Capital_letter_link_click(self):
        department_page = Admin_page(self)
        department_page.open()
        department_page.phone_number_inter('1950000000')
        department_page.send_telphon_button()
        department_page.Code_number_inter('1234')
        department_page.admin_department()
        department_page.Search_clickable_check()
        department_page.search_enter_value('B')
        time.sleep(2)

    @allure.description('verify search bar by send small letter')
    @pytest.mark.sanity
    def test_search_by_single_small_letter_link_click(self):
        department_page = Admin_page(self)
        department_page.open()
        department_page.phone_number_inter('1950000000')
        department_page.send_telphon_button()
        department_page.Code_number_inter('1234')
        department_page.admin_department()
        department_page.Search_clickable_check()
        department_page.search_enter_value('a')
        time.sleep(2)

    @allure.description('verify search bar null')
    @pytest.mark.sanity
    def test_search_empty_link_click(self):
        department_page = Admin_page(self)
        department_page.open()
        department_page.phone_number_inter('1950000000')
        department_page.send_telphon_button()
        department_page.Code_number_inter('1234')
        department_page.admin_department()
        department_page.Search_clickable_check()
        department_page.search_enter_value('')
        time.sleep(2)

    @allure.description('verify search bar letter and number mix')
    @pytest.mark.sanity
    def test_search_by_number_and_letter_link_click(self):
        department_page = Admin_page(self)
        department_page.open()
        department_page.phone_number_inter('1950000000')
        department_page.send_telphon_button()
        department_page.Code_number_inter('1234')
        department_page.admin_department()
        department_page.Search_clickable_check()
        department_page.search_enter_value('112rtya')
        time.sleep(2)

        assertion = department_page.assertion_for_negative_search
        assert "אין תוצאות" in assertion

    @allure.description('verify search bar number and letter mix')
    @pytest.mark.sanity
    def test_search_by_letter_and_number_link_click(self):
        department_page = Admin_page(self)
        department_page.open()
        department_page.phone_number_inter('1950000000')
        department_page.send_telphon_button()
        department_page.Code_number_inter('1234')
        department_page.admin_department()
        department_page.Search_clickable_check()
        department_page.search_enter_value('rtya2345')
        time.sleep(2)
        assertion = department_page.assertion_for_negative_search
        assert "אין תוצאות" in assertion

    @allure.description('verify search bar special characters')
    @pytest.mark.sanity
    def test_search_by_special_characters_link_click(self):
        department_page = Admin_page(self)
        department_page.open()
        department_page.phone_number_inter('1950000000')
        department_page.send_telphon_button()
        department_page.Code_number_inter('1234')
        department_page.admin_department()
        department_page.Search_clickable_check()
        department_page.search_enter_value('@@@@###')
        time.sleep(2)

    @allure.description('verify search bar special characters and number')
    @pytest.mark.sanity
    def test_search_by_special_characters_and_number_link_click(self):
        department_page = Admin_page(self)
        department_page.open()
        department_page.phone_number_inter('1950000000')
        department_page.send_telphon_button()
        department_page.Code_number_inter('1234')
        department_page.admin_department()
        department_page.Search_clickable_check()
        department_page.search_enter_value('@@@@@333333')
        time.sleep(2)
        assertion = department_page.assertion_for_negative_search
        assert "אין תוצאות" in assertion


    @allure.description('verify search bar by send name ')
    @pytest.mark.sanity
    def test_search_by_send_name_link_click(self):
        department_page = Admin_page(self)
        department_page.open()
        department_page.phone_number_inter('1950000000')
        department_page.send_telphon_button()
        department_page.Code_number_inter('1234')
        department_page.admin_department()
        department_page.Search_clickable_check()
        department_page.search_enter_value('tezu')
        time.sleep(2)
        assertion = department_page.assertion_for_negative_search
        assert "אין תוצאות" in assertion

    @allure.description('verify search bar by send capital letter')
    @pytest.mark.sanity
    def test_search_by_send_name_link_click(self):
        department_page = Admin_page(self)
        department_page.open()
        department_page.phone_number_inter('1950000000')
        department_page.send_telphon_button()
        department_page.Code_number_inter('1234')
        department_page.admin_department()
        department_page.Search_clickable_check()
        department_page.search_enter_value('alex')
        time.sleep(2)


    @allure.description('verify search bar special characters and number')
    @pytest.mark.sanity
    def test_search_by_special_letter_and_characters_link_click(self):
        department_page = Admin_page(self)
        department_page.open()
        department_page.phone_number_inter('1950000000')
        department_page.send_telphon_button()
        department_page.Code_number_inter('1234')
        department_page.admin_department()
        department_page.Search_clickable_check()
        department_page.search_enter_value('able2@@@@@')
        time.sleep(2)
        assertion = department_page.assertion_for_negative_search
        assert "אין תוצאות" in assertion

    @allure.description('verify search bar special characters and number')
    @pytest.mark.sanity
    def test_search_by_special_characters_and_letter_link_click(self):
        department_page = Admin_page(self)
        department_page.open()
        department_page.phone_number_inter('1950000000')
        department_page.send_telphon_button()
        department_page.Code_number_inter('1234')
        department_page.admin_department()
        department_page.Search_clickable_check()
        department_page.search_enter_value('@@@@#add')
        time.sleep(2)
        assertion = department_page.assertion_for_negative_search
        assert "אין תוצאות" in assertion

    @allure.description('Chech icon bar add')
    @pytest.mark.sanity
    def test_Icone_add_link_click(self):
        department_page = Admin_page(self)
        department_page.open()
        department_page.phone_number_inter('1950000000')
        department_page.send_telphon_button()
        department_page.Code_number_inter('1234')
        department_page.admin_department()
        department_page.Icon_bar_Add()

    @allure.description('Icone button')
    @pytest.mark.sanity
    def test_Icone_addName_link_click(self):
        department_page = Admin_page(self)
        department_page.open()
        department_page.phone_number_inter('1950000000')
        department_page.send_telphon_button()
        department_page.Code_number_inter('1234')
        department_page.admin_department()
        department_page.Icon_bar_Add()
        department_page.Icon_bar_Add_name_field('helloworld')

    @allure.description('verify if the Icon bar is avaliable')
    @pytest.mark.sanity
    def test_Icone_link_click(self):
        department_page = Admin_page(self)
        department_page.open()
        department_page.phone_number_inter('1950000000')
        department_page.send_telphon_button()
        department_page.Code_number_inter('1234')
        department_page.admin_department()
        department_page.Icon_bar_Exit()

    @allure.description('Interval numbers')
    @pytest.mark.sanity
    def test_Interval_link_click(self):
        department_page = Admin_page(self)
        department_page.open()
        department_page.phone_number_inter('1950000000')
        department_page.send_telphon_button()
        department_page.Code_number_inter('1234')
        department_page.admin_department()
        department_page.Interval_bar_button()

    @allure.description('Interval numbers lower')
    @pytest.mark.sanity
    def test_Interval_lower_link_click(self):
        department_page = Admin_page(self)
        department_page.open()
        department_page.phone_number_inter('1950000000')
        department_page.send_telphon_button()
        department_page.Code_number_inter('1234')
        department_page.admin_department()
        department_page.Interval_bar_button()
        department_page.Interval_lower_20()

    @allure.description('Interval numbers higher')
    @pytest.mark.sanity
    def test_Interval_medium_link_click(self):
        department_page = Admin_page(self)
        department_page.open()
        department_page.phone_number_inter('1950000000')
        department_page.send_telphon_button()
        department_page.Code_number_inter('1234')
        department_page.admin_department()
        department_page.Interval_bar_button()
        department_page.Interval_medium_50()

    @allure.description('Interval numbers higher')
    @pytest.mark.sanity
    def test_Interval_higher_link_click(self):
        department_page = Admin_page(self)
        department_page.open()
        department_page.phone_number_inter('1950000000')
        department_page.send_telphon_button()
        department_page.Code_number_inter('1234')
        department_page.admin_department()
        department_page.Interval_bar_button()
        department_page.Interval_lower_200()
        assertion_text =driver.find_element(By.XPATH, "//div[contains(text(),'200')]").text
        assert assertion_text == '200'

    @allure.description('Update name of department')
    @pytest.mark.sanity
    def test_update_name_image_link_click(self):
        department_page = Admin_page(self)
        department_page.open()
        department_page.phone_number_inter('1950000000')
        department_page.send_telphon_button()
        department_page.Code_number_inter('1234')
        department_page.admin_department()
        department_page.Sample_update_name('belayalew')

    @allure.description('Update name of department')
    @pytest.mark.sanity
    def test_update_name_image2_link_click(self):
        department_page = Admin_page(self)
        department_page.open()
        department_page.phone_number_inter('1950000000')
        department_page.send_telphon_button()
        department_page.Code_number_inter('1234')
        department_page.admin_department()
        department_page.Sample_update_name('bela123456')
