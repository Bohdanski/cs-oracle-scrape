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
        return False
    return True

def main():
    """
    Main guts of the script.
    """
    driver.get("https://tinyurl.com/yx6l85d8")

    sleep(5)

    log_in(cs_username, cs_password)

    try:
        while True:
            try:
                dashboard_link = driver.find_element_by_link_text("Customer Detail Export Dashboard - Standard SL Export")
                dashboard_link.click()
                sleep(5)
                break
            except Exception:
                while check_refresh() == False:
                    driver.refresh()
                    sleep(5)

        while True:
            try:
                drop_dwn_btn = driver.find_element_by_class_name("promptDropDownButton")
                drop_dwn_btn.click()
                sleep(5)
                break
            except Exception:
                while check_refresh() == False:
                    driver.refresh()
                    sleep(5)

        while True:
            try:
                wtd_btn = driver.find_element_by_xpath("/html/body/div[9]/div/div[2]/div[3]/span")
                wtd_btn.click()
                sleep(5)
                break
            except Exception:
                while check_refresh() == False:
                    driver.refresh()
                    sleep(5)

        while True:
            try:
                apply_btn = driver.find_element_by_id("gobtn")
                apply_btn.click()
                sleep(5)
                break
            except Exception:
                while check_refresh() == False:
                    driver.refresh()
                    sleep(5)

        while True:
            try:
                export_link = driver.find_element_by_link_text("Export")
                export_link.click()
                sleep(1)
                break
            except Exception:
                while check_refresh() == False:
                    driver.refresh()
                    sleep(5)

        while True:
            try:
                data_link = driver.find_element_by_link_text("Data")
                data_link.click
                sleep(1)
                break
            except Exception:
                while check_refresh() == False:
                    driver.refresh()
                    sleep(5)

        while True:
            try:
                csv_link = driver.find_element_by_link_text("Tab delimited Format")
                csv_link.click()
                sleep(1)
                break
            except Exception:
                while check_refresh() == False:
                    driver.refresh()
                    sleep(5)

        while True:
            try:
                ok_btn = driver.find_element_by_partial_link_text("OK")
                ok_btn.click()
                sleep(1)
                break
            except Exception:
                while check_refresh() == False:
                    driver.refresh()
                    sleep(5)
    finally:
        try:
            logout_btn = driver.find_element_by_id("logout")
            logout_btn.click()
            sleep(5)
        finally:
            driver.delete_all_cookies()
            driver.close()
            exit()

if __name__ == "__main__":
    driver = webdriver.Chrome(".\chromedriver_win32\chromedriver.exe")
    main()
