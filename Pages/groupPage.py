import time
from Locators.locators import Locators
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class GroupPage:
    def __init__(self, driver):
        self.driver = driver

    # get user role count
    def get_role_count(self):
        role_count = self.driver.find_elements(By.XPATH, Locators.role_table_xpath)
        return len(role_count)

    #function for create group
    def create_group(self, group_name, group_description, min_role_required=1):
        roles = self.get_role_count()
        if roles < min_role_required:
            print(f"Can't create the group as number of roles are {roles} and you need at least {min_role_required} role to proceed...!")
        else:
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, Locators.skip_button_xpath))
            ).click()
            self.driver.execute_script("window.scrollTo(0, 0)")
            self.driver.find_element(By.ID, Locators.create_button_id).click()
            self.driver.find_element(By.XPATH, Locators.group_item_xpath).click()
            self.driver.find_element(By.XPATH, Locators.group_level_radio_button_xpath).click()
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            WebDriverWait(self.driver, 3).until(
                EC.visibility_of_element_located((By.XPATH, Locators.first_continue_button_xpath))
            ).click()
            self.driver.find_element(By.ID, Locators.groupName_textbox_id).clear()
            self.driver.find_element(By.ID, Locators.groupName_textbox_id).send_keys(group_name)
            self.driver.find_element(By.ID, Locators.groupDescription_textbox_id).send_keys(group_description)
            self.driver.find_element(By.XPATH, Locators.second_continue_button_xpath).click()
            self.driver.find_element(By.XPATH, Locators.third_continue_button_xpath).click()

            # confirm notification for group creation
            create_notification = WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located((By.XPATH, Locators.confirmation_msg_xpath))
            ).text
            assert create_notification in self.driver.page_source, "Group creation failed"
            print("Successfully added the group")

            #scroll down to done button
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            self.driver.find_element(By.XPATH, Locators.done_button_xpath).click()
            time.sleep(3)

            #confirm group created successfully
            group_elements = self.driver.find_elements(By.XPATH, Locators.group_names_class)
            group_names = [group.text for group in group_elements]
            assert "Amasha" in group_names, "Group 'Amasha' was not found!"
            print("Group 'Amasha' created successfully!")
            time.sleep(1)

    #function for update group
    def update_group(self,update_group_name,update_group_description):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Locators.skip_button_xpath))
        ).click()
        self.driver.find_element(By.ID, Locators.configuration_id).click()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.driver.find_element(By.XPATH, Locators.group_xpath).click()
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Locators.edit_button_xpath))
        ).click()
        self.driver.find_element(By.ID, Locators.update_form_name_id).send_keys(Keys.CONTROL + "a", Keys.BACKSPACE)
        self.driver.find_element(By.ID, Locators.update_form_name_id).send_keys(update_group_name)
        self.driver.find_element(By.ID, Locators.update_form_description_id).send_keys(Keys.CONTROL + "a", Keys.BACKSPACE)
        self.driver.find_element(By.ID, Locators.update_form_description_id).send_keys(update_group_description)
        self.driver.find_element(By.XPATH, Locators.update_button_xpath).click()

        # confirm notification for group update
        update_notification = WebDriverWait(self.driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, Locators.notification_xpath))
        ).text
        assert update_notification in self.driver.page_source, "Group Update failed"
        print("Successfully updated the group")

        #confirm group update
        group_elements = self.driver.find_elements(By.XPATH, Locators.group_names_class)
        group_names = [group.text for group in group_elements]
        assert update_group_name in group_names, "Group 'Amasha' has not updated successfully!"
        print(f"Group 'Amasha' updated to {update_group_name} successfully!")
        time.sleep(1)

    #function for delete the group
    def delete_group(self,delete_group_name):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Locators.skip_button_xpath))
        ).click()
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located((By.ID, Locators.configuration_id))
        ).click()
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, Locators.group_xpath))
        ).click()

        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Locators.delete_button_xpath))
        ).click()

        #wait until ok button is visible
        WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, Locators.ok_button_xpath))
        ).click()

        # confirm notification for group delete
        delete_notification = WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located((By.XPATH, Locators.notification_xpath))
        ).text
        assert delete_notification in self.driver.page_source, "Group deletion failed"
        print("Successfully deleted the group")

        # confirm group deletion
        group_elements = self.driver.find_elements(By.XPATH, Locators.group_names_class)
        group_names = [group.text for group in group_elements]
        assert delete_group_name not in group_names, "Group 'Amasha_edited' has not deleted successfully!"
        print(f"Group {delete_group_name} deleted successfully!")
        time.sleep(1)
