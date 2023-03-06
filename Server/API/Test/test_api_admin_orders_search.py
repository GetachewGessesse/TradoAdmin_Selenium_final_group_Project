import requests
import allure
import pytest
from Server.API.Constants.constant_api_admin_orders_search import ConstantSearchOrders


class TestApiOrdersSearch:

    @allure.description('test_api ')
    @pytest.mark.sanity
    def test_api_existing_product(self):
        url = ConstantSearchOrders.url
        data = ConstantSearchOrders.valid_data                                       #1
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api ')
    @pytest.mark.sanity
    def test_api_non_existing_product(self):
        url = ConstantSearchOrders.url
        data = ConstantSearchOrders.invalid_non_existing                               #2
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 400
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api ')
    @pytest.mark.sanity
    def test_api_speciaL_character_product(self):
        url = ConstantSearchOrders.url
        data = ConstantSearchOrders.invalid_special_character                             #3
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 400
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api ')
    @pytest.mark.sanity
    def test_api_null_search_bar(self):
        url = ConstantSearchOrders.url
        data = ConstantSearchOrders.null_search_bar                                        #4
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api ')
    @pytest.mark.sanity
    def test_api_insert_only_numbers(self):
        url = ConstantSearchOrders.url
        data = ConstantSearchOrders.insert_only_numbers                                      #5
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 400
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api ')
    @pytest.mark.sanity
    def test_api_insert_single_letter(self):
        url = ConstantSearchOrders.url
        data = ConstantSearchOrders.insert_single_letter                                        #6
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 400
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api ')
    @pytest.mark.sanity
    def test_api_search_multiple_words(self):
        url = ConstantSearchOrders.url
        data = ConstantSearchOrders.search_multiple_words                                         #7
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 400
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api ')
    @pytest.mark.sanity
    def test_api_misspeling_words(self):
        url = ConstantSearchOrders.url
        data = ConstantSearchOrders.misspeling_words                                                  #8
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 400
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api ')
    @pytest.mark.sanity
    def test_api_search_UPPERCASE_letter(self):
        url = ConstantSearchOrders.url
        data = ConstantSearchOrders.search_UPPERCASE_letter                                          #9
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api ')
    @pytest.mark.sanity
    def test_api_search_LOWER_case(self):
        url = ConstantSearchOrders.url
        data = ConstantSearchOrders.search_LOWER_case                                                #10
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api ')
    @pytest.mark.sanity
    def test_api_search_product_mix_UPPER_and_LOWER_case(self):
        url = ConstantSearchOrders.url
        data = ConstantSearchOrders.search_product_mix_UPPER_and_LOWER_case                               #11
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 400
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api ')
    @pytest.mark.sanity
    def test_api_search_mix_upper_lower_special_letter(self):
        url = ConstantSearchOrders.url
        data = ConstantSearchOrders.search_mix_upper_lower_special_letter                                    #12
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 400
        assert response.elapsed.total_seconds() < 10








