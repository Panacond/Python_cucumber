from pages.base_page import BasePage


class LoginPage(BasePage):

    locators = {
        "field_user_name": ('XPATH', "//input[@autocomplete='username']"),
        "button_continue": ('XPATH', "//button[@id='signin-continue-btn']"),
        "error_message": ('XPATH', "//p[@id='errormsg']"),
    }

    def is_error_message_visible(self):
        self.error_message.is_displayed()

    def input_field_user_name(self, name):
        self.field_user_name.set_text(name)

    def get_field_user_name(self):
        return self.field_user_name

    def click_button_continue(self):
        self.button_continue.click()
