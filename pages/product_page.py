import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException # в начале файла
from .base_page import BasePage
from .locators import ProductPageLocators, PageLinks, BasketPageLocators

class ProductPage(BasePage):

    def should_be_product_page(self):
        self.should_be_add_to_basket()

    def should_be_add_to_basket(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_COST).text
        time.sleep(1)
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        link.click()
        BasePage.solve_quiz_and_get_code(self)
        time.sleep(1)
        print(product_name, self.browser.find_element(*ProductPageLocators.PRODUCT_ADD_TO_BASKET_SUCCESS).text)
        print(product_cost, self.browser.find_element(*ProductPageLocators.BASKET_COST).text)
        time.sleep(1)
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
        time.sleep(1)
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_ADD_TO_BASKET_SUCCESS), \
               "Success message is presented, but should not be"
