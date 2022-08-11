# This test uses http://the-internet.herokuapp.com/add_remove_elements/

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


class AddRemoveElements(unittest.TestCase):

    test_url = 'http://the-internet.herokuapp.com/add_remove_elements/'

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
    def test_a_add_remove(self):
        driver = self.driver
        # asking user how many elements are to be added and removed
        elements_add = int(input('How many elements do you want to add? '))
        elements_remove = int(
            input('How many elements do you want to remove? '))
        total_elements = elements_add - elements_remove
        # getting add button
        btn_add = driver.find_element(
            By.XPATH, '//*[@id="content"]/div/button')

        # adding elements
        for i in range(elements_add):
            # wait for add button to be clickable
            WebDriverWait(driver, 15).until(
                EC.element_to_be_clickable(btn_add))
            # "press" button
            btn_add.click()
        # option: is possible to execute the script related to button directly.
        # for i in range(elements_add):
        #    driver.execute_script("addElement()")

        # remove element, a try/catch is used in case there is no more elements to remove
        for i in range(elements_remove):
            try:
                # getting remove button (using classname for convinience)
                btn_delete = driver.find_element(
                    By.CLASS_NAME, 'added-manually')
                WebDriverWait(driver, 15).until(
                    EC.element_to_be_clickable(btn_delete))
                btn_delete.click()
            except:
                print("There is no more elements to remove")
                break

        # showing results to user
        if total_elements > 0:
            print(f"There are {total_elements} remaining")
        else:
            print("There is no elements remaining")

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
