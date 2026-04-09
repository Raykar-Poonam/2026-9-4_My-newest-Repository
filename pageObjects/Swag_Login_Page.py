from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SwagLoginPage:
    Input_Username_ID = "user-name"
    Input_Password_ID = "password"
    Button_LoginButton_ID = "login-button"
    Button_BurgerMenuButton_ID = "react-burger-menu-btn"
    Button_LogoutButton_ID = "logout_sidebar_link"
    Text_Validate_LoginStatus_XPATH = "//div[@class='app_logo']"


    def __init__(self,driver):
        self.driver = driver

    def Enter_Username(self,username):
        # WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.ID,self.Input_Username_ID))).send_keys(username)
        self.driver.find_element(By.ID,self.Input_Username_ID).send_keys(username)

    def Enter_Password(self,password):
        self.driver.find_element(By.ID,self.Input_Password_ID).send_keys(password)

    def Click_Login_Button(self):
        self.driver.find_element(By.ID,self.Button_LoginButton_ID).click()

    def Click_BurgerMenu_Button(self):
        self.driver.find_element(By.ID,self.Button_BurgerMenuButton_ID).click()

    def Click_Logout_Button(self):
        self.driver.find_element(By.ID,self.Button_LogoutButton_ID).click()

    def Validate_LoginStatus(self):
        try:
            self.driver.find_element(By.XPATH,self.Text_Validate_LoginStatus_XPATH)
            return "Login Pass"

        except:
            return "Login Fail"