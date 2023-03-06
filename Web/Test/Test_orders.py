import time
import allure
import pytest
from Web.Page.orders_page import Orders_page



class Test_Orders():

    @allure.description('Test if the orders page open')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_if_the_orders_page_open(self):
        Orders = Orders_page(self)
        Orders.open_website()
        Orders.click_on_Telephone_field('1950000000')                                                         #1 0000000
        Orders.click_on_Send_code_button()
        Orders.click_on_Code_field('1234')
        Orders.click_on_connection_button()
        Orders.click_on_orders()
        time.sleep(3)

    @allure.description('Test_if_the_detail_option_works')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_if_the_detail_option_works(self):
        Orders = Orders_page(self)
        Orders.open_website()
        Orders.click_on_Telephone_field('1950000000')                                                          #2  0000000
        Orders.click_on_Send_code_button()
        Orders.click_on_Code_field('1234')
        Orders.click_on_connection_button()
        Orders.click_on_orders()
        time.sleep(3)
        Orders.click_On_someone_order()
        time.sleep(2)

    @allure.description('Test if the drop menu icon open')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_if_the_drop_menu_icon_open(self):
        Orders = Orders_page(self)
        Orders.open_website()
        Orders.click_on_Telephone_field('1950000000')                                                             #3  00000000
        Orders.click_on_Send_code_button()
        Orders.click_on_Code_field('1234')
        Orders.click_on_connection_button()
        Orders.orders_click_on_icon_bar()
        time.sleep(3)

    @allure.description(' Test that the search box accepts input from the user.')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_orders_page(self):
        Orders = Orders_page(self)
        Orders.open_website()
        Orders.click_on_Telephone_field('1950000000')                                                            #4 000000000
        Orders.click_on_Send_code_button()
        Orders.click_on_Code_field('1234')
        Orders.click_on_connection_button()
        Orders.click_on_search_button_accept('milk')
        time.sleep(3)

    @allure.description('Check to insert existing products on search bar')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_orders_page(self):
        Orders = Orders_page(self)
        Orders.open_website()
        Orders.click_on_Telephone_field('1950000000')                                                                 #5  00000000
        Orders.click_on_Send_code_button()
        Orders.click_on_Code_field('1234')
        Orders.click_on_connection_button()
        Orders.click_on_search_button_accept('גורילה גלו')
        time.sleep(3)

    @allure.description('check  Check to insert non existing products on search bar ')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_orders_page(self):
        Orders = Orders_page(self)
        Orders.open_website()
        Orders.click_on_Telephone_field('1950000000')                                                                    #6 0000000
        Orders.click_on_Send_code_button()
        Orders.click_on_Code_field('1234')
        Orders.click_on_connection_button()
        Orders.click_on_search_button_accept('shfghdgfhghdhjghavds')
        time.sleep(3)

    @allure.description('check to search without inserting any products ')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_orders_page(self):
        Orders = Orders_page(self)
        Orders.open_website()
        Orders.click_on_Telephone_field('1950000000')                                                                  #7 0000000
        Orders.click_on_Send_code_button()
        Orders.click_on_Code_field('1234')
        Orders.click_on_connection_button()
        Orders.click_on_search_button_accept('')
        time.sleep(3)

    @allure.description('Check to insert numbers into the search box ')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_orders_page(self):
        Orders = Orders_page(self)
        Orders.open_website()
        Orders.click_on_Telephone_field('1950000000')                                                                   #8  00000000
        Orders.click_on_Send_code_button()
        Orders.click_on_Code_field('1234')
        Orders.click_on_connection_button()
        Orders.click_on_search_button_accept('45743885787548')
        time.sleep(3)

    @allure.description('Check  to search by inserting single letter')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_orders_page(self):
        Orders = Orders_page(self)
        Orders.open_website()
        Orders.click_on_Telephone_field('1950000000')                                                         #9 0000000
        Orders.click_on_Send_code_button()
        Orders.click_on_Code_field('1234')
        Orders.click_on_connection_button()
        Orders.click_on_search_button_accept('2')
        time.sleep(3)

    @allure.description('Check that the search functionality works correctly when multiple search terms are used.')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_orders_page(self):
        Orders = Orders_page(self)
        Orders.open_website()
        Orders.click_on_Telephone_field('1950000000')                                                           #10  000000
        Orders.click_on_Send_code_button()
        Orders.click_on_Code_field('1234')
        Orders.click_on_connection_button()
        Orders.click_on_search_button_accept('got millks')
        time.sleep(3)

    @allure.description('Check that the search functionality works correctly when the search query is empty')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_orders_page(self):
        Orders = Orders_page(self)
        Orders.open_website()
        Orders.click_on_Telephone_field('1950000000')                                                             #11 0000000
        Orders.click_on_Send_code_button()
        Orders.click_on_Code_field('1234')
        Orders.click_on_connection_button()
        Orders.click_on_search_button_accept('')
        time.sleep(3)

    @allure.description('Check the search functionality by entering an invalid search term and verifying that no results are displayed')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_orders_page(self):
        Orders = Orders_page(self)
        Orders.open_website()
        Orders.click_on_Telephone_field('1950000000')                                                               #12 0000000
        Orders.click_on_Send_code_button()
        Orders.click_on_Code_field('1234')
        Orders.click_on_connection_button()
        Orders.click_on_search_button_accept('miklzxtcg')
        time.sleep(3)

    @allure.description('Check to enter a search term with special characters and verify that the correct results are displayed.')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_orders_page(self):
        Orders = Orders_page(self)
        Orders.open_website()
        Orders.click_on_Telephone_field('1950000000')                                                                 #13 0000000
        Orders.click_on_Send_code_button()
        Orders.click_on_Code_field('1234')
        Orders.click_on_connection_button()
        Orders.click_on_search_button_accept('@#$5')
        time.sleep(3)

    @allure.description('Check to search multiple words.')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_orders_page(self):
        Orders = Orders_page(self)
        Orders.open_website()
        Orders.click_on_Telephone_field('1950000000')                                                                   #14  0000000
        Orders.click_on_Send_code_button()
        Orders.click_on_Code_field('1234')
        Orders.click_on_connection_button()
        Orders.click_on_search_button_accept('milk milk')
        time.sleep(3)

    @allure.description('Check that the search functionality works as expected when the search term is a misspelling.')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_orders_page(self):
        Orders = Orders_page(self)
        Orders.open_website()
        Orders.click_on_Telephone_field('1950000000')                                                                   #15 0000000
        Orders.click_on_Send_code_button()
        Orders.click_on_Code_field('1234')
        Orders.click_on_connection_button()
        Orders.click_on_search_button_accept('milk goa')
        time.sleep(3)

    @allure.description('Test the search functionality by searching for a term with uppercase letters.')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_orders_page(self):
        Orders = Orders_page(self)
        Orders.open_website()
        Orders.click_on_Telephone_field('1950000000')                                                                   #16  0000000
        Orders.click_on_Send_code_button()
        Orders.click_on_Code_field('1234')
        Orders.click_on_connection_button()
        Orders.click_on_search_button_accept('MILK')
        time.sleep(3)

    @allure.description('Test the search functionality by searching for a term with lowercase letters.')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_orders_page(self):
        Orders = Orders_page(self)
        Orders.open_website()
        Orders.click_on_Telephone_field('1950000000')                                                                   #17  0000000
        Orders.click_on_Send_code_button()
        Orders.click_on_Code_field('1234')
        Orders.click_on_connection_button()
        Orders.click_on_search_button_accept('milkgoat')
        time.sleep(3)

    @allure.description('Test the search functionality by searching for a term with a mix of upper and lower case letters.')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_orders_page(self):
        Orders = Orders_page(self)
        Orders.open_website()
        Orders.click_on_Telephone_field('1950000000')                                                                   #18 0000000
        Orders.click_on_Send_code_button()
        Orders.click_on_Code_field('1234')
        Orders.click_on_connection_button()
        Orders.click_on_search_button_accept('CHArger')
        time.sleep(3)

    @allure.description('Check the next button is functional.')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_orders_page(self):
        Orders = Orders_page(self)
        Orders.open_website()
        Orders.click_on_Telephone_field('1950000000')                                                                  #19 0000000
        Orders.click_on_Send_code_button()
        Orders.click_on_Code_field('1234')
        Orders.click_on_connection_button()
        Orders.orders_click_on_single_previus_arrow()
        time.sleep(3)


    @allure.description('Check the page number is clicable.')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_orders_page(self):
        Orders = Orders_page(self)
        Orders.open_website()
        Orders.click_on_Telephone_field('1950000000')                                                                 #20 000000
        Orders.click_on_Send_code_button()
        Orders.click_on_Code_field('1234')
        Orders.click_on_connection_button()
        Orders.orders_click_on_interval_number()
        time.sleep(3)
        Orders.orders_click_on_Interval_lower()
        time.sleep(3)
        Orders.orders_click_on_Interval_mid()
        time.sleep(3)
        Orders.orders_click_on_Interval_mid()
        time.sleep(3)
        Orders.orders_click_on_Interval_higher()
        time.sleep(3)

    @allure.description('Check the single next arrow takes you to the next page.')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_orders_page(self):
        Orders = Orders_page(self)
        Orders.open_website()
        Orders.click_on_Telephone_field('1950000000')                                                                  #21 0000000
        Orders.click_on_Send_code_button()
        Orders.click_on_Code_field('1234')
        Orders.click_on_connection_button()
        Orders.orders_click_on_single_next_arrow()
        time.sleep(3)

    @allure.description('Check the double next arrow takes you to the last page')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_orders_page(self):
        Orders = Orders_page(self)
        Orders.open_website()
        Orders.click_on_Telephone_field('1950000000')                                                                  #22 0000000
        Orders.click_on_Send_code_button()
        Orders.click_on_Code_field('1234')
        Orders.click_on_connection_button()
        Orders.orders_click_on_double_next_arrow()
        time.sleep(3)

    @allure.description('Check the double back arrow takes you to the first page.')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_orders_page(self):
        Orders = Orders_page(self)
        Orders.open_website()
        Orders.click_on_Telephone_field('1950000000')                                                                   #23 0000000
        Orders.click_on_Send_code_button()
        Orders.click_on_Code_field('1234')
        Orders.click_on_connection_button()
        Orders.orders_click_on_double_back_arrow()
        time.sleep(3)

    @allure.description('Check the single previues arrow takes you to the previeus page.')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_orders_page(self):
        Orders = Orders_page(self)
        Orders.open_website()
        Orders.click_on_Telephone_field('1950000000')                                                                   #24 00000000
        Orders.click_on_Send_code_button()
        Orders.click_on_Code_field('1234')
        Orders.click_on_connection_button()
        Orders.click_on_orders()
        time.sleep(3)

    @allure.description('Test if the ready bar page open')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_orders_page(self):
        Orders = Orders_page(self)
        Orders.open_website()
        Orders.click_on_Telephone_field('1950000000')                                                                  #25 00000000
        Orders.click_on_Send_code_button()
        Orders.click_on_Code_field('1234')
        Orders.click_on_connection_button()
        Orders.click_on_ready()
        time.sleep(3)

    @allure.description('Test if the finished bar page open')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_orders_page(self):
        Orders = Orders_page(self)
        Orders.open_website()
        Orders.click_on_Telephone_field('1950000000')                                                                    #26 00000000
        Orders.click_on_Send_code_button()
        Orders.click_on_Code_field('1234')
        Orders.click_on_connection_button()
        Orders.click_on_finished()
        time.sleep(3)

    @allure.description('Test if the in shiping bar page open')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_orders_page(self):
        Orders = Orders_page(self)
        Orders.open_website()
        Orders.click_on_Telephone_field('1950000000')                                                                    #27  0000000000
        Orders.click_on_Send_code_button()
        Orders.click_on_Code_field('1234')
        Orders.click_on_connection_button()
        Orders.click_on_in_shiping()
        time.sleep(3)

    @allure.description('Test if the received orders bar page open')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_orders_page(self):
        Orders = Orders_page(self)
        Orders.open_website()
        Orders.click_on_Telephone_field('1950000000')                                                                     #28 0000000000
        Orders.click_on_Send_code_button()
        Orders.click_on_Code_field('1234')
        Orders.click_on_connection_button()
        Orders.click_received_orders()
        time.sleep(3)

    @allure.description('check if it can display all details about orders when clicking at the person who registered')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_orders_page(self):
        Orders = Orders_page(self)
        Orders.open_website()
        Orders.click_on_Telephone_field('1950000000')                                                                    #29  00000000000
        Orders.click_on_Send_code_button()
        Orders.click_on_Code_field('1234')
        Orders.click_on_connection_button()
        Orders.click_on_orders()
        time.sleep(3)
        Orders.click_On_someone_order()
        time.sleep(3)
        Orders.click_on_email()
        time.sleep(3)

    @allure.description('Check the page number 1 is clicable.')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_orders_page(self):
        Orders = Orders_page(self)
        Orders.open_website()
        Orders.click_on_Telephone_field('1950000000')                                                                    #30 00000000
        Orders.click_on_Send_code_button()
        Orders.click_on_Code_field('1234')
        Orders.click_on_connection_button()
        Orders.click_page_number_1()
        time.sleep(3)

    @allure.description('Check the page number 2 is clicable')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_orders_page(self):
        Orders = Orders_page(self)
        Orders.open_website()
        Orders.click_on_Telephone_field('1950000000')                                                                 #31 00000000000
        Orders.click_on_Send_code_button()
        Orders.click_on_Code_field('1234')
        Orders.click_on_connection_button()
        Orders.click_page_number_2()
        time.sleep(3)

    @allure.description('Check the page number 3 is clicable')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_orders_page(self):
        Orders = Orders_page(self)
        Orders.open_website()
        Orders.click_on_Telephone_field('1950000000')                                                                  #32 0000000000
        Orders.click_on_Send_code_button()
        Orders.click_on_Code_field('1234')
        Orders.click_on_connection_button()
        Orders.click_page_number_3()
        time.sleep(3)

    @allure.description('Test if the first user is clickable')
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.regression
    def test_orders_page(self):
        Orders = Orders_page(self)
        Orders.open_website()
        Orders.click_on_Telephone_field('1950000000')                                                                    #33 00000000
        Orders.click_on_Send_code_button()
        Orders.click_on_Code_field('1234')
        Orders.click_on_connection_button()
        Orders.click_on_orders()
        time.sleep(3)
        Orders.click_On_someone_order()
        time.sleep(3)




