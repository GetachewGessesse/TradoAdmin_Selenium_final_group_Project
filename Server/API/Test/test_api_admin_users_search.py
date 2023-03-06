import requests
import allure
import pytest
from Server.API.Constants.constant_api_admin_users_search import Constantsearchusers


class TestApiOrdersSearch:

    @allure.description('test_api_existing_product')
    @pytest.mark.sanity
    def test_api_existing_product(self):
        url = Constantsearchusers.url
        data = Constantsearchusers.valid_data
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api_existing_product_2')
    @pytest.mark.sanity
    def test_api_existing_product_2(self):
        url = Constantsearchusers.url
        data = Constantsearchusers.valid_data
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 400
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api_non_existing_product')
    @pytest.mark.sanity
    def test_api_non_existing_product(self):
        url = Constantsearchusers.url
        data = Constantsearchusers.invalid_non_existing
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api_non_existing_product_2')
    @pytest.mark.sanity
    def test_api_non_existing_product_2(self):
        url = Constantsearchusers.url
        data = Constantsearchusers.invalid_non_existing
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 200
        assert response.elapsed.total_seconds() == 1

    @allure.description('test_api_special_character')
    @pytest.mark.sanity
    def test_api_special_character(self):
        url = Constantsearchusers.url
        data = Constantsearchusers.invalid_special_character
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api_special_character_2')
    @pytest.mark.sanity
    def test_api_special_character_2(self):
        url = Constantsearchusers.url
        data = Constantsearchusers.invalid_special_character
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 300
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api_null_search_bar')
    @pytest.mark.sanity
    def test_api_null_search_bar(self):
        url = Constantsearchusers.url
        data = Constantsearchusers.null_search_bar
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api_null_search_bar_2')
    @pytest.mark.sanity
    def test_api_null_search_bar_2(self):
        url = Constantsearchusers.url
        data = Constantsearchusers.null_search_bar
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 400
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api_insert_only_numbers')
    @pytest.mark.sanity
    def test_api_insert_only_numbers(self):
        url = Constantsearchusers.url
        data = Constantsearchusers.insert_only_numbers
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api_insert_only_numbers_2')
    @pytest.mark.sanity
    def test_api_insert_only_numbers_2(self):
        url = Constantsearchusers.url
        data = Constantsearchusers.insert_only_numbers
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 400
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api_insert_single_letter')
    @pytest.mark.sanity
    def test_api_insert_single_letter(self):
        url = Constantsearchusers.url
        data = Constantsearchusers.insert_single_letter
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api_insert_single_letter_2')
    @pytest.mark.sanity
    def test_api_insert_single_letter_2(self):
        url = Constantsearchusers.url
        data = Constantsearchusers.insert_single_letter
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 400
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api_search_multiple_words')
    @pytest.mark.sanity
    def test_api_search_multiple_words(self):
        url = Constantsearchusers.url
        data = Constantsearchusers.search_multiple_words
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api_search_multiple_words_2')
    @pytest.mark.sanity
    def test_api_search_multiple_words_2(self):
        url = Constantsearchusers.url
        data = Constantsearchusers.search_multiple_words
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 400
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api_search_miss_spelling_words')
    @pytest.mark.sanity
    def test_api_search_miss_spelling_words(self):
        url = Constantsearchusers.url
        data = Constantsearchusers.miss_spelling_words
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api_search_miss_spelling_words_2')
    @pytest.mark.sanity
    def test_api_search_miss_spelling_words_2(self):
        url = Constantsearchusers.url
        data = Constantsearchusers.miss_spelling_words
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 400
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api_search_UPPERCASE_letter')
    @pytest.mark.sanity
    def test_api_search_UPPERCASE_letter(self):
        url = Constantsearchusers.url
        data = Constantsearchusers.search_UPPERCASE_letter
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api_search_UPPERCASE_letter_2')
    @pytest.mark.sanity
    def test_api_search_UPPERCASE_letter_2(self):
        url = Constantsearchusers.url
        data = Constantsearchusers.search_UPPERCASE_letter
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 400
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api_search_LOWER_case r')
    @pytest.mark.sanity
    def test_api_search_LOWER_case(self):
        url = Constantsearchusers.url
        data = Constantsearchusers.search_LOWER_case
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api_search_LOWER_case_2')
    @pytest.mark.sanity
    def test_api_search_LOWER_case_2(self):
        url = Constantsearchusers.url
        data = Constantsearchusers.search_LOWER_case
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 400
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api_search_product_mix_UPPER_and_LOWER_case')
    @pytest.mark.sanity
    def test_api_search_product_mix_UPPER_and_LOWER_case(self):
        url = Constantsearchusers.url
        data = Constantsearchusers.search_product_mix_UPPER_and_LOWER_case
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api_search_product_mix_UPPER_and_LOWER_case_2')
    @pytest.mark.sanity
    def test_api_search_product_mix_UPPER_and_LOWER_case_2(self):
        url = Constantsearchusers.url
        data = Constantsearchusers.search_product_mix_UPPER_and_LOWER_case
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 400
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api_search_mix_upper_lower_special_letter')
    @pytest.mark.sanity
    def test_api_search_mix_upper_lower_special_letter(self):
        url = Constantsearchusers.url
        data = Constantsearchusers.search_mix_upper_lower_special_letter
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api_search_mix_upper_lower_special_letter_2')
    @pytest.mark.sanity
    def test_api_search_mix_upper_lower_special_letter_2(self):
        url = Constantsearchusers.url
        data = Constantsearchusers.search_mix_upper_lower_special_letter
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 400
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api_search_mix_upper_lower_special_letter_3')
    @pytest.mark.sanity
    def test_api_search_mix_upper_lower_special_letter_3(self):
        url = Constantsearchusers.url
        data = Constantsearchusers.search_mix_upper_lower_special_letter
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 200
        assert response.elapsed.total_seconds() == 1






