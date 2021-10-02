import openpyxl as excel
import time
from selenium.webdriver.common.keys import Keys
import sys
import os
from Locator.locators import Locator
sys.path.append(os.path.join(os.path.dirname(__file__), ".", "."))


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.search_box_xpath = Locator.search_box_xpath
        self.search_item_class = Locator.search_item_class
        self.message_box_xpath = Locator.message_box_xpath
        self.menu_bar_xpath = Locator.menu_bar_xpath
        self.logout_button_xpath = Locator.logout_button_xpath
        self.file = Locator.file

    def load_data(self):
        file = self.file
        file_load = excel.load_workbook(file)
        sheet = file_load.active
        col1 = sheet['A']

        return col1

    def search_box(self):
        search_box = self.driver.find_element_by_xpath(self.search_box_xpath)
        time.sleep(4)
        return search_box

    def show_number(self, contact):
        search_box = self.search_box()
        search_box.clear()
        search_box.send_keys(contact)

    def send_message(self, contact, message):
        self.show_number(contact)
        time.sleep(3)
        self.driver.find_element_by_class_name(self.search_item_class).click()
        message_box = self.driver.find_element_by_xpath(self.message_box_xpath)
        message_box.send_keys(message)
        time.sleep(2)
        message_box.send_keys(Keys.ENTER)

    def write_sent(self, contact, cell):
        self.send_message(contact, "check")
        file_load = excel.load_workbook(self.file)
        sheet = file_load.active
        col2 = sheet['B']
        col2[cell].value = 'sent'
        file_load.save(self.file)

    def logout(self):
        menu_bar = self.driver.find_element_by_xpath(self.menu_bar_xpath)
        menu_bar.click()
        time.sleep(2)
        self.driver.find_element_by_xpath(self.logout_button_xpath).click()
