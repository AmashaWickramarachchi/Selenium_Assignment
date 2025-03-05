import time
import unittest
from selenium import webdriver
from Pages.groupPage import GroupPage
from Pages.loginPage import LoginPage
from Utils.config import USERNAME, PASSWORD,EDIT_GROUP_NAME

class TestDeleteGroup(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.delete_all_cookies()

    def test_e_mgt_groups_delete(self):
        driver = self.driver
        driver.get("https://uem.mgt.entgra.net/endpoint-mgt/devices")

        #Login
        login_page = LoginPage(driver)
        login_page.login(USERNAME,PASSWORD)

        #update group
        group_page = GroupPage(driver)
        group_page.delete_group(EDIT_GROUP_NAME)
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Delete test completed")

if __name__ == '__main__':
    unittest.main()