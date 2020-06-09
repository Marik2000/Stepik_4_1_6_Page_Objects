import time
from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "This isn't Login Page"
        #assert True

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Login email field is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login password field is not presented"
        #assert True

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "Registration email field is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD), "Registration password field is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_REPLAY), "Registration password replay field is not presented"
        #assert True

    def register_new_user(self, email, password):
        #time.sleep(2)
        self.go_to_login_page()
        self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_REPLAY).send_keys(password)
        #time.sleep(2)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()
        #time.sleep(2)
        #assert self.is_element_present(*LoginPageLocators.REGISTRATION_SUCCESSFUL), "Registration is not successful"
        assert self.is_not_element_present(*BasePageLocators.LOGIN_LINK), "User is not logged"
