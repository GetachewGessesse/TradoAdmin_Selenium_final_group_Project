import pytest
from Web.Page.products_admin_page import ProductAdmin
import time
import allure

class TestProductAdmin:

    @allure.description('open_trado_admin')
    @pytest.mark.sanity
    def test_open_trado_admin(self):
        product = ProductAdmin(self)
        product.open_trado_admin()
        product.click_phone()
        product.click_code()

    @allure.description('test_click_product_option')
    @pytest.mark.sanity
    def test_click_product_option(self):
        product = ProductAdmin(self)
        product.open_trado_admin()
        product.click_phone()
        product.click_code()
        product.click_product_option()

    @allure.description('test_the_next_arrow_clickable')
    @pytest.mark.sanity
    def test_the_next_arrow_clickable(self):
        product = ProductAdmin(self)
        product.open_trado_admin()
        product.click_phone()
        product.click_code()
        product.click_product_option()
        product.click_single_next_arrow()

    @allure.description('test_the_next_double_clickable')
    @pytest.mark.sanity
    def test_next_double_arrow_clickable(self):
        product = ProductAdmin(self)
        product.open_trado_admin()
        product.click_phone()
        product.click_code()
        product.click_product_option()
        product.click_double_next_arrow()

    @allure.description('test_double_back_arrow_clickable')
    @pytest.mark.sanity
    def test_double_back_arrow_clickable(self):
        product = ProductAdmin(self)
        product.open_trado_admin()
        product.click_phone()
        product.click_code()
        product.click_product_option()
        product.click_amount_display()
        product.click_amount_display()

    @allure.description('test_to_add_product')
    @pytest.mark.sanity
    def test_to_add_product(self):
        product = ProductAdmin(self)
        product.open_trado_admin()
        product.click_phone()
        product.click_code()
        product.click_product_option()

    def test_to_change_from_Hebrew_to_English_language(self):
        product = ProductAdmin(self)
        product.open_trado_admin()
        product.click_phone()
        product.click_code()
        product.click_to_change_language()

    def test_to_change_from_English_to_Hebrew_language(self):
        product = ProductAdmin(self)
        product.open_trado_admin()
        product.click_phone()
        product.click_code()
        product.click_to_change_language()


