from selenium.webdriver.common.by import By

from pages.ConfirmPage import ConfirmPage


class CheckoutPage:
    __verify_Checkout = (By.XPATH, "//button[@class='btn btn-success']")

    # to get tests driver object, so when calling we send the driver to this class
    def __init__(self, driver):
        self.driver = driver

    # after clicking on checkout, next page is Confirmation page
    # that's why we are returning ConfirmPage
    def verifyAndCheckout(self):
        self.driver.find_element(*CheckoutPage.__verify_Checkout).click()
        return ConfirmPage(self.driver)
