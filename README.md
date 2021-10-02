# Whatsapp-ui-automation

To run the code please first setup the environments
 change the paths in Locator folder locators.py file
 
Then go to the project folder in cmd or pycharm IDE then run following commands to test

# To full test run 
python -m unittest

python -m unittest Tests.testcases.WhatsappTest.test_one

python -m unittest Tests.testcases.WhatsappTest.test_two

python -m unittest Tests.testcases.WhatsappTest.test_three

python -m unittest Tests.testcases.WhatsappTest.test_five

# Usage
 **I use Page Object Model for organize the project in a order
 ** use Python Selenium and Chrome webdriver
 ** Use openpyxl package for accessing excel file
 **Use Unittest for testing
 **Use HtmlTestRunner for generate test reports

# Issues 
 ## Please run again if first time get error. There have some path issues
 ## I could not complete test four because i was not able to access the last msg path,
 it changed everytime so i could not get the right result, thats why there is no implement of test four. But i tried
   ###
   messages = list()
    soup = BeautifulSoup(driver.page_source, "html.parser")
    for i in soup.find_all("div", class_="_2wUmf message-out focusable-list-item"):
        print("div[i]")
        message = i.find("span", class_="selectable-text")
        if message:
            message2 = message.find("span")
            if message2:
                messages.append(message2.text)
    messages = list(filter(None, messages))

    messages_len = len(messages)
    last_msg = messages[messages_len-1]
    print(last_msg)
    ###
 In the above code i can access the last message sent by a user but can't get the 'path' or 'aria-level' value
 
# Difficulties face
  **In my system python, selenium and pycharm were not installed so i have install and setup it
  **when i try to run there face some WebGL problem and i solve it
  **I face problems to identify paths
  
In this project i learned many new things and it will be helpful for me. Thank you
