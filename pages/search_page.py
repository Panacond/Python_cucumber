from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


class SearchPage(BasePage):
    locators = {
        "result_title_search": ('XPATH', "//h3[@class='s-item__title']"),
        "no_exact_matches_message": ('XPATH', "//h3[text()='No exact matches found']"),
        "field_min_price": ('XPATH', "//input[@aria-label='Minimum Value in $']"),
        "result_error_price_find": ('XPATH', "//div[@class='x-price__error']"),
        "related_search": ('XPATH', "//span[@class='cbx x-refine__multi-select-cbx']"),
    }

    def get_search_result_title(self):
        return self.driver.find_elements_by_xpath(self.locators.get("result_title_search")[1])

    def is_no_exact_matches_message_visible(self):
        self.no_exact_matches_message.is_displayed()

    def set_minimum_price(self, price):
        self.field_min_price.set_text(price + Keys.ENTER)

    def error_input_price_value(self):
        expected = True
        if self.result_error_price_find == 1:
            expected = False
        return expected

    def set_related_search(self, text):
        for element in self.driver.find_elements_by_xpath(self.locators.get("related_search")[1]):
            try:
                element_text = element.text
            except Exception:
                element_text = ""
            if text in element_text:
                element.click()
                continue
