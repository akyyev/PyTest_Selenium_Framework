from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from utilities.BaseClass import BaseClass


class HomePage:
    __shop = (By.CSS_SELECTOR, "a[href*='shop']")

    __name = (By.NAME, 'name')

    __email = (By.NAME, 'email')

    __password = (By.CSS_SELECTOR, "input[type='password']")

    __gender = (By.ID, 'exampleFormControlSelect1')

    __loveIceCream = (By.ID, 'exampleCheck1')

    __submit = (By.CSS_SELECTOR, "input[type='submit']")

    __submit_msg = (By.XPATH, "//div[contains(@class, 'alert alert-success')]")

    # to get tests driver object, so when calling we send the driver to this class
    def __init__(self, driver):
        self.driver = driver

    def shopItems(self):
        # * is to deserialize the tuple
        return self.driver.find_element(*HomePage.__shop)

    def type_name(self, name):
        self.driver.find_element(*self.__name).send_keys(name)

    def type_email(self, email):
        self.driver.find_element(*self.__email).send_keys(email)

    def type_password(self, password):
        temp = self.driver.find_element(*self.__password)
        temp.clear()
        temp.send_keys(password)

    def select_gender(self, gender):
        dropDown = Select(self.driver.find_element(*self.__gender))
        dropDown.select_by_visible_text(gender.capitalize())

    def love_ice_cream(self, yes_or_no):
        if yes_or_no == 'yes':
            self.driver.find_element(*self.__loveIceCream).click()

    def submitForm(self):
        self.driver.find_element(*self.__submit).click()

    def get_submit_msg(self):
        return self.driver.find_element(*self.__submit_msg).text
