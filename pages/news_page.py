from pages.base_page import BasePage


class NewsPage(BasePage):
    locators = {
        "element_news": ('XPATH', "//div[@class='article-wrapper internal-article wide-ml-content animate']")
    }

    def get_element_news(self):
        return self.element_news

    def is_element_news_visible(self):
        self.element_news.is_displayed()
