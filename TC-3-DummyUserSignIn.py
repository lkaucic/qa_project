import os
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from threading import Thread
BROWSERSTACK_USERNAME = os.environ.get("BROWSERSTACK_USERNAME") or "lukakaucic_4n65Hx"
BROWSERSTACK_ACCESS_KEY = os.environ.get("BROWSERSTACK_ACCESS_KEY") or "iTmAvqqg9iF6xDPsHTzR"
URL = os.environ.get("URL") or "https://hub.browserstack.com/wd/hub"
BUILD_NAME = "TC-3-Sign_In_Dummy"

# Most used versions of browsers found: https://gs.statcounter.com/browser-version-market-share
capabilities = [
    {
        "browserName": "Chrome",
        "browserVersion": "107.0",
        "os": "Windows",
        "osVersion": "10",
        "sessionName": "WIndows - Chrome", # test name
        "buildName": BUILD_NAME,  # Your tests will be organized within this build
    },
    {
        "browserName": "Edge",
        "browserVersion": "107",
        "os": "Windows",
        "osVersion": "10",
        "sessionName": "Windows - Edge",
        "buildName": BUILD_NAME,
    },
    {
        "browserName": "Safari",
        "browserVersion": "16",
        "os": "OS X",
        "osVersion": "Ventura",
        "sessionName": "OS - Safari",
        "buildName": BUILD_NAME,
    },
        {
        "os": "android",
        "browserName":"Chrome",
        "deviceName":"Samsung Galaxy S21",
        "osVersion": "11.0",
        "sessionName": "Android - Chrome",
        "buildName": BUILD_NAME,
    },
    {
        "os": "ios",
        "browserName":"Safari",
        "deviceName":"iPhone 13 Pro",
        "osVersion": "15.5",
        "sessionName": "iOS - Safari",
        "buildName": BUILD_NAME,
    },
]
def get_browser_option(browser):
    switcher = {
        "chrome": ChromeOptions(),
        "firefox": FirefoxOptions(),
        "edge": EdgeOptions(),
        "safari": SafariOptions(),
    }
    return switcher.get(browser, ChromeOptions())
def run_session(cap):
    bstack_options = {
        "osVersion": cap["osVersion"],
        "buildName": cap["buildName"],
        "sessionName": cap["sessionName"],
        "userName": BROWSERSTACK_USERNAME,
        "accessKey": BROWSERSTACK_ACCESS_KEY
    }
    if "os" in cap:
        bstack_options["os"] = cap["os"]
    if "deviceName" in cap:
        bstack_options['deviceName'] = cap["deviceName"]
    if "deviceOrientation" in cap:
        bstack_options["deviceOrientation"] = cap["deviceOrientation"]
    if cap['browserName'] in ['ios']:
        cap['browserName'] = 'safari'
    options = get_browser_option(cap["browserName"].lower())
    if "browserVersion" in cap:
        options.browser_version = cap["browserVersion"]
    options.set_capability('bstack:options', bstack_options)
    if cap['browserName'].lower() == 'samsung':
        options.set_capability('browserName', 'samsung')
    driver = webdriver.Remote(
        command_executor=URL,
        options=options)
    try:
        driver.get("https://bstackdemo.com/")
        WebDriverWait(driver, 10).until(EC.title_contains("StackDemo"))

        # Go to Login Page
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div/div[1]/div/div/div[2]/nav/a'))).click()

        # Username Field
        username = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/form/div[2]/div[1]/div/div[1]')
        username.click()
        dummy_user = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/form/div[2]/div[1]/div[2]/div/div/div[2]/div[1]')
        dummy_user.click()

        # Password Field
        password = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/form/div[2]/div[2]/div/div[1]')
        password.click()
        dummy_pass = driver.find_element(By.XPATH,'/html/body/div/div[2]/div/form/div[2]/div[2]/div[2]/div/div/div[2]/div')
        dummy_pass.click()

        # Sign In
        WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[2]/div/form/div[2]/button"))).click()

        current_link = driver.current_url
        if current_link == "https://bstackdemo.com/?signin=true":
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "User signed in!"}}')
    except NoSuchElementException as err:
        message = "Exception: " + str(err.__class__) + str(err.msg)
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": ' + json.dumps(message) + '}}')
    except Exception as err:
        message = "Exception: " + str(err.__class__) + str(err.msg)
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": ' + json.dumps(message) + '}}')
    # Stop the driver
    driver.quit()
for cap in capabilities:
    Thread(target=run_session, args=(cap,)).start()