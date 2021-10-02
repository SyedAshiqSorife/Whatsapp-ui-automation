from selenium import webdriver
import time
import unittest
import sys
import os

from Locator.locators import Locator
from Pages.homePage import HomePage
import HtmlTestRunner
sys.path.append(os.path.join(os.path.dirname(__file__), ".", "."))


class WhatsappTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path=Locator.executable_file)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_one(self):
        driver = self.driver
        driver.get("https://web.whatsapp.com/")
        home = HomePage(driver)
        col1 = home.load_data()
        for cell in range(len(col1)):
            contact = str(col1[cell].value)
            home.show_number(contact)
        time.sleep(2)

    def test_two(self):
        driver = self.driver
        driver.get("https://web.whatsapp.com/")
        home = HomePage(driver)
        col1 = home.load_data()
        for cell in range(len(col1)):
            contact = str(col1[cell].value)
            home.send_message(contact, "Hi!there")
        time.sleep(2)

    def test_three(self):
        driver = self.driver
        driver.get("https://web.whatsapp.com/")
        home = HomePage(driver)
        col1 = home.load_data()
        for cell in range(len(col1)):
            contact = str(col1[cell].value)
            home.write_sent(contact, cell)
        time.sleep(2)

    def test_five(self):
        driver = self.driver
        driver.get("https://web.whatsapp.com/")
        home = HomePage(driver)
        home.logout()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=Locator.report_output))
