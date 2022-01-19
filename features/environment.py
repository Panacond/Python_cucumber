from selenium import webdriver
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.news_page import NewsPage
from pages.product_page import ProductPage
from pages.search_page import SearchPage
from pages.xiaomi_page import XiaomiPage
from pages.xiaomi_vacuum_cleaners_page import XiaomiVacuumCleanersPage


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.ebay.com/")
    context.driver.maximize_window()


def after_scenario(context, scenario):
    context.driver.close()


class BaseTest(object):
    DEFAULT_TIMEOUT = 100

    def __init__(self):
        self.driver = None

    def get_home_page(self):
        return HomePage(self.driver)

    def get_login_page(self):
        return LoginPage(self.driver)

    def get_news_page(self):
        return NewsPage(self.driver)

    def get_product_page(self):
        return ProductPage(self.driver)

    def get_search_page(self):
        return SearchPage(self.driver)

    def get_xiaomi_page(self):
        return XiaomiPage(self.driver)

    def get_xiaomi_vacuum_cleaners_page(self):
        return XiaomiVacuumCleanersPage(self.driver)
