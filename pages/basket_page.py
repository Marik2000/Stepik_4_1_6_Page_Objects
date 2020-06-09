from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from .locators import ProductPageLocators, PageLinks, BasePageLocators, BasketPageLocators

class BasketPage(BasePage):

    def should_be_open_basket_page(self):
        link = self.browser.find_element(*BasePageLocators.VIEW_BASKET_BUTTON)
        link.click()

    def should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.ITEMS_TO_BAY), \
               "Basket is not empty"

    def should_be_empty_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
               "Empty message is not presented"
