from pages.BasePage import BasePage


class NewsPage(BasePage):
    locators = {
        "elementNews": ('XPATH', "//div[@class='article-wrapper internal-article wide-ml-content animate']")
    }

    def getElementNews(self):
        return self.elementNews

    def isElementNewsVisible(self):
        self.elementNews.is_displayed()
