from selenium.webdriver.common.keys import Keys

from pages.BasePage import BasePage


class SearchPage(BasePage):
    locators = {
        "resultTitleSearch": ('XPATH', "//h3[@class='s-item__title']"),
        "noExactMatchesMessage": ('XPATH', "//h3[text()='No exact matches found']"),
        "fieldMinPrice": ('XPATH', "//input[@aria-label='Minimum Value in $']"),
        "resultErrorPriceFind": ('XPATH', "//div[@class='x-price__error']"),
        "relatedSearch": ('XPATH', "//span[@class='cbx x-refine__multi-select-cbx']"),
    }

    def getSearchResultTitle(self):
        return self.driver.find_elements_by_xpath("//h3[@class='s-item__title']")

    def isNoExactMatchesMessageVisible(self):
        self.noExactMatchesMessage.is_displayed()

    def setMinimumPrice(self, price):
        self.fieldMinPrice.set_text(price + Keys.ENTER)

    def errorInputPriceValue(self):
        expected = True
        if self.resultErrorPriceFind == 1:
            expected = False
        return expected

    def setRelatedSearch(self, text):
        for element in self.driver.find_elements_by_xpath(self.locators.get("relatedSearch")[1]):
            try:
                element_text = element.text
            except Exception:
                element_text = ""
            if text in element_text:
                element.click()
                continue