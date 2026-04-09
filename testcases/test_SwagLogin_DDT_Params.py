from unittest import TestCase

import pytest
from pageObjects.Swag_Login_Page import SwagLoginPage
from utilities.readconfigfile import readconfig
from utilities.Logger import Loggen
import allure
from allure_commons.types import AttachmentType


@pytest.mark.usefixtures("setup")
class Test_SwagLogin:
    # Username = readconfig.getUsername()
    # Password = readconfig.getPassword()
    log = Loggen.log_generator()

    def test_login_TC01(self,setup,DataForLogin):
        self.log.info("test_login_TC01 Test Case started")
        self.log.info("Opening webbrowser and Navigating to Swag Labs")
        self.driver = setup
        self.lp = SwagLoginPage(self.driver)
        self.log.info("Entering Username --> " + (DataForLogin[0]))
        self.lp.Enter_Username(DataForLogin[0])
        self.log.info("Entering Password --> " + (DataForLogin[1]))
        self.lp.Enter_Password(DataForLogin[1])
        self.log.info("Clicking Login Button")
        self.lp.Click_Login_Button()
        self.log.info("Validating Login Status")

        TestCase_Status_list = []
        if self.lp.Validate_LoginStatus() == "Login Pass":
            self.log.info("Actual Result Pass")
            if DataForLogin[2] == "Pass":
                self.log.info("Expected Result Pass")
                self.log.info("Updating TestCase_Status_List as 'PASS'")
                TestCase_Status_list.append("PASS")
                self.log.info("Taking Screenshot")
                self.driver.save_screenshot("D:\\Credence\\Tushar Sir\\selenium Part  2\\Project_tusharsir\\Pytest 06\\PythonProject6\\Screenshots\\test_login_TC01_PASS.png")
                allure.attach(self.driver.get_screenshot_as_png(),name="test_login_TC01_Pass",attachment_type=AttachmentType.PNG)
            elif DataForLogin[2] == "Fail":
                self.log.info("Expected Result Fail")
                self.log.info("Updating TestCase_Status_List as 'FAIL'")
                TestCase_Status_list.append("FAIL")
                self.log.info("Taking Screenshot")
                allure.attach(self.driver.get_screenshot_as_png(),name="test_login_TC01_Fail",attachment_type=AttachmentType.PNG)
                self.driver.save_screenshot("D:\\Credence\\Tushar Sir\\selenium Part  2\\Project_tusharsir\\Pytest 06\\PythonProject6\\Screenshots\\test_login_TC01_FAIL.png")

        elif self.lp.Validate_LoginStatus() == "Login Fail":
            self.log.info("Actual Result Fail")
            if DataForLogin[2] == "Pass":
                self.log.info("Expected Result Pass")
                self.log.info("Updating TestCase_Status_List as 'FAIL'")
                TestCase_Status_list.append("FAIL")
                self.log.info("Taking Screenshot")
                allure.attach(self.driver.get_screenshot_as_png(),name="test_login_TC01_Fail",attachment_type=AttachmentType.PNG)
                self.driver.save_screenshot("D:\\Credence\\Tushar Sir\\selenium Part  2\\Project_tusharsir\\Pytest 06\\PythonProject6\\Screenshots\\test_login_TC01_FAIL.png")
            elif DataForLogin[2] == "Fail":
                self.log.info("Expected Result Fail")
                self.log.info("Updating TestCase_Status_List as 'PASS'")
                TestCase_Status_list.append("PASS")
                self.log.info("Taking Screenshot")
                allure.attach(self.driver.get_screenshot_as_png(),name="test_login_TC01_Pass",attachment_type=AttachmentType.PNG)
                self.driver.save_screenshot("D:\\Credence\\Tushar Sir\\selenium Part  2\\Project_tusharsir\\Pytest 06\\PythonProject6\\Screenshots\\test_login_TC01_PASS.png")

        if "PASS" in TestCase_Status_list:
            self.log.info(TestCase_Status_list)
            assert True

        elif "FAIL" in TestCase_Status_list:
            self.log.info(TestCase_Status_list)
            assert False

        self.log.info("test_login_TC01 Test Case is Completed")




























        #     self.log.info("Validating Login Status Passed")
        #     self.log.info("Taking TC Pass Screenshot ")
        #     self.driver.save_screenshot("D:\\Credence\\Tushar Sir\\selenium Part  2\\Project_tusharsir\\Pytest 06\\PythonProject6\\Screenshots\\test_login_TC01_PASS.png")
        #     assert True
        #
        # else:
        #     self.driver.save_screenshot("D:\\Credence\\Tushar Sir\\selenium Part  2\\Project_tusharsir\\Pytest 06\\PythonProject6\\Screenshots\\test_login_TC01_FAIL.png")
        #     self.log.info("Validating Login Status Failed")
        #     self.log.info("Taking TC Fail Screenshot ")
        #     assert False
        # self.log.info("test_login_TC01 Test Case is completed")