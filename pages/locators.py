from selenium.webdriver.common.by import By

class PageLinks():
    PRODUCT_PAGE = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_REPLAY = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")
    REGISTRATION_SUCCESSFUL = (By.CSS_SELECTOR, "icon-ok-sign")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main h1")
    PRODUCT_COST = (By.CSS_SELECTOR, "div.col-sm-6.product_main p.price_color")
    PRODUCT_ADD_TO_BASKET_SUCCESS = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-success:nth-child(1) strong")
    BASKET_COST = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-info.fade.in strong")

class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    EMPTY_BASKET_MESSAGE_AFTER_DELETE_ITEMS = (By.CSS_SELECTOR, ".alertinner p:nth-child(1)")
    ITEMS_TO_BAY = (By.CSS_SELECTOR, ".col-sm-6.h3")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group .btn.btn-default:nth-child(1)")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
