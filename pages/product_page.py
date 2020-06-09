from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from .locators import ProductPageLocators, PageLinks, BasketPageLocators

class ProductPage(BasePage):

    def should_be_product_page(self):
        self.should_be_add_to_basket()

    def should_be_add_to_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_COST).text
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        link.click()
        self.solve_quiz_and_get_code()
        assert product_name == self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_TO_BASKET_SUCCESS).text
        assert product_cost == self.browser.find_element(*ProductPageLocators.BASKET_COST).text

    def should_be_add_to_basket_without_quiz(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_COST).text
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        link.click()
        assert product_name == self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_TO_BASKET_SUCCESS).text
        assert product_cost == self.browser.find_element(*ProductPageLocators.BASKET_COST).text

    def should_not_see_success_message_after_adding_product_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        link.click()
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_ADD_TO_BASKET_SUCCESS), \
               "Success message is presented, but should not be"

    def should_not_see_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_ADD_TO_BASKET_SUCCESS), \
               "Success message is presented, but should not be"

    def should_not_message_disappeared_after_adding_product_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        link.click()
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_ADD_TO_BASKET_SUCCESS), \
               "Success message is presented, but should not be"
