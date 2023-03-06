
from selenium import webdriver
from Web.Page.admin_dashboard_page import Admin_page
import allure
import time

class  Test_Admin_side:

    @allure.description('test_admin_side_product_button')
    def test_admin_side_product_button(self):
        side_product_button = Admin_page(self)
        side_product_button.opening_trado()
        side_product_button.click_phone()
        side_product_button.click_code()
        side_product_button.click_on_product()


    @allure.description('test_admin_side_sales_button')
    def test_admin_side_sales_button(self):
        side_sales_button = Admin_page(self)
        side_sales_button.opening_trado()
        side_sales_button.click_phone()
        side_sales_button.click_code()
        side_sales_button.click_on_sales()


    @allure.description('test_admin_side_coupon')
    def test_admin_side_coupon(self):
        side_coupon_button = Admin_page(self)
        side_coupon_button.opening_trado()
        side_coupon_button.click_phone()
        side_coupon_button.click_code()
        side_coupon_button.click_on_coupon()



    @allure.description('test_admin_side_orders')
    def test_admin_side_orders(self):
        side_orders_button = Admin_page(self)
        side_orders_button.opening_trado()
        side_orders_button.click_phone()
        side_orders_button.click_code()
        side_orders_button.click_on_orders()

    @allure.description('test_admin_side_invoices')
    def test_admin_side_invoices(self):
        side_invoices_button = Admin_page(self)
        side_invoices_button.opening_trado()
        side_invoices_button.click_phone()
        side_invoices_button.click_code()
        side_invoices_button.click_on_invoices()


    @allure.description('test_admin_side_shipping_certificates')
    def test_admin_side_shipping_certificates(self):
        side_shipping_certificates = Admin_page(self)
        side_shipping_certificates.opening_trado()
        side_shipping_certificates.click_phone()
        side_shipping_certificates.click_code()
        side_shipping_certificates.click_on_shipping_certificates()



    @allure.description('test_admin_side_shippimg_dashboars')
    def test_admin_side_shippimg_dashboars(self):
        side_shipping_dashboard = Admin_page(self)
        side_shipping_dashboard.opening_trado()
        side_shipping_dashboard.click_phone()
        time.sleep(3)
        side_shipping_dashboard.click_code()
        time.sleep(3)
        side_shipping_dashboard.click_on_shipping_dashboard()
        time.sleep(4)



    @allure.description('test_admin_side_shipping_table')
    def test_admin_side_shipping_table(self):
        side_shipping_table = Admin_page(self)
        side_shipping_table.opening_trado()
        side_shipping_table.click_phone()
        time.sleep(3)
        side_shipping_table.click_code()
        time.sleep(3)
        side_shipping_table.click_on_shipping_tables()




    @allure.description('test_admin_side_purchases')
    def test_admin_side_purchases(self):
        side_purchases = Admin_page(self)
        side_purchases.opening_trado()
        side_purchases.click_phone()
        side_purchases.click_code()
        side_purchases.click_on_review_purchases()
        side_purchases.click_on_review_monthly()
        side_purchases.click_on_review_daily()



    @allure.description('test_side_audience_review')
    def test_side_audience_review(self):
        side_audiences = Admin_page(self)
        side_audiences.opening_trado()
        side_audiences.click_phone()
        side_audiences.click_code()
        side_audiences.click_on_audience_review()



    @allure.description('test_side_reviewing_behaviors')
    def test_side_reviewing_behaviors(self):
        side_behaviors = Admin_page(self)
        side_behaviors.opening_trado()
        side_behaviors.click_phone()
        time.sleep(4)
        side_behaviors.click_code()
        time.sleep(4)
        side_behaviors.click_on_reviewing_behaviors()
        time.sleep(4)


    @allure.description('test_side_overview')
    def test_side_overview(self):
        side_overview = Admin_page(self)
        side_overview.opening_trado()
        side_overview.click_phone()
        time.sleep(4)
        side_overview.click_code()
        time.sleep(4)
        side_overview.click_on_reviewing_behaviors()



    @allure.description('test_side_dashboard')
    def test_side_dashboard(self):
        side_dashboard = Admin_page(self)
        side_dashboard.opening_trado()
        side_dashboard.click_phone()
        time.sleep(4)
        side_dashboard.click_code()
        time.sleep(4)
        side_dashboard.click_on_reviewing_behaviors()



    @allure.description('test_side_report')
    def test_side_report(self):
        side_report = Admin_page(self)
        side_report.opening_trado()
        side_report.click_phone()
        time.sleep(4)
        side_report.click_code()
        time.sleep(4)
        side_report.click_on_reports()
        time.sleep(3)
        side_report.click_on_date_display()
        time.sleep(2)



    @allure.description('test_side_alerts')
    def test_side_alerts(self):
        side_alerts = Admin_page(self)
        side_alerts.opening_trado()
        side_alerts.click_phone()
        time.sleep(4)
        side_alerts.click_code()
        time.sleep(4)
        side_alerts.click_on_alerts()


    @allure.description('test_side_objectives')
    def test_side_objectives(self):
        side_objectives = Admin_page(self)
        side_objectives.opening_trado()
        side_objectives.click_phone()
        time.sleep(4)
        side_objectives.click_code()
        time.sleep(4)
        side_objectives.click_on_objectives()



    @allure.description('test_side_finanec')
    def test_side_finanec(self):
        side_finance = Admin_page(self)
        side_finance.opening_trado()
        side_finance.click_phone()
        time.sleep(4)
        side_finance.click_code()
        time.sleep(4)
        side_finance.click_on_finanec()



    @allure.description('test_side_etrado')
    def test_side_etrado(self):
        side_etrado = Admin_page(self)
        side_etrado.opening_trado()
        side_etrado.click_phone()
        time.sleep(4)
        side_etrado.click_code()
        time.sleep(4)
        side_etrado.click_on_etrado()



    @allure.description('test_side_departement')
    def test_side_departement(self):
        side_departement = Admin_page(self)
        side_departement.opening_trado()
        side_departement.click_phone()
        time.sleep(4)
        side_departement.click_code()
        time.sleep(4)
        side_departement.click_on_departement()



    @allure.description('test_side_catagory')
    def test_side_catagory(self):
        side_catagory = Admin_page(self)
        side_catagory.opening_trado()
        side_catagory.click_phone()
        time.sleep(4)
        side_catagory.click_code()
        time.sleep(4)
        side_catagory.click_on_catagory()




    @allure.description('test_side_store')
    def test_side_store(self):
        side_stores = Admin_page(self)
        side_stores.opening_trado()
        side_stores.click_phone()
        time.sleep(4)
        side_stores.click_code()
        time.sleep(4)
        side_stores.click_on_stores()



    @allure.description('test_side_users')
    def test_side_users(self):
        side_users = Admin_page(self)
        side_users.opening_trado()
        side_users.click_phone()
        time.sleep(4)
        side_users.click_code()
        time.sleep(4)
        side_users.click_on_users()



    @allure.description('test_side_system_users')
    def test_side_system_users(self):
        side_system_user = Admin_page(self)
        side_system_user.opening_trado()
        side_system_user.click_phone()
        time.sleep(4)
        side_system_user.click_code()
        time.sleep(4)
        side_system_user.click_on_user_system()



    @allure.description('test_side_hand_outs')
    def test_side_hand_outs(self):
        side_hand_outs = Admin_page(self)
        side_hand_outs.opening_trado()
        side_hand_outs.click_phone()
        time.sleep(4)
        side_hand_outs.click_code()
        time.sleep(4)
        side_hand_outs.click_on_hand_outs()




    @allure.description('test_side_setting')
    def test_side_setting(self):
        side_setting = Admin_page(self)
        side_setting.opening_trado()
        side_setting.click_phone()
        time.sleep(4)
        side_setting.click_code()
        time.sleep(4)
        side_setting.click_on_setting()



    @allure.description('test_side_user_records')
    def test_side_user_records(self):
        side_user_records = Admin_page(self)
        side_user_records.opening_trado()
        side_user_records.click_phone()
        time.sleep(4)
        side_user_records.click_code()
        time.sleep(4)
        side_user_records.click_on_user_records()
        time.sleep(3)

    # Dashboard_test_Dashboard_test_Dashboard_test_Dashboard_test_Dashboard_test_Dashboard_test_Dashboard_test_Dashboard


    @allure.description('test_dashboard_coupon')
    def test_dashboard_coupon(self):
        coupon_dashboard = Admin_page(self)
        coupon_dashboard.opening_trado()
        coupon_dashboard.click_phone()
        time.sleep(3)
        coupon_dashboard.click_code()
        time.sleep(3)
        coupon_dashboard.click_on_dashboard_button()
        time.sleep(3)
        coupon_dashboard.click_on_coupon_dashboard()
        time.sleep(3)



    @allure.description('test_dashboard_finances_1')
    def test_dashboard_finances_1(self):
        finances_1_dashboard = Admin_page(self)
        finances_1_dashboard.opening_trado()
        finances_1_dashboard.click_phone()
        time.sleep(3)
        finances_1_dashboard.click_code()
        time.sleep(3)
        finances_1_dashboard.click_on_dashboard_button()
        time.sleep(7)
        finances_1_dashboard.click_on_finances_1_dashboard()
        time.sleep(6)



    @allure.description('test_dashboard_orders')
    def test_dashboard_orders(self):
        orders_dashboard = Admin_page(self)
        orders_dashboard.opening_trado()
        orders_dashboard.click_phone()
        time.sleep(3)
        orders_dashboard.click_code()
        time.sleep(3)
        orders_dashboard.click_on_dashboard_button()
        time.sleep(7)
        orders_dashboard.click_on_orders_dashboard()




    @allure.description('test_dashboard_productas')
    def test_dashboard_productas(self):
        products_dashboard = Admin_page(self)
        products_dashboard.opening_trado()
        products_dashboard.click_phone()
        time.sleep(3)
        products_dashboard.click_code()
        time.sleep(3)
        products_dashboard.click_on_dashboard_button()
        time.sleep(7)
        products_dashboard.click_on__product_dashboard()




    @allure.description('test_dashboard_sales')
    def test_dashboard_sales(self):
        sales_dashboard = Admin_page(self)
        sales_dashboard.opening_trado()
        sales_dashboard.click_phone()
        time.sleep(3)
        sales_dashboard.click_code()
        time.sleep(3)
        sales_dashboard.click_on_dashboard_button()
        time.sleep(7)
        sales_dashboard.click_on__sales_dashboard()



    @allure.description('test_dashboard_stores')
    def test_dashboard_stores(self):
        stores_dashboard = Admin_page(self)
        stores_dashboard.opening_trado()
        stores_dashboard.click_phone()
        time.sleep(3)
        stores_dashboard.click_code()
        time.sleep(3)
        stores_dashboard.click_on_dashboard_button()
        time.sleep(7)
        stores_dashboard.click_on_stores_dashboard()



    @allure.description('test_dashboard_users')
    def test_dashboard_users(self):
        users_dashboard = Admin_page(self)
        users_dashboard.opening_trado()
        users_dashboard.click_phone()
        time.sleep(3)
        users_dashboard.click_code()
        time.sleep(3)
        users_dashboard.click_on_dashboard_button()
        time.sleep(7)
        users_dashboard.click_on_users_dashboard()




    @allure.description('test_dashboard_finances')
    def test_dashboard_finances(self):
        finances_dashboard = Admin_page(self)
        finances_dashboard.opening_trado()
        finances_dashboard.click_phone()
        time.sleep(3)
        finances_dashboard.click_code()
        time.sleep(3)
        finances_dashboard.click_on_dashboard_button()
        time.sleep(7)
        finances_dashboard.click_on_finances_2_dashboard()

