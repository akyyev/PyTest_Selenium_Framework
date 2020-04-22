from time import sleep

import pytest

from TestData.HomePageData import HomePageData
from pages.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        log.info('First name is ' + getData['name'])

        homePage.type_name(getData['name'])
        homePage.type_email(getData['email'])
        homePage.type_password('hello123')
        homePage.love_ice_cream('yes')
        homePage.select_gender(getData['gender'])
        homePage.submitForm()
        alertText = homePage.get_submit_msg()
        assert ('Success!' in alertText)
        self.driver.refresh()

    # DDT test
    @pytest.fixture(params=HomePageData.test_homePage_data)
    def getData(self, request):
        return request.param


    def test_formSubmission2(self, getDataFromExcel):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        log.info('First name is ' + getDataFromExcel['firstname'])

        homePage.type_name(getDataFromExcel['firstname'])
        homePage.type_email(getDataFromExcel['email'])
        homePage.type_password('password')
        homePage.love_ice_cream('yes')
        homePage.select_gender(getDataFromExcel['gender'])
        homePage.submitForm()
        alertText = homePage.get_submit_msg()
        assert ('Success!' in alertText)
        self.driver.refresh()

    # DDT test
    @pytest.fixture(params=HomePageData.getAllDataAsListOfDict())
    def getDataFromExcel(self, request):
        return request.param
