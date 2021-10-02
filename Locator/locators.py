class Locator:

    # environment setup
    file = "E:/assignments/whatsappUi/contacts.xlsx"
    report_output = 'E:/assignments/whatsappUi/Reports'
    executable_file = r'E:/assignments/whatsappUi/chromedriver.exe'

    # paths
    search_box_xpath = '//*[@id="side"]/div[1]/div/label/div/div[2]'
    search_item_class = '_3m_Xw'
    message_box_xpath = '//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]'
    menu_bar_xpath = '//*[@id="side"]/header/div[2]/div/span/div[3]/div/span'
    logout_button_xpath = '//*[@id="side"]/header/div[2]/div/span/div[3]/span/div[1]/ul/li[4]'
