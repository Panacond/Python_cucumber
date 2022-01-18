from pages.BasePage import BasePage


class ProductPage(BasePage):
    locators = {
        "buttonAddToWatchlist": ('XPATH', "//span[text()='Add to Watchlist']"),
        "fieldNumberProduct": ('XPATH', "//input[@class='qtyInput']"),
        "errorNumberMessage": ('XPATH', "//div[@id='w1-13-_errMsg']"),
    }

    def clickButtonAddToWatchlist(self):
        self.buttonAddToWatchlist.click()

    def inputFieldNumberProduct(self, number):
        self.fieldNumberProduct.set_text(number)

    def clickFieldNumberProduct(self):
        self.fieldNumberProduct.click()

    def isErrorNumberMessage(self):
        self.errorNumberMessage.is_displayed()