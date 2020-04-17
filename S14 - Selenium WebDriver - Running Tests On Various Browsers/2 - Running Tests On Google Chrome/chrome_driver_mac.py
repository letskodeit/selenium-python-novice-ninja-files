from selenium import webdriver
import time

class ChromeDriverMac():

    def test(self):
        # Instantiate Chrome Browser Command
        driver = webdriver.Chrome(executable_path="/Users/atomar/Documents/workspace_python/drivers/chromedriver")
        # Open the provided URL
        driver.get("http://www.letskodeit.com")
        time.sleep(20)

cc = ChromeDriverMac()
cc.test()

# Instantiate Chrome Browser Command
# driver = webdriver.Chrome(executable_path="/Users/atomar/Documents/workspace_python/drivers/chromedriver")
# Open the provided URL
# driver.get("http://www.letskodeit.com")