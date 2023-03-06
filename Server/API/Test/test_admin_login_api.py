from Server.API.Constants.constant_admin_login_api import *
import requests


class TestLogin_API:
    # @allure.description('Login correctly')
    def test_admin_login_correctly(self):
        url = AdminLoginConstants.url
        data = AdminLoginConstants.valid_data
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 5



    def test_admin_login_phone_and_code_incorrectly(self):
        url = AdminLoginConstants.url
        data = AdminLoginConstants.invalid_phone_invalid_code
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 4
        assert res.elapsed.total_seconds() < 5



    def test_admin_login_phone_and_code_null(self):
        url = AdminLoginConstants.url
        data = AdminLoginConstants.phone_and_code_field_null
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5



    def test_admin_login_valid_phone_and_invalid_code(self):
        url = AdminLoginConstants.url
        data = AdminLoginConstants.valid_phone_and_invalid_code
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5



    def test_admin_login_invalid_phone_and_valid_code(self):
        url = AdminLoginConstants.url
        data = AdminLoginConstants.invalid_phone_and_valid_code
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5



    def test_admin_login_valid_phone_and_code_null(self):
        url = AdminLoginConstants.url
        data = AdminLoginConstants.valid_phone_and_code_null
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5



    def test_admin_login_phone_null_and_code_valid(self):
        url = AdminLoginConstants.url
        data = AdminLoginConstants.phone_null_code_valid
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5


    def test_admin_login_invalid_phone_and_code_null(self):
        url = AdminLoginConstants.url
        data = AdminLoginConstants.invalid_phone_code_null
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5



    def test_admin_login_phone_null_and_code_invalid(self):
        url = AdminLoginConstants.url
        data = AdminLoginConstants.phone_null_code_invalid
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5




    def test_admin_login_phone_longValue_code_valid(self):
        url = AdminLoginConstants.url
        data = AdminLoginConstants.phone_insert_longValue_and_code_valid
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5




    def test_admin_login_phone_shortValue_code_valid(self):
        url = AdminLoginConstants.url
        data = AdminLoginConstants.phone_insert_shortValue_and_code_valid
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5



    def test_admin_login_phone_longtValue_code_invalid(self):
        url = AdminLoginConstants.url
        data = AdminLoginConstants.phone_insert_longValue_and_code_invalid
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5




    def test_admin_login_phone_shorttValue_code_invalid(self):
        url = AdminLoginConstants.url
        data = AdminLoginConstants.phone_insert_longValue_and_code_invalid
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5




    def test_admin_login_phone_longtValue_code_null(self):
        url = AdminLoginConstants.url
        data = AdminLoginConstants.phone_insert_longValue_and_code_null
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5



    def test_admin_login_phone_shorttValue_code_null(self):
        url = AdminLoginConstants.url
        data = AdminLoginConstants.phone_insert_shortValue_and_code_null
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5



    def test_phone_valid_and_code_insert_longValue(self):
        url = AdminLoginConstants.url
        data = AdminLoginConstants.phone_valid_and_code_insert_longValue
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5




    def test_phone_valid_and_code_insert_shortValue(self):
        url = AdminLoginConstants.url
        data = AdminLoginConstants.phone_valid_and_code_insert_shortValue
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5




    def test_phone_null_and_code_insert_longValue(self):
        url = AdminLoginConstants.url
        data = AdminLoginConstants.phone_null_and_code_insert_longValue
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5



    def test_phone_null_and_code_insert_shortValue(self):
        url = AdminLoginConstants.url
        data = AdminLoginConstants.phone_null_and_code_insert_shortValue
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5



    def test_phone_invalid_and_code_insert_longValue(self):
        url = AdminLoginConstants.url
        data = AdminLoginConstants.phone_invalid_and_code_insert_longValue
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5




    def test_phone_invalid_and_code_insert_shortValue(self):
        url = AdminLoginConstants.url
        data = AdminLoginConstants.phone_invalid_and_code_insert_shortValue
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5



    def test_phone_and_code_both_insert_longValue(self):
        url = AdminLoginConstants.url
        data = AdminLoginConstants.phone_and_code_both_insert_longValue
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5




    def test_phone_and_code_both_insert_shortValue(self):
        url = AdminLoginConstants.url
        data = AdminLoginConstants.phone_and_code_both_insert_shortValue
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5



    def test_both_fields_insert_character(self):
        url = AdminLoginConstants.url
        data = AdminLoginConstants.both_fields_insert_character
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5




    def test_both_fields_insert_string_character_and(self):
        url = AdminLoginConstants.url
        data = AdminLoginConstants.both_fields_insert_character
        res = requests.post(url, data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5




