from selenium.webdriver.common.by import By

from pages.CheckoutPage import CheckoutPage


class ShopPage:
    __products = (By.XPATH, "//div[@class='card h-100']")
    __checkoutButton = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    # to get tests driver object, so when calling we send the driver to this class
    def __init__(self, driver):
        self.driver = driver

    def getProducts(self):
        return self.driver.find_elements(*ShopPage.__products)

    def addItemToTheCart(self, name):
        # products   = //div[@class='card h-100']
        # blackberry = //div[@class='card h-100']/div/h4/a
        # add_button = //div[@class='card h-100']/div[2]/button
        for product in self.getProducts():
            if product.find_element_by_xpath('div/h4/a').text == name:
                print(product.find_element_by_xpath('div/h4/a').text)
                product.find_element_by_xpath('div[2]/button').click()

    # right after clicking on checkout button Checkout page will open
    # that's why we returned the object of Checkout page
    def clickCheckoutButton(self):
        self.driver.find_element(*ShopPage.__checkoutButton).click()
        return CheckoutPage(self.driver)
