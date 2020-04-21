import inspect
import logging

import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:
    pass

    def waitUntilPresenceAndReturn(self, locator_tuple):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(locator_tuple))
        return self.driver.find_element(*locator_tuple)

    def selectOptionByText(self, locator, text):
        drop_down = Select(locator)
        drop_down.select_by_visible_text(text)

    def getLogger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)

        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s : %(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # accepts filehandler object
        logger.setLevel(logging.DEBUG)
        return logger