import pytest
from pageObjects.Swag_Login_Page import SwagLoginPage
from utilities.readconfigfile import readconfig
from utilities.Logger import Loggen

@pytest.mark.usefixtures("setup")
class Test_SwagLogin:
    Username = readconfig.getUsername()
    Password = readconfig.getPassword()
    log = Loggen.log_generator()

    def test_login_TC01(self,setup,DataForLogin):
        self.log.info("test_login_TC01 Test Case started")
        self.log.info("Opening webbrowser and Navigating to Swag Labs")
        self.driver = setup
        self.lp = SwagLoginPage(self.driver)
        self.log.info("Entering Username --> " + self.Username )
        self.lp.Enter_Username(self.Username)
        self.log.info("Entering Password --> " + self.Password)
        self.lp.Enter_Password(self.Password)
        self.log.info("Clicking Login Button")
        self.lp.Click_Login_Button()
        self.log.info("Validating Login Status")

        if self.lp.Validate_LoginStatus() == "Login Pass":
            self.log.info("Validating Login Status Passed")
            self.log.info("Taking TC Pass Screenshot ")
            self.driver.save_screenshot("D:\\Credence\\Tushar Sir\\selenium Part  2\\Project_tusharsir\\Pytest 06\\PythonProject6\\Screenshots\\test_login_TC01_PASS.png")
            assert True

        else:
            self.driver.save_screenshot("D:\\Credence\\Tushar Sir\\selenium Part  2\\Project_tusharsir\\Pytest 06\\PythonProject6\\Screenshots\\test_login_TC01_FAIL.png")
            self.log.info("Validating Login Status Failed")
            self.log.info("Taking TC Fail Screenshot ")
            assert False

        self.log.info("test_login_TC01 Test Case is completed")