from pages.base_page import BasePage


class XiaomiPage(BasePage):
    locators = {
        "button_vacuum_cleaners": ('XPATH', "//div[contains(text(),'Cleaners')]"),
    }

    def click_button_vacuum_cleaners(self):
        self.button_vacuum_cleaners.click()
