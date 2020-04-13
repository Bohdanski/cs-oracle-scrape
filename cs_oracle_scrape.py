"""
Main working script, with block and inline comments to explain the code.
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
        # Look for the C&S Oracle logo. This logo should be visable
        # at all times, if it is not, the page must be refreshed.
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
            # Additional methods for interacting with elements may be defined
            # here, but should ideally be limited to ID, Class Name, and xPath
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
            # If the element is unable to be clicked, call the refresh method
            # and check if the page needs to be refreshed.
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
        # Click on the out of stock dashboard.
        click_element('//*[@title="Customer Detail Export Dashboard - Standard SL Export"]', "xpath")

        # Click the dropdown arrow for the Timeframe prompt.
        click_element("promptDropDownButton", "class")

        # Click the WTD (Week to Date) option.
        click_element('//*[@title="WTD"]', "xpath")

        # Click apply.
        click_element("gobtn", "id")

        # Click export.
        click_element('//*[@title="Export to different format"]', "xpath")

        # Click the pop-up menu to select the method for export.
        click_element('//*[@title="Download columnar data"]', "xpath")

        # Click the "Tab Delimited Format" option.
        click_element('//*[@aria-label="Tab delimited Format"]', "xpath")

        # Click "OK" to close out of the pop-up.
        click_element('//*[@name="OK"]', "xpath")
    finally:
        try:
            # Click logout to end the session instance.
            click_element("logout", "id")
        finally:
            # Delete all cookies, close the browser, and exit the script.
            driver.delete_all_cookies()
            driver.close()
            exit()

if __name__ == "__main__":
    driver = webdriver.Chrome(".\chromedriver_win32\chromedriver.exe")
    main()
