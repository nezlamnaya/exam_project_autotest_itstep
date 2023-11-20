from ..pages import base_page, locators
import inspect


class SignupPage(base_page.BasePage):

    def click_account_button(self, account):
        assert self.click_element(*locators.BasePageLocators.SIGNUP, account), \
            "The element currency is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def click_signup_button(self):
        assert self.click_element(*locators.BasePageLocators.SIGNUP), \
            "The element currency is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def input_mail(self, mail):
        assert self.input_data(*locators.SignupLoginPageLocators.INPUT_MAIL, mail), \
            "The element currency is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def input_password(self, password):
        assert self.input_data(*locators.SignupLoginPageLocators.INPUT_PASSWORD, password), \
            "The element currency is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def input_confirm_password(self, confirm_password):
        assert self.input_data(*locators.SignupLoginPageLocators.INPUT_CONFIRM_PASSWORD, confirm_password), \
            "The element currency is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def input_full_name(self, full_name):
        assert self.input_data(*locators.SignupLoginPageLocators.INPUT_FULL_NAME, full_name), \
            "The element currency is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def input_number_telephone(self, number_telephone):
        assert self.input_data(*locators.SignupLoginPageLocators.INPUT_NUMBER_TELEPHONE, number_telephone), \
            "The element currency is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")
              
    def select_field(self, field):
        assert self.select_data(*locators.SignupLoginPageLocators.INPUT_FIELD, field), \
            "The element currency is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")
              
    def select_сommunity(self, community):
        assert self.select_data(*locators.SignupLoginPageLocators.INPUT_COMMUNITY, community), \
            "The element currency is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")
              
    def input_post_office(self, post_office):
        assert self.input_data(*locators.SignupLoginPageLocators.INPUT_POST_OFFICE, post_office), \
            "The element currency is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")
              
    def input_post_code(self, post_code):
        assert self.input_data(*locators.SignupLoginPageLocators.INPUT_POST_CODE, post_code), \
            "The element currency is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")
              
    def input_address(self, Address):
        assert self.input_data(*locators.SignupLoginPageLocators.INPUT_ADDRESS, Address), \
            "The element currency is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")
                      
    def select_newsletter(self, newsletter):
        assert self.click_data(*locators.SignupLoginPageLocators.SELECT_NEWSLETTER, newsletter), \
            "The element currency is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def press_button_confirm(self, confirm):
        assert self.click_element(*locators.SignupLoginPageLocators.BUTTON_CONFIRM, confirm), \
            "The element currency is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

class LoginPage(base_page.BasePage):
    
    def click_account(self,account):
        assert self.click_element(*locators.BasePageLocators.LOGIN, account), \
            "The element currency is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def input_mail(self, mail):
        assert self.input_data(*locators.SignupLoginPageLocators.INPUT_MAIL, mail), \
            "The element currency is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def input_password(self, password):
        assert self.input_data(*locators.SignupLoginPageLocators.INPUT_PASSWORD, password), \
            "The element currency is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def press_login_button(self, login_button):
        assert self.click_element(*locators.SignupLoginPageLocators.LOGIN_BUTTON, login_button), \
            "The element currency is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def is_button_logout_in_header(self):
        assert self.is_element_present(*locators.BasePageLocators.LOGOUT), \
            "Button login is not present"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")

    def press_button_logout(self):
        assert self.click_element(*locators.BasePageLocators.LOGOUT), \
            "The element currency is not present or intractable"
        print(f"{inspect.currentframe().f_code.co_name} - Ok")


    