from selenium import webdriver


class RunFFTests():
    def testMethod(self):
        # Instantiate the FF Browser Command
        driver = webdriver.Firefox(executable_path="C:\\Users\\letsk\\workspace_python\\drivers\\geckodriver.exe")
        #  Open the provided URL
        driver.get("http://www.letskodeit.com")

ff = RunFFTests()
ff.testMethod()