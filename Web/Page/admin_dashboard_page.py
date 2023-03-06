

from selenium import webdriver
from Web.Locator.locators_dashboard_admin import Admin_locators
from selenium.webdriver.common.by import By
import time
import allure

class Admin_page(Admin_locators):
    def __init__(self, driver):
        self.driver = driver
        self.url = Admin_locators.admin_url
        self.product = Admin_locators.product_XPATH
        self.sales = Admin_locators.sales_XPATH
        self.coupon = Admin_locators.coupon_XPATH
        self.orders = Admin_locators.orders_XPATH
        self.invoices = Admin_locators.invoices_XPATH
        self.shipping_certificates = Admin_locators.shipping_certificates_XPATH
        self.shipping_dashboard = Admin_locators.shipping_dashboard_XPATH
        self.shipping_tables = Admin_locators.shipping_tables_XPATH
        self.review_purchases = Admin_locators.review_purchases_XPATH
        self.review_monthly = Admin_locators.review_monthly_XPATH
        self.review_daily = Admin_locators.review_daily_XPATH
        self.audience_review = Admin_locators.audience_review_XPATH
        self.reviewing_behaviors = Admin_locators.reviewing_behaviors_XPATH
        self.overview = Admin_locators.overview_XPATH
        self.dashboard = Admin_locators.dashboard_XPATH
        self.reports = Admin_locators.reports_XPATH
        self.date_display = Admin_locators.date_display_ID
        self. alerts = Admin_locators.alerts_XPATH
        self.objectives = Admin_locators.objectives_XPATH
        self.finanec = Admin_locators.finanec_XPATH
        self. etrado = Admin_locators.etrado_XPATH
        self.departement = Admin_locators.departement_XPATH
        self.catagory = Admin_locators.catagory_XPATH
        self.stores = Admin_locators.stores_XPATH
        self.users = Admin_locators.users_XPATH
        self.user_system = Admin_locators.user_system_XPATH
        self.hand_outs = Admin_locators.hand_outs_XPATH
        self.setting = Admin_locators.setting_XPATH
        self.records = Admin_locators.records_XPATH
        self.dashboard_button = Admin_locators.dashboard_button_xpath
        self.dashboard_coupon = Admin_locators.dashboard_coupon_XPATH
        self.dashboard_finances_1 = Admin_locators.dashboard_finances_1_XPATH
        self.dashboard_orders = Admin_locators.dashboard_orders_XPATH
        self.dashboard_product = Admin_locators.dashboard_product_XPATH
        self.dashboard_sales = Admin_locators.dashboard_sales_XPATH
        self.dashboard_stores = Admin_locators.dashboard_stores_XPATH
        self.dashboard_users = Admin_locators.dashboard_users_XPATH
        self.dashboard_finances_2 = Admin_locators.dashboard_finances_2_XPATH
        self.option_phone = Admin_locators.option1_xpath
        self.option_code = Admin_locators.option2_xpath

    @allure.step
    @allure.description('opening_trado')
    def opening_trado(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(4)


    @allure.step
    @allure.description('click_phone')
    def click_phone(self):
        self.driver.find_element(By.XPATH, self.option_phone).send_keys("1950000000")
        time.sleep(4)
        self.driver.find_element(By.XPATH, self.click_xpath).click()
        time.sleep(4)



    @allure.step
    @allure.description('click_code')
    def click_code(self):
        self.driver.find_element(By.XPATH, self.option_code).send_keys("1234")
        self.driver.find_element(By.XPATH, self.login_button).click()
        self.driver.implicitly_wait(6)

    # def click_save_button(self):
    #     self.driver.find_element(By.XPATH, self.login_button).click()


    @allure.step
    @allure.description('click_on_product')
    def click_on_product(self):
        self.driver.find_element(By.XPATH, self.product).click()
        assertion_product = self.driver.find_element(By.TAG_NAME, "h4").text
        assert assertion_product == "מוצרים"
        self.driver.implicitly_wait(3)



    @allure.step
    @allure.description('click_on_sales')
    def click_on_sales(self):
        self.driver.find_element(By.XPATH, self.sales).click()
        assertion_sales = self.driver.find_element(By.TAG_NAME, "h4").text
        assert assertion_sales == "מבצעים"
        self.driver.implicitly_wait(3)



    @allure.step
    @allure.description('click_on_coupon')
    def click_on_coupon(self):
        self.driver.find_element(By.XPATH, self.coupon).click()
        assertion_coupon = self.driver.find_element(By.TAG_NAME,"h4").text
        assert assertion_coupon == "קופונים"
        self.driver.implicitly_wait(3)



    @allure.step
    @allure.description('click_on_orders')
    def click_on_orders(self):
        self.driver.find_element(By.XPATH, self.orders).click()
        assertion_orders = self.driver.find_element(By.XPATH, "//h4[contains(text(),'הזמנות')]").text
        assert assertion_orders == "הזמנות"
        self.driver.implicitly_wait(3)



    @allure.step
    @allure.description('click_on_invoices')
    def click_on_invoices(self):
        self.driver.find_element(By.XPATH, self.invoices).click()
        assertion_invoices = self.driver.find_element(By.XPATH, "//h4[contains(text(),'חשבוניות')]").text
        assert assertion_invoices == "חשבוניות"
        self.driver.implicitly_wait(3)



    @allure.step
    @allure.description('click_on_shipping_certificates')
    def click_on_shipping_certificates(self):
        self.driver.find_element(By.XPATH, self.shipping_certificates).click()
        assertion_shipping_cert = self.driver.find_element(By.XPATH, "//h4[contains(text(),'תעודת משלוח')]").text
        assert assertion_shipping_cert == "תעודת משלוח"
        self.driver.implicitly_wait(3)



    @allure.step
    @allure.description('click_on_shipping_dashboard')
    def click_on_shipping_dashboard(self):
        self.driver.find_element(By.XPATH, self.shipping_dashboard).click()
        assertion_shipping_dash = self.driver.find_element(By.XPATH, "//h4[contains(text(),'דשבורד משלוחים')]").text
        assert assertion_shipping_dash == "דשבורד משלוחים"
        self.driver.implicitly_wait(3)



    @allure.step
    @allure.description('click_on_shipping_tables')
    def click_on_shipping_tables(self):
        self.driver.find_element(By.XPATH, self.shipping_tables).click()
        assertion_shipping_cert = self.driver.find_element(By.XPATH, "//h4[contains(text(),'טבלת משלוחים')]").text
        assert assertion_shipping_cert == "טבלת משלוחים"
        self.driver.implicitly_wait(3)




    @allure.step
    @allure.description('click_on_review_purchases')
    def click_on_review_purchases(self):
        self.driver.find_element(By.XPATH, self.review_purchases).click()
        assertion_purchases = self.driver.find_element(By.XPATH, "//h4[contains(text(),'סקירת רכישות')]").text
        assert assertion_purchases == "סקירת רכישות"
        self.driver.implicitly_wait(3)





    @allure.step
    @allure.description('click_on_review_monthly')
    def click_on_review_monthly(self):
        self.driver.find_element(By.XPATH, self.review_monthly).click()
        assertion_purchases = self.driver.find_element(By.XPATH, "//h4[contains(text(),'סקירת רכישות')]").text
        assert assertion_purchases == "סקירת רכישות"
        self.driver.implicitly_wait(3)




    @allure.step
    @allure.description('click_on_review_daily')
    def click_on_review_daily(self):
        self.driver.find_element(By.XPATH, self.review_daily).click()
        assertion_purchases = self.driver.find_element(By.XPATH, "//h4[contains(text(),'סקירת רכישות')]").text
        assert assertion_purchases == "סקירת רכישות"
        self.driver.implicitly_wait(3)




    @allure.step
    @allure.description('click_on_audience_review')
    def click_on_audience_review(self):
        self.driver.find_element(By.XPATH, self.audience_review).click()
        assertion_purchases = self.driver.find_element(By.XPATH, "//h4[contains(text(),'סקירת קהלים')]").text
        assert assertion_purchases == "סקירת קהלים"
        self.driver.implicitly_wait(3)



    @allure.step
    @allure.description('click_on_reviewing_behaviors')
    def click_on_reviewing_behaviors(self):
        self.driver.find_element(By.XPATH, self.reviewing_behaviors).click()
        assertion_purchases = self.driver.find_element(By.XPATH, "//h4[contains(text(),'סקירת התנהגויות')]").text
        assert assertion_purchases == "סקירת התנהגויות"
        self.driver.implicitly_wait(3)



    @allure.step
    @allure.description('click_on_overview')
    def click_on_overview(self):
        self.driver.find_element(By.XPATH, self.overview).click()
        assertion_purchases = self.driver.find_element(By.TAG_NAME, "h4").text
        assert assertion_purchases == "דשבורד"
        self.driver.implicitly_wait(3)




    @allure.step
    @allure.description('click_on_dashboard')
    def click_on_dashboard(self):
        self.driver.find_element(By.XPATH, self.dashboard).click()
        assertion_purchases = self.driver.find_element(By.TAG_NAME, "h4").text
        assert assertion_purchases == "דשבורד"
        self.driver.implicitly_wait(3)



    @allure.step
    @allure.description('click_on_reports')
    def click_on_reports(self):
        self.driver.find_element(By.XPATH, self.reports).click()
        assertion_purchases = self.driver.find_element(By.XPATH, "//h4[contains(text(),'דיווחים')]").text
        assert assertion_purchases == "דיווחים'"
        self.driver.implicitly_wait(3)




    @allure.step
    @allure.description('click_on_date_display')
    def click_on_date_display(self):
        self.driver.find_element(By.ID, self.date_display).click()
        assertion_purchases = self.driver.find_element(By.XPATH, "//span[contains(text(),'היום')]").text
        assert assertion_purchases == "היום"
        self.driver.implicitly_wait(3)




    @allure.step
    @allure.description('click_on_alerts')
    def click_on_alerts(self):
        self.driver.find_element(By.XPATH, self.alerts).click()
        assertion_purchases = self.driver.find_element(By.XPATH, "//h4[contains(text(),'דשבורד')]").text
        assert assertion_purchases == "דשבורד"
        self.driver.implicitly_wait(3)



    @allure.step
    @allure.description('click_on_objectives')
    def click_on_objectives(self):
        self.driver.find_element(By.XPATH, self.objectives).click()
        assertion_purchases = self.driver.find_element(By.XPATH, "//h4[contains(text(),'דשבורד')]").text
        assert assertion_purchases == "דשבורד"
        self.driver.implicitly_wait(3)




    @allure.step
    @allure.description('click_on_finanec')
    def click_on_finanec(self):
        self.driver.find_element(By.XPATH, self.finanec).click()
        assertion_purchases = self.driver.find_element(By.XPATH, "//h4[contains(text(),'פיננסים')]").text
        assert assertion_purchases == "פיננסים"
        self.driver.implicitly_wait(3)



    @allure.step
    @allure.description('click_on_etrado')
    def click_on_etrado(self):
        self.driver.find_element(By.XPATH, self.etrado).click()
        assertion_purchases = self.driver.find_element(By.XPATH, "//h4[contains(text(),'eTrado')]").text
        assert assertion_purchases == "eTrado"
        self.driver.implicitly_wait(3)



    @allure.step
    @allure.description('click_on_departement')
    def click_on_departement(self):
        self.driver.find_element(By.XPATH, self.departement).click()
        assertion_purchases = self.driver.find_element(By.XPATH, "//h4[contains(text(),'מחלקות')]").text
        assert assertion_purchases == "מחלקות"
        self.driver.implicitly_wait(3)



    @allure.step
    @allure.description('click_on_catagory')
    def click_on_catagory(self):
        self.driver.find_element(By.XPATH, self.catagory).click()
        assertion_purchases = self.driver.find_element(By.XPATH, "//h4[contains(text(),'קטגוריות')]").text
        assert assertion_purchases == "קטגוריות"
        self.driver.implicitly_wait(3)



    @allure.step
    @allure.description('click_on_stores')
    def click_on_stores(self):
        self.driver.find_element(By.XPATH, self.stores).click()
        assertion_purchases = self.driver.find_element(By.XPATH, "//h4[contains(text(),'חנויות')]").text
        assert assertion_purchases == "חנויות"
        self.driver.implicitly_wait(3)



    @allure.step
    @allure.description('click_on_users')
    def click_on_users(self):
        self.driver.find_element(By.XPATH, self.users).click()
        assertion_purchases = self.driver.find_element(By.XPATH, "//h4[contains(text(),'משתמשים')]").text
        assert assertion_purchases == "משתמשים"
        self.driver.implicitly_wait(3)



    @allure.step
    @allure.description('click_on_user_system')
    def click_on_user_system(self):
        self.driver.find_element(By.XPATH, self.user_system).click()
        assertion_purchases = self.driver.find_element(By.XPATH, "//h4[contains(text(),'משתמשי מערכת')]").text
        assert assertion_purchases == "משתמשי מערכת"
        self.driver.implicitly_wait(3)



    @allure.step
    @allure.description('click_on_hand_outs')
    def click_on_hand_outs(self):
        self.driver.find_element(By.XPATH, self.hand_outs).click()
        assertion_purchases = self.driver.find_element(By.XPATH, "//h4[contains(text(),'דפי מידע')]").text
        assert assertion_purchases == "דפי מידע"
        self.driver.implicitly_wait(3)



    @allure.step
    @allure.description('click_on_setting')
    def click_on_setting(self):
        self.driver.find_element(By.XPATH, self.setting).click()
        assertion_purchases = self.driver.find_element(By.XPATH, "//h4[contains(text(),'הגדרות')]").text
        assert assertion_purchases == "הגדרות"
        self.driver.implicitly_wait(3)



    @allure.step
    @allure.description('click_on_user_records')
    def click_on_user_records(self):
        self.driver.find_element(By.XPATH, self.records).click()
        assertion_purchases = self.driver.find_element(By.XPATH, "//h4[contains(text(),'תיעודים')]").text
        assert assertion_purchases == "תיעודים"
        self.driver.implicitly_wait(3)

    # Dashboard_page_Dashboard_page_Dashboard_page_Dashboard_page_Dashboard_page_Dashboard_page_Dashboard_page_Dashboard
    @allure.step
    @allure.description('click_on_dashboard_button')
    def click_on_dashboard_button(self):
        self.driver.find_element(By.XPATH, self.dashboard_button).click()
        self.driver.implicitly_wait(3)



    @allure.step
    @allure.description('click_on_coupon_dashboard')
    def click_on_coupon_dashboard(self):
        self.driver.find_element(By.XPATH, self.dashboard_coupon).click()
        assertion_dashboard = self.driver.find_element(By.XPATH, "//h4[contains(text(),'קופונים')]").text
        assert assertion_dashboard == "קופונים"
        self.driver.implicitly_wait(3)



    @allure.step
    @allure.description('click_on_finances_1_dashboard')
    def click_on_finances_1_dashboard(self):
        self.driver.find_element(By.XPATH, self.dashboard_finances_1).click()
        assertion_dashboard = self.driver.find_element(By.XPATH, "//h4[contains(text(),'קופונים')]").text
        assert assertion_dashboard == "קופונים"
        self.driver.implicitly_wait(3)





    @allure.step
    @allure.description('click_on_orders_dashboard')
    def click_on_orders_dashboard(self):
        self.driver.find_element(By.XPATH, self.orders).click()
        assertion_dashboard = self.driver.find_element(By.XPATH, "//h4[contains(text(),'הזמנות')]").text
        assert assertion_dashboard == "הזמנות"
        self.driver.implicitly_wait(3)




    @allure.step
    @allure.description('click_on__product_dashboard')
    def click_on__product_dashboard(self):
        self.driver.find_element(By.XPATH, self.product).click()
        assertion_dashboard = self.driver.find_element(By.XPATH, "//h4[contains(text(),'מוצרים')]").text
        assert assertion_dashboard == "מוצרים"
        self.driver.implicitly_wait(3)




    @allure.step
    @allure.description(' click_on__sales_dashboard')
    def click_on__sales_dashboard(self):
        self.driver.find_element(By.XPATH, self.sales).click()
        assertion_dashboard = self.driver.find_element(By.XPATH, "//h4[contains(text(),'מבצעים')]").text
        assert assertion_dashboard == "מבצעים"
        self.driver.implicitly_wait(3)



    @allure.step
    @allure.description('click_on_stores_dashboard')
    def click_on_stores_dashboard(self):
        self.driver.find_element(By.XPATH, self.stores).click()
        assertion_dashboard = self.driver.find_element(By.XPATH, "//h4[contains(text(),'חנויות')]").text
        assert assertion_dashboard == "חנויות"
        self.driver.implicitly_wait(3)



    @allure.step
    @allure.description('click_on_users_dashboard')
    def click_on_users_dashboard(self):
        self.driver.find_element(By.XPATH, self.users).click()
        assertion_dashboard = self.driver.find_element(By.XPATH, "//h4[contains(text(),'משתמשים')]").text
        assert assertion_dashboard == "משתמשים"
        self.driver.implicitly_wait(3)



    @allure.step
    @allure.description('finances_2_dashboard')
    def click_on_finances_2_dashboard(self):
        self.driver.find_element(By.XPATH, self.dashboard_finances_2).click()
        assertion_dashboard = self.driver.find_element(By.XPATH, "//h4[contains(text(),'משתמשים')]").text
        assert assertion_dashboard == "משתמשים"
        self.driver.implicitly_wait(3)


