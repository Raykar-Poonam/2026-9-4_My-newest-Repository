import pytest
from selenium import webdriver





# def pytest_addoption(parser):
#     parser.addoption("--browser")
#
# @pytest.fixture()
# def setup(request):
#     browser = request.config.getoption("--browser")
#
#     if browser == "chrome":
#         driver = webdriver.Chrome()
#         print("Test Run - Chrome Browser")
#     elif browser == "firefox":
#         driver = webdriver.Firefox()
#         print("Test Run - Firefox Browser")
#     elif browser == "safari":
#         driver = webdriver.Safari()
#         print("Test Run - Safari Browser")
#     elif browser == "edge":
#         driver = webdriver.Edge()
#         print("Test Run - Edge Browser")
#     else:
#         driver = webdriver.Chrome()
#
#     driver.maximize_window()
#     driver.get("https://www.saucedemo.com/")
#     driver.refresh()
#     driver.implicitly_wait(10)
#     yield driver
#     driver.quit()






@pytest.fixture(params=[("standard_user","secret_sauce","Pass"),
                        ("standard_user1","secret_sauce","Fail"),
                        ("standard_user","secret_sauce1","Fail"),
                        ("standard_user1","secret_sauce1","Fail")])
def DataForLogin(request):
    return request.param



















# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
#
# @pytest.fixture()
# def setup():
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.maximize_window()
#     driver.get("https://www.saucedemo.com/")
#     # driver.implicitly_wait(10)
#
#     yield driver
#     driver.quit()




@pytest.fixture()
def setup():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    # driver.implicitly_wait(10)
    yield driver
    driver.quit()

