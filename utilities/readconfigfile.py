import configparser

config = configparser.RawConfigParser()
config.read("D:\\Credence\\Tushar Sir\\selenium Part  2\\Project_tusharsir\\Pytest 06\\PythonProject6\\Configuration\\config.ini")

class readconfig:

    @staticmethod
    def getUsername():
        Username = config.get("login data","Username")
        return Username

    @staticmethod
    def getPassword():
        Password = config.get("login data","Password")
        return Password


