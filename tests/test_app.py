# Allows this module to be called from parent directory
import sys
sys.path.insert(0,'.')

import unittest
import todolist
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class FunctionalTesting(unittest.TestCase):
    """
    Test the basic functionality of the application via Selenium. 
    Many of these tests may require updates when changes to the HTML templates are made.
    In its current state, this test module requires that the app server is already running.
    """

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_server_running(self):
        self.driver.get('http://localhost:5000')

        assert self.driver.title == 'To-Do List'

    def test_adding_task(self):
        self.driver.get('http://localhost:5000')
        starting_task_ids = [elem.get_attribute('id') for elem in self.driver.find_elements_by_xpath('//tr[@id]')]
        
        # Navigate to the New Task form
        add_task_button = self.driver.find_element_by_link_text('Add New Item')
        add_task_button.click()

        # Fill out the form with test data
        task_title_field = self.driver.find_element_by_id('taskTitle')
        task_title_field.send_keys('test_task \'\\!@#$%^&*()~;')
        target_date_field = self.driver.find_element_by_id('targetDate')
        target_date_field.send_keys('4202069')

        # Submit the New Task form, returning to home page
        target_date_field.submit()

        ending_task_ids = [elem.get_attribute('id') for elem in self.driver.find_elements_by_xpath('//tr[@id]')]

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()