from pages.base_page import BasePage


class HomePage(BasePage):
    locators = {
        "news_page": ('XPATH', "//a[@href='https://www.ebayinc.com/stories/news/']"),
        "field_search": ('XPATH', "//input[@placeholder='Search for anything']"),
        "button_search": ('XPATH', "//input[@id='gh-btn']"),
        "button_xiaomi": ('XPATH', "//img[@src='https://i.ebayimg.com/images/g/pq0AAOSwOFFeJrV0/s-l200.webp']")
    }

    def go_news_page(self):
        self.news_page.click_button()

    def input_field_search(self, text):
        self.field_search.set_text(text)

    def click_button_search(self):
        self.button_search.click()

    def click_button_xiaomi(self):
        # self.button_xiaomi.click_button()
        self.driver.find_element_by_xpath("//img[@src='https://i.ebayimg.com/images/g/pq0AAOSwOFFeJrV0/s-l200.webp']").click()
