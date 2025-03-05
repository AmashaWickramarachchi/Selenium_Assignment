import time
import unittest
from selenium import webdriver
from Pages.groupPage import GroupPage
from Pages.loginPage import LoginPage
from Utils.config import USERNAME, PASSWORD,GROUP_NAME,GROUP_DESCRIPTION

class TestCreateGroup(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_e_mgt_group_creates_parent(self):
        driver = self.driver
        driver.get("https://uem.mgt.entgra.net/endpoint-mgt/devices")

        #Login
        login_page = LoginPage(driver)
        login_page.login(USERNAME,PASSWORD)

        #create group
        group_page = GroupPage(driver)
        group_page.create_group(GROUP_NAME,GROUP_DESCRIPTION)
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Create test completed")

if __name__ == '__main__':
    unittest.main()