import time

import allure
import pytest
from Page.page_admin_user import Admin_users_page



class Test_Admin_page():

    @allure.description('Verify the website works ')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_admin_page_load(self):
        users = Admin_users_page(self)
        users.open_admin_trado()
        assertion_text = users.admin_assertion
        assert "טלפון*" == assertion_text

    @allure.description('Verify all the page opens ')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_admin_trado_page(self):
        users = Admin_users_page(self)
        users.open_admin_trado()
        users.click_phone()
        users.click_code()
        assertion_text = users.trado_page_assertion
        assert "דשבורד" == assertion_text



    @allure.description('Test if the users page open')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_user_page(self):
        users = Admin_users_page(self)
        users.open_admin_trado()
        users.click_phone()
        users.click_code()
        users.click_on_user_page()
        assertion_text = users.trado_user_assertion
        assert "משתמשי מערכת" == assertion_text


    @allure.description('Test if the detail option works')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_detail_page(self):
        users = Admin_users_page(self)
        users.open_admin_trado()
        users.click_phone()
        users.click_code()
        users.click_on_user_page()
        users.click_on_detail_page()
        assertion_text = users.trado_user_assertion
        assert "משתמשי מערכת" == assertion_text

    @allure.description('Test if the drop menu open')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_drop_menu(self):
        users = Admin_users_page(self)
        users.open_admin_trado()
        users.click_phone()
        users.click_code()
        users.click_on_user_page()
        users.click_on_drop_menu()
        assertion_text = users.drop_box_assertion
        assert "הוספה" == assertion_text

    @allure.description('Test if the drop menu clicks add')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_drop_menu_add(self):
        users = Admin_users_page(self)
        users.open_admin_trado()
        users.click_phone()
        users.click_code()
        users.click_on_user_page()
        users.click_on_drop_menu()
        users.click_on_drop_menu_add()
        assertion_text = users.add_user_assertion
        assert "משתמש מערכת" == assertion_text

    @allure.description('Test if the drop menu clicks export')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_drop_menu_export(self):
        users = Admin_users_page(self)
        users.open_admin_trado()
        users.click_phone()
        users.click_code()
        users.click_on_user_page()
        users.click_on_drop_menu()
        users.click_on_drop_menu_export()



    @allure.description('Test if the list no works')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_list_no(self):
        users = Admin_users_page(self)
        users.open_admin_trado()
        users.click_phone()
        users.click_code()
        users.click_on_user_page()
        users.click_on_list()
        assertion_text = users.list_no_assertion
        assert "הכל" == assertion_text

    @allure.description('Test if the list no "20" works')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_list_no_20(self):
        users = Admin_users_page(self)
        users.open_admin_trado()
        users.click_phone()
        users.click_code()
        users.click_on_user_page()
        users.select_20_users()



    @allure.description('Test if the list no "50" works')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_list_no_50(self):
        users = Admin_users_page(self)
        users.open_admin_trado()
        users.click_phone()
        users.click_code()
        users.click_on_user_page()
        users.select_50_users()



    @allure.description('Test if the list no "100" works')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_list_no_100(self):
        users = Admin_users_page(self)
        users.open_admin_trado()
        users.click_phone()
        users.click_code()
        users.click_on_user_page()
        users.select_100_users()

    @allure.description('Test if the next slide list displays')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_next_list(self):
        users = Admin_users_page(self)
        users.open_admin_trado()
        users.click_phone()
        users.click_code()
        users.click_on_user_page()
        users.select_next_list()
        assertion_text = users.list_next_assertion
        assert "XKNUI" == assertion_text

    @allure.description('Test if the fast next slide list displays')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_fast_next_list(self):
        users = Admin_users_page(self)
        users.open_admin_trado()
        users.click_phone()
        users.click_code()
        users.click_on_user_page()
        users.select_fast_next_list()
        assertion_text = users.list_fast_next_assertion
        assert "amazon" == assertion_text

    @allure.description('Test if the english language changes')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_language(self):
        users = Admin_users_page(self)
        users.open_admin_trado()
        users.click_phone()
        users.click_code()
        users.click_on_user_page()
        users.click_on_language()
        assertion_text = users.language_assertion
        assert "Hello slamonnn" == assertion_text

    @allure.description('Test if the first user is clickable')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_user1(self):
        users = Admin_users_page(self)
        users.open_admin_trado()
        users.click_phone()
        users.click_code()
        users.click_on_user_page()
        users.click_on_user()
        assertion_text = users.user_check_assertion
        assert "שם פרטי*" == assertion_text

    @allure.description('Test if the search bar is clickable')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_search_bar(self):
        users = Admin_users_page(self)
        users.open_admin_trado()
        users.click_phone()
        users.click_code()
        users.click_on_user_page()
        users.click_on_search()
        assertion_text = users.check_search_assertion
        assert "" == assertion_text


    @allure.description('Test if the search existing user works')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_search_bar_existing(self):
        users = Admin_users_page(self)
        users.open_admin_trado()
        users.click_phone()
        users.click_code()
        users.click_on_user_page()
        users.click_search_existing()
        assertion_text = users.check_search_existing_assertion
        assert "salmon@gmail.com" == assertion_text

    @allure.description('Test if the search existing user works')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_search_bar_non_existing(self):
        users = Admin_users_page(self)
        users.open_admin_trado()
        users.click_phone()
        users.click_code()
        users.click_on_user_page()
        users.click_search_non_existing()
        assertion_text = users.check_search_non_existing_assertion
        assert "סה״כ: 0 שורות" in assertion_text

    @allure.description('Test if the search number works')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_search_bar_number(self):
        users = Admin_users_page(self)
        users.open_admin_trado()
        users.click_phone()
        users.click_code()
        users.click_on_user_page()
        users.click_search_number()
        assertion_text = users.check_search_number_assertion
        assert "1234567894" in assertion_text

    @allure.description('Test if the search null works')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_search_bar_null(self):
        users = Admin_users_page(self)
        users.open_admin_trado()
        users.click_phone()
        users.click_code()
        users.click_on_user_page()
        users.click_search_null()


    @allure.description('Test if the search null works')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_search_bar_single_character(self):
        users = Admin_users_page(self)
        users.open_admin_trado()
        users.click_phone()
        users.click_code()
        users.click_on_user_page()
        users.click_search_single_character()
        assertion_text = users.check_single_character_assertion
        assert "" == assertion_text

    @allure.description('Test if the search upper case works')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_search_bar_upper_case(self):
        users = Admin_users_page(self)
        users.open_admin_trado()
        users.click_phone()
        users.click_code()
        users.click_on_user_page()
        users.click_search_upper_case()
        assertion_text = users.check_upper_case_assertion
        assert "סה״כ: 0 שורות" == assertion_text






