from pages.BasePage import BasePage


class LoginPage(BasePage):

    locators = {
        "fieldUserName": ('XPATH', "//input[@autocomplete='username']"),
        "buttonContinue": ('XPATH', "//button[@id='signin-continue-btn']"),
        "errorMessage": ('XPATH', "//p[@id='errormsg']"),
    }

    def isErrorMessageVisible(self):
        self.errorMessage.is_displayed()

    def inputFieldUserName(self, name):
        self.fieldUserName.set_text(name)

    def getFieldUserName(self):
        return self.fieldUserName

    def clickButtonContinue(self):
        self.buttonContinue.click()
