from selenium import webdriver


class Homepage(object):
    def __init__(self, driver):
        self.driver = driver

    def gotohomepage(self):
        self.driver.get("http://www.baidu.com")