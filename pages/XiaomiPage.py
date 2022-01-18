from pages.BasePage import BasePage


class XiaomiPage(BasePage):
    locators = {
        "buttonVacuumCleaners": ('XPATH', "//div[contains(text(),'Cleaners')]"),
    }

    def clickButtonVacuumCleaners(self):
        self.buttonVacuumCleaners.click()
