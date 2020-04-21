from time import sleep

import pytest

from pages.CheckoutPage import CheckoutPage
from pages.ConfirmPage import ConfirmPage
from pages.HomePage import HomePage
from pages.ShopPage import ShopPage
from utilities.BaseClass import BaseClass


# tag will be removed to baseClass
# @pytest.mark.usefixtures("setup")
class TestOne(BaseClass):

    def test_e2e_purchasing(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        shopPage = ShopPage(self.driver)

        homePage.shopItems().click()

        log.info('adding items to the cart')
        shopPage.addItemToTheCart('Blackberry')
        shopPage.addItemToTheCart("Nokia Edge")
        checkoutPage = shopPage.clickCheckoutButton()
        confirmPage = checkoutPage.verifyAndCheckout()

        # selecting delivery location
        log.info('selecting location as ind')
        confirmPage.enterLocation('ind')
        confirmPage.selectLocation("India")
        # clicking on checkbox for agreement
        confirmPage.clickAgreement()
        confirmPage.purchase()

        # confirmation message
        log.info('confirmation message received is: ' + confirmPage.getConfirmationMessage())
        confirmPage.verifyConfirmationMessage()