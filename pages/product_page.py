import time, math
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
        self.browser.get(PageLinks.PRODUCT_PAGE)
        time.sleep(5)
        link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        link.click()
        self.solve_quiz_and_get_code()
        time.sleep(5)
        assert product_name in self.browser.find_element(*BasketPageLocators.PRODUCT_ADD_TO_BASKET_SUCCESS).text
        assert product_cost in self.browser.find_element(*BasketPageLocators.BASKET_COST).text

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
