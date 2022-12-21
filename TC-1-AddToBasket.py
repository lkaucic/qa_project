import os
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from threading import Thread
BROWSERSTACK_USERNAME = os.environ.get("BROWSERSTACK_USERNAME") or "lukakaucic_4n65Hx"
BROWSERSTACK_ACCESS_KEY = os.environ.get("BROWSERSTACK_ACCESS_KEY") or "iTmAvqqg9iF6xDPsHTzR"
URL = os.environ.get("URL") or "https://hub.browserstack.com/wd/hub"
BUILD_NAME = "TC-1-Add_To_Basket"

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

        # Filter only Samsung products
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/main/div[1]/div[2]/label/span'))).click()

        # Get text of an product - Galaxy S20 with XPath when products are filtered
        item_on_page = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/p'))).text

        # Click the 'Add to cart' button if it is visible
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div/div/main/div[2]/div[2]/div[4]'))).click()

        # Check if the Cart pane is visible
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "float-cart__content")))

        # Get text of product in cart
        item_in_cart = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div/div/div[2]/div[2]/div[2]/div/div[3]/p[1]'))).text

        # Verify whether the product (Galaxy S20) is added to cart
        if item_on_page == item_in_cart:
            # Set the status of test as 'passed' or 'failed' based on the condition; if item is added to cart
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Galaxy S20 has been successfully added to the cart!"}}')
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