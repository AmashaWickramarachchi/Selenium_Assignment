import time
import unittest
from selenium import webdriver
from Pages.groupPage import GroupPage
from Pages.loginPage import LoginPage
from Utils.config import USERNAME, PASSWORD,EDIT_GROUP_NAME,EDIT_GROUP_DESCRIPTION

class TestUpdateGroup(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.delete_all_cookies()

    def test_e_mgt_groups_edit(self):
        driver = self.driver
        driver.get("https://uem.mgt.entgra.net/endpoint-mgt/devices")

        #Login
        login_page = LoginPage(driver)
        login_page.login(USERNAME,PASSWORD)

        #update group
        group_page = GroupPage(driver)
        group_page.update_group(EDIT_GROUP_NAME, EDIT_GROUP_DESCRIPTION)
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Update test completed")

if __name__ == '__main__':
    unittest.main()