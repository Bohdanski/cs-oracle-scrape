"""
Program test script to be used for updates and bug fixes.
"""

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from credentials import cs_username, cs_password

def log_in(username, password):
    """
    Takes in user credentials and logs into the website
    """
    username_field = driver.find_element_by_name("username")
    username_field.send_keys(username)

    password_field = driver.find_element_by_name("password")
    password_field.send_keys(password)

    password_field.send_keys(Keys.ENTER)
    sleep(5)

def check_refresh():
    """
    Check if Oracle DB is prompting Adobe Flash Update.
    """
    try:
        driver.find_element_by_class_name("HeaderLogo")
    except NoSuchElementException:
        return True
    return False

def click_element(path, method):
    """
    Main function to interact with different webpage elements.
    Paramaeters are the path or id of the element that is being interacted with
    as well as the method Selenium is using to find the element.
    """
    while True:
        try:
            if method == "xpath":
                element = driver.find_element_by_xpath(path)
            elif method == "class":
                element = driver.find_element_by_class_name(path)
            elif method == "id":
                element = driver.find_element_by_id(path)
            else:
                raise NameError("The specified method is not defined.")
            element.click()
            sleep(5)
            break
        except Exception:
            while check_refresh() == True:
                driver.refresh()
                sleep(5)

def main():
    """
    Main guts of the script.
    """
    driver.get("https://tinyurl.com/yx6l85d8")

    sleep(5)

    log_in(cs_username, cs_password)

    try:
        click_element('//*[@title="Customer Detail Export Dashboard - Standard SL Export"]', "xpath")

        click_element("promptDropDownButton", "class")

        click_element('//*[@title="WTD"]', "xpath")

        click_element("gobtn", "id")

        click_element('//*[@title="Export to different format"]', "xpath")

        click_element('//*[@title="Download columnar data"]', "xpath")

        click_element('//*[@aria-label="Tab delimited Format"]', "xpath")

        click_element('//*[@name="OK"]', "xpath")
    finally:
        try:
            click_element("logout", "id")
        finally:
            driver.delete_all_cookies()
            driver.close()
            exit()

if __name__ == "__main__":
    driver = webdriver.Chrome(".\chromedriver_win32\chromedriver.exe")
    main()
