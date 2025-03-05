from selenium.webdriver.common.by import By
from Locators.locators import Locators

class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    def login(self,username,password):
        self.driver.find_element(By.ID, Locators.username_textBox_id).clear()
        self.driver.find_element(By.ID, Locators.username_textBox_id).send_keys(username)

        self.driver.find_element(By.ID, Locators.password_testBox_id).clear()
        self.driver.find_element(By.ID, Locators.password_testBox_id).send_keys(password)

        self.driver.find_element(By.XPATH, Locators.continue_button_xpath).click()
        self.driver.find_element(By.ID, Locators.allow_button_id).click()
