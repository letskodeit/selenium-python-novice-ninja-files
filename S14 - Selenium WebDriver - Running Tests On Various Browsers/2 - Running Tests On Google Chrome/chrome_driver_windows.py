from selenium import webdriver

class ChromeDriverWindows():

    def test(self):
        # Instantiate Chrome Browser Command
        driver = webdriver.Chrome(executable_path="C:\\Users\\letsk\\workspace_python\\drivers\\chromedriver.exe")
        # Open the provided URL
        driver.get("http://www.letskodeit.com")

cc = ChromeDriverWindows()
cc.test()

# Instantiate Chrome Browser Command
# driver = webdriver.Chrome(executable_path="C:\\Users\\letsk\\workspace_python\\drivers\\chromedriver.exe")
# Open the provided URL
# driver.get("http://www.letskodeit.com")