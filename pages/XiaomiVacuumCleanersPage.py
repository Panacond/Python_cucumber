from selenium.webdriver.common.keys import Keys

from pages.BasePage import BasePage


class XiaomiVacuumCleanersPage(BasePage):

    locators = {
        "buttonPrice": ('XPATH', "//span[text()='Price']"),
        "selectPriceRange150_350": ('XPATH', "//span[text()='$150.00 to $350.00']"),
        "checkPrice": ('XPATH', "//span[@class='s-item__price']"),
        "buttonView": ('XPATH', "//button[@aria-label='Gallery View']"),
        "buttonViewList": ('XPATH', "//span[text()='List View']"),
        "elementViewList": ('XPATH', "//ul[@class='b-list__items_nofooter']"),
        "firstElementList": ('XPATH', "//div[@class='s-item__wrapper clearfix']"),
        "searchField": ('XPATH', "//input[@placeholder='Search for anything']"),
        "listResultTitle": ('XPATH', "//h3[@class='s-item__title']"),
    }

    def clickButtonPrice(self):
        self.buttonPrice.click()

    def clickSelectPriceRange150_350(self):
        self.selectPriceRange150_350.click()

    def getCheckPrise(self):
        # return self.checkPrice.get_all_list_item()
        return self.driver.find_elements_by_xpath("//span[@class='s-item__price']")
    def clickButtonView(self):
        self.buttonView.click_button()

    def clickButtonViewList(self):
        self.buttonViewList.click_button()

    def isElementViewListVisible(self):
        self.elementViewList.is_displayed()

    def clickFirstElementList(self):
        self.firstElementList.click()

    def inputSearchField(self, text):
        self.searchField.set_text(text + Keys.ENTER)

    def getListResultTitle(self):
        # return self.listResultTitle.get_all_list_item()
        return self.driver.find_elements_by_xpath(self.locators.get("listResultTitle")[1])
