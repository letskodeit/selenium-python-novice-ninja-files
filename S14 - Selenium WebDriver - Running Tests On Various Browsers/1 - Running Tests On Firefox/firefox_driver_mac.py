from selenium import webdriver


class FirefoxDriverMac():
    def testMethod(self):
        # Instantiate FF Browser Command
        driver = webdriver.Firefox(executable_path="/Users/atomar/Documents/workspace_python/drivers/geckodriver")
        # Open the provided URL
        driver.get("http://www.letskodeit.com")

ff = FirefoxDriverMac()
ff.testMethod()