from pages.BasePage import BasePage


class HomePage(BasePage):
    locators = {
        "newsPage": ('XPATH', "//a[@href='https://www.ebayinc.com/stories/news/']"),
        "fieldSearch": ('XPATH', "//input[@placeholder='Search for anything']"),
        "buttonSearch": ('XPATH', "//input[@id='gh-btn']"),
        "buttonXiaomi": ('XPATH', "//img[@src='https://i.ebayimg.com/images/g/pq0AAOSwOFFeJrV0/s-l200.webp']")
    }

    def goNewsPage(self):
        self.newsPage.click_button()

    def inputFieldSearch(self, text):
        self.fieldSearch.set_text(text)

    def clickButtonSearch(self):
        self.buttonSearch.click()

    def clickButtonXiaomi(self):
        # self.buttonXiaomi.click_button()
        self.driver.find_element_by_xpath("//img[@src='https://i.ebayimg.com/images/g/pq0AAOSwOFFeJrV0/s-l200.webp']").click()
