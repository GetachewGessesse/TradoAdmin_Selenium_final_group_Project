import requests
import allure
import pytest
from Server.API.Constants.constraint_search_product_admin import ConstraintProduct
class TestApiProductSearch:


    @allure.description('test_api ')
    @pytest.mark.sanity
    def test_api_existing_product(self):
        url = ConstraintProduct.url
        data = ConstraintProduct.valid_data_json
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api ')
    @pytest.mark.sanity
    def test_api_non_existing_product(self):
        url = ConstraintProduct.url
        data = ConstraintProduct.invalid_jason_non_exsting
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 400
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api ')
    @pytest.mark.sanity
    def test_api_with_special_characters(self):
        url = ConstraintProduct.url
        data = ConstraintProduct.invalid_special_characters
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 400
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api ')
    @pytest.mark.sanity
    def test_api_that_the_search_box_accepts_input_from_the_user(self):
        url = ConstraintProduct.url
        data = ConstraintProduct.input_from_the_user
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api ')
    @pytest.mark.sanity
    def test_to_insert_numbers_into_the_search_box(self):
        url = ConstraintProduct.url
        data = ConstraintProduct.number_from_the_user
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api ')
    @pytest.mark.sanity
    def test_to_search_without_inserting_any_products(self):
        url = ConstraintProduct.url
        data = ConstraintProduct.empty_item_from_the_user
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 400
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api ')
    @pytest.mark.sanity
    def test_to_search_by_inserting_the_single_letter(self):
        url = ConstraintProduct.url
        data = ConstraintProduct.single_letter
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api ')
    @pytest.mark.sanity
    def test_that_the_search_results_are_sorted_correctly(self):
        url = ConstraintProduct.url
        data = ConstraintProduct.sorting_products
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api ')
    @pytest.mark.sanity
    def test_that_the_search_functionality_works_correctly_when_multiple_search_terms_are_used(self):
        url = ConstraintProduct.url
        data = ConstraintProduct.multiple_products
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 400
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api ')
    @pytest.mark.sanity
    def test_to_search_multiple_words(self):
        url = ConstraintProduct.url
        data = ConstraintProduct.repeated_letters
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 400
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api ')
    @pytest.mark.sanity
    def test_that_the_search_results_are_displayed_correctly_on_the_page(self):
        url = ConstraintProduct.url
        data = ConstraintProduct.display_correctly
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api ')
    @pytest.mark.sanity
    def test_that_the_search_functionality_by_searching_for_a_term_with_uppercase_letters(self):
        url = ConstraintProduct.url
        data = ConstraintProduct.upper_case
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api ')
    @pytest.mark.sanity
    def test_that_the_search_functionality_by_searching_for_a_term_with_lowercase_letters(self):
        url = ConstraintProduct.url
        data = ConstraintProduct.lower_case
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api ')
    @pytest.mark.sanity
    def test_that_the_search_functionality_by_searching_for_a_term_with_lowercase_and_uppercase_letters(self):
        url = ConstraintProduct.url
        data = ConstraintProduct.lower_and_upper_case
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 10


    @allure.description('test_api ')
    @pytest.mark.sanity
    def test_that_the_search_functionality_by_searching_for_a_term_with_lowercase_and_uppercase_letters(self):
        url = ConstraintProduct.url
        data = ConstraintProduct.lower_and_upper_case
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api ')
    @pytest.mark.sanity
    def test_that_the_search_functionality_by_searching_for_a_term_with_uppercase_letters(self):
        url = ConstraintProduct.url
        data = ConstraintProduct.upper_case
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api ')
    @pytest.mark.sanity
    def test_that_the_search_functionality_by_searching_for_a_term_with_lowercase_letters(self):
        url = ConstraintProduct.url
        data = ConstraintProduct.lower_case
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api ')
    @pytest.mark.sanity
    def test_search_functionality_by_searching_for_a_term_with_lowercase_and_uppercase_letters(self):
        url = ConstraintProduct.url
        data = ConstraintProduct.lower_and_upper_case
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 200
        assert response.elapsed.total_seconds() < 10

    @allure.description('test_api ')
    @pytest.mark.sanity
    def test_that_the_search_functionality_by_searching_for_a_term_with_lowercase_and_uppercase_and_special_characters(self):
        url = ConstraintProduct.url
        data = ConstraintProduct.lower_and_upper_case
        response = requests.post(url, data)
        response.json()
        assert response.status_code == 400
        assert response.elapsed.total_seconds() < 10












