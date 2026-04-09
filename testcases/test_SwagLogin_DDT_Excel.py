from time import sleep

import allure
from allure_commons.types import AttachmentType
import pytest
from pageObjects.Swag_Login_Page import SwagLoginPage
from utilities import ExcelMethods
from utilities.Logger import Loggen

@pytest.mark.usefixtures("setup")
class Test_SwagLogin_Excel:
    Excel_File_Path = "D:\\Credence\\Tushar Sir\\selenium Part  2\\Project_tusharsir\\Pytest 06\\PythonProject6\\testcases\\Test_Data\\TestData_.xlsx"
    log = Loggen.log_generator()

    @pytest.mark.ddt
    def test_Login_TC01(self,setup):

        self.log.info("test_Login_TC01 Test Case is Started")
        self.log.info("Opening Browser and Navigating to SwagLab")
        self.driver = setup
        self.lp = SwagLoginPage(self.driver)
        self.log.info("Finding the number of Rows in Excel DDT File")
        self.rows = ExcelMethods.numRows(self.Excel_File_Path,"LoginData")


        for r in range(2, self.rows + 1):
            TestCase_Status_List = []
            self.log.info("Opening Browser and Navigating to SwagLab")
            self.driver.get("https://www.saucedemo.com/")
            self.log.info("Fetching Username from Excel File for " + str(r) + "th row" )
            self.Username = ExcelMethods.readData(self.Excel_File_Path,'LoginData',r,2)
            self.log.info("Fetching Password from Excel File for " + str(r) + "th row")
            self.Password = ExcelMethods.readData(self.Excel_File_Path,'LoginData',r,3)
            self.log.info("Fetching Expected Result from Excel File for " + str(r) + "th row")
            self.Expected_Result = ExcelMethods.readData(self.Excel_File_Path,"LoginData",r,4)
            self.log.info("Entering Username in Swaglab for " + str(r) + "th row")
            self.lp.Enter_Username(self.Username)
            self.log.info("Entering Password in Swaglab for " + str(r) + "th row")
            self.lp.Enter_Password(self.Password)
            self.log.info("Clicking Login Button in Swaglab for " + str(r) + "th row")
            self.lp.Click_Login_Button()


            if self.lp.Validate_LoginStatus() == "Login Pass":
                self.log.info("Actual Login Pass")
                self.log.info("Writing Actual Login as Pass in Excel File for " + str(r) + "th row")
                ExcelMethods.writeData(self.Excel_File_Path,"LoginData",r,5,"Pass")

                if self.Expected_Result == "Pass":
                    self.log.info("Expected Login Pass")
                    self.log.info("Updating TestCase_Status_List as Pass")
                    TestCase_Status_List.append("Pass")
                    self.log.info("Taking Pass Screenshot")
                    self.driver.save_screenshot(
                        "D:\\Credence\\Tushar Sir\\selenium Part  2\\Project_tusharsir\\Pytest 06\\PythonProject6\\Screenshots\\test_login_TC01_PASS.png")
                    allure.attach(self.driver.get_screenshot_as_png(),name="test_Login_TC01_Pass",attachment_type=AttachmentType.PNG)
                    # self.lp.Click_BurgerMenu_Button()
                    # self.lp.Click_Logout_Button()

                elif self.Expected_Result == "Fail":
                    self.log.info("Expected Login Fail")
                    self.log.info("Updating TestCase_Status_List as Fail")
                    TestCase_Status_List.append("Fail")
                    self.log.info("Taking Fail Screenshot")
                    self.driver.save_screenshot(
                        "D:\\Credence\\Tushar Sir\\selenium Part  2\\Project_tusharsir\\Pytest 06\\PythonProject6\\Screenshots\\test_login_TC01_FAIL.png")
                    allure.attach(self.driver.get_screenshot_as_png(),name="test_Login_TC01_Fail",attachment_type=AttachmentType.PNG)
                    # self.lp.Click_BurgerMenu_Button()
                    # self.lp.Click_Logout_Button()


            elif self.lp.Validate_LoginStatus() == "Login Fail":
                self.log.info("Actual Login Pass")
                self.log.info("Writing Actual Login as Fail in Excel File for " + str(r) + "th row")
                ExcelMethods.writeData(self.Excel_File_Path,"LoginData",r,5,"Fail")

                if self.Expected_Result == "Pass":
                    self.log.info("Expected Login Pass")
                    self.log.info("Updating TestCase_Status_List as Fail")
                    TestCase_Status_List.append("Fail")
                    self.log.info("Taking Fail Screenshot")
                    self.driver.save_screenshot(
                        "D:\\Credence\\Tushar Sir\\selenium Part  2\\Project_tusharsir\\Pytest 06\\PythonProject6\\Screenshots\\test_login_TC01_FAIL.png")
                    allure.attach(self.driver.get_screenshot_as_png(),name="test_Login_TC01_Fail",attachment_type=AttachmentType.PNG)

                elif self.Expected_Result == "Fail":
                    self.log.info("Expected Login Fail")
                    self.log.info("Updating TestCase_Status_List as Pass")
                    TestCase_Status_List.append("Pass")
                    self.log.info("Taking Pass Screenshot")
                    self.driver.save_screenshot(
                        "D:\\Credence\\Tushar Sir\\selenium Part  2\\Project_tusharsir\\Pytest 06\\PythonProject6\\Screenshots\\test_login_TC01_PASS.png")
                    allure.attach(self.driver.get_screenshot_as_png(),name="test_Login_TC01_Pass",attachment_type=AttachmentType.PNG)

            if "Pass" in TestCase_Status_List:
                self.log.info("TestCase_Status_List " + str(TestCase_Status_List))
                assert True

            elif "Fail" in TestCase_Status_List:
                self.log.info("TestCase_Status_List" + str(TestCase_Status_List))
                assert False

        self.log.info("test_Login_TC01 Test Case is Completed")