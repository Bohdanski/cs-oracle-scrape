"""
Crawls through CS Orcale DB to extract OOS information
"""

import os
import sys

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class WebCrawler():
    def __init__(self):
        self.driver = webdriver.Chrome("./chromedriver_win32/chromedriver.exe")

    def check_refresh(self):
        """
        Check if Oracle DB is prompting Adobe Flash Update.
        """
        try:
            # Look for the C&S Oracle logo. This logo should be visable
            # at all times, if it is not, the page must be refreshed.
            self.driver.find_element_by_class_name("HeaderLogo")
        except NoSuchElementException:
            return True
        return False

    def click_element(self, path, method, delay):
        """
        Main method to interact with different webpage elements.
        Paramaeters are the path or id of the element that is being interacted with
        as well as the method Selenium is using to find the element.
        """
        while True:
            try:
                # Additional methods for interacting with elements may be defined
                # here, but should ideally be limited to ID, Class Name, and xPath
                if method == "xpath":
                    element = self.driver.find_element_by_xpath(path)
                elif method == "class":
                    element = self.driver.find_element_by_class_name(path)
                elif method == "id":
                    element = self.driver.find_element_by_id(path)
                else:
                    raise NameError("The specified method is not defined.")

                element.click()
                sleep(delay)
                break
            except Exception:
                # If the element is unable to be clicked, call the refresh method
                # and check if the page needs to be refreshed.
                while self.check_refresh() == True:
                    self.driver.refresh()
                    sleep(5)

    def login(self):
        """
        Takes in user credentials and logs into the website
        """
        self.driver.get("https://tinyurl.com/yx6l85d8")

        sleep(5)

        username = os.environ.get("CS_USER")
        username_field = self.driver.find_element_by_name("username")
        username_field.send_keys(username)

        password = os.environ.get("CS_PASS")
        password_field = self.driver.find_element_by_name("password")
        password_field.send_keys(password)

        password_field.send_keys(Keys.ENTER)

    def run(self):
        while True:
            try:
                self.login()

                # Click on the out of stock dashboard.
                self.click_element('//*[@title="Customer Detail Export Dashboard - Standard SL Export"]', "xpath", 15)

                # Click the dropdown arrow for the Timeframe prompt.
                self.click_element("promptDropDownButton", "class", 1)

                # Click the WTD (Week to Date) option.
                self.click_element('//*[@title="WTD"]', "xpath", 1)

                # Click apply.
                self.click_element("gobtn", "id", 10)

                # Click export.
                self.click_element('//*[@title="Export to different format"]', "xpath", 1)

                # Click the "Excel 2007+" option.
                self.click_element('//*[@aria-label="Excel 2007+"]', "xpath", 1)

                # Click "OK" to close out of the pop-up.
                self.click_element('//*[@name="OK"]', "xpath", 1)
            except:
                # Click logout to end the session instance.
                self.click_element("logout", "id", 5)

                break
            finally:
                # Click logout to end the session instance.
                self.click_element("logout", "id", 5)
                
                # Delete all cookies, close the browser, and exit the script.
                self.driver.delete_all_cookies()
                self.driver.close()
                sys.exit(0)


def main():
    crawler = WebCrawler()
    crawler.run()


if __name__ == "__main__":
    main()
