class Locators:

    #Login page locators
    username_textBox_id = "username"
    password_testBox_id = "password"
    continue_button_xpath = "//button[contains(text(), 'Continue')]"
    allow_button_id = "approve"

    # common locators in group page
    skip_button_xpath = "//span[contains(text(),'Skip')]"
    group_names_class = "//div[@class='ant-card-meta-title']"
    notification_xpath = "//div[contains(@class, 'ant-notification-notice-description')]"
    configuration_id = "configurations"
    group_xpath = "//span[contains(text(),'Groups')]"

    # role table locator
    role_table_xpath = "//table/tbody/tr"

    # group create locators
    create_button_id = "create-btn"
    group_item_xpath = "//span[contains(text(),'Group')]"
    group_level_radio_button_xpath = "//span[contains(text(),'Top level group')]"
    first_continue_button_xpath = "(//button/span[text()='Continue'])[1]"
    groupName_textbox_id = "basic_GroupName"
    groupDescription_textbox_id = "basic_GroupDescription"
    second_continue_button_xpath = "(//button/span[text()='Continue'])[2]"
    third_continue_button_xpath = "(//button/span[text()='Continue'])[3]"
    confirmation_msg_xpath = "//div[@class='ant-result-title']"
    done_button_xpath = "//span[text()='Done']"

    # group edit locators
    edit_button_xpath = "//span[@class='anticon anticon-edit']"
    update_form_name_id = "groupForm_name"
    update_form_description_id = "groupForm_description"
    update_button_xpath = "//button/span[text()='Update']"

    # group delete locators
    delete_button_xpath = "//span[@class='anticon anticon-delete']"
    ok_button_xpath = "//button/span[text()='OK']"