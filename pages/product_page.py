from pages.base_page import BasePage


class ProductPage(BasePage):
    locators = {
        "button_add_to_watchlist": ('XPATH', "//span[text()='Add to Watchlist']"),
        "field_number_product": ('XPATH', "//input[@class='qtyInput']"),
        "error_number_message": ('XPATH', "//div[@id='w1-13-_errMsg']"),
    }

    def click_button_add_to_watchlist(self):
        self.button_add_to_watchlist.click()

    def input_field_number_product(self, number):
        self.field_number_product.set_text(number)

    def click_field_number_product(self):
        self.field_number_product.click()

    def is_error_number_message(self):
        self.error_number_message.is_displayed()