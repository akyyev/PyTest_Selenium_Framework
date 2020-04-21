from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from utilities.BaseClass import BaseClass


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    __delivery = (By.ID, 'country')

    # clicking on checkbox for agreement
    __agreementBox = (By.CSS_SELECTOR, "label[for='checkbox2']")

    __purchaseButton = (By.CSS_SELECTOR, "[type='submit']")

    __conf_message = (By.XPATH, "//div[contains(@class, 'alert-dismissible')]")

    def enterLocation(self, location):
        self.driver.find_element(*ConfirmPage.__delivery).send_keys(location)

    def selectLocation(self, location_full):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, location_full)))
        self.driver.find_element_by_link_text(location_full).click()

    def clickAgreement(self):
        self.driver.find_element(*self.__agreementBox).click()

    def purchase(self):
        self.driver.find_element(*self.__purchaseButton).click()

    def verifyConfirmationMessage(self):
        print(self.getConfirmationMessage())
        assert 'Success! Thank you!' in self.getConfirmationMessage()

    def getConfirmationMessage(self):
        return self.driver.find_element(*self.__conf_message).text
