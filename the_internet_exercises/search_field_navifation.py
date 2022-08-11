# A quick navigation through google site

import unittest
# webdriver will connect and manage the browser used for tests.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# webdriverwait and expected conditions are use to allow some time to browser to perform actions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# By alows selection using html tags, classes, ids, css selectors or xpath
from selenium.webdriver.common.by import By
# pyunitreport will run the test and save reports in html format.
from pyunitreport import HTMLTestRunner
# time will be used to actually see the tests, as they happen to fast.
from time import sleep


class NavigationTest(unittest.TestCase):

    test_url = 'http://google.com'

    # methods setUp and tearDown must be classmethods and use cls instead of self
    @classmethod
    def setUpClass(cls):
        # point to the webdriver (in this case Chrome) service.
        cls.driver = webdriver.Chrome(service=Service(
            '/Users/pedro/Documents/DEVELOPER/PYTHON/chromedriver'))
        driver = cls.driver
        driver.implicitly_wait(15)
        # load a web site.
        driver.get(cls.test_url)

    # test methods name must start with test_ and they will be passed in alphabetical order

    def test_browser_navigation(self):
        driver = self.driver
        # getting google's search bar
        element_input = driver.find_element(
            By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        # remove any text that could be present
        element_input.clear()
        # search something
        element_input.send_keys("stack overflow")
        # execute search
        sleep(1)
        element_input.submit()
        # wait 5 seconds and return back
        sleep(5)
        driver.back()
        # wait 2 seconds and go forward
        sleep(2)
        driver.forward()
        # wait 2 seconds and refresh page
        sleep(2)
        driver.refresh()
        # wait 2 sec and go to other site
        sleep(2)
        driver.get('https://www.coches.net/')

    # tearDown will shut down browser

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


# main method, not needed if tests are to be taken in bulk, but it's here in case
# this test is wanted to be run alone
if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(
        output='reports', report_name='add_remove_report'
    ))
