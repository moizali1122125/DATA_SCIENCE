# ----------------------------------------
# 1. Install Libraries
# ----------------------------------------

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import pyautogui

from seleniumbase import Driver
from selenium.webdriver.common.by import By
from time import sleep
import random
import string

# ----------------------------------------
# 2. Random Data Generator Functions
# ----------------------------------------

def generate_username(length=8):
    """Generate a random username."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_email():
    """Generate a random email address."""
    return f"{generate_username()}@example.com"

def generate_password(length=12):
    """Generate a random password."""
    return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))


# ----------------------------------------
# 3. Selenium Functions for Signup
# ----------------------------------------

def bypass_captcha(url):
    """Try to bypass captcha by reconnecting and clicking the captcha."""
    try:
        driver.uc_open_with_reconnect(url, 10)  # Open and reconnect if necessary
        driver.uc_gu_click_captcha()  # Click the captcha using seleniumbase method
        sleep(2)  # Give time for captcha to process
    except Exception as e:
        print(f"Captcha bypass attempt failed: {e}")


def fill_signup_form(username, email, password):
    """Fill the signup form with generated data."""
    driver.find_element(By.ID, "basic_username").send_keys(username)
    driver.find_element(By.ID, "basic_email").send_keys(email)
    driver.find_element(By.ID, "basic_password").send_keys(password)
    driver.find_element(By.ID, "basic_confirm_password").send_keys(password)
    driver.find_element(By.ID, "basic_referral_code").send_keys("DsKWpmUv3K9qiZX")  # Referral code
    driver.find_element(By.ID, "basic_agree").click()  # Agree to terms and conditions


def submit_signup_form():
    """Submit the signup form."""
    driver.find_element(By.CSS_SELECTOR, ".ant-btn.css-ve8idd.ant-btn-primary.ant-btn-color-primary.ant-btn-variant-solid.ant-btn-lg.ant-btn-block.mt-8").click()


def signup_account():
    """Sign up a new account with random data."""
    username = generate_username()
    email = generate_email()
    password = generate_password()

    driver.get(target_url_signup)
    sleep(2)  # Wait for the page to load
    
    bypass_captcha(target_url_signup)  # Try to bypass captcha on signup page
    
    try:
        fill_signup_form(username, email, password)
        submit_signup_form()
        print(f"Account created for {username} with email {email}")
        
        # After signup, proceed to the next page
        sleep(2)  # Wait for the next page to load
        proceed_to_login()  # Proceed to the login page
        login_page(username, password)  # Proceed to login with generated credentials
    except Exception as e:
        print(f"Error during signup for {username}: {e}")


# ----------------------------------------
# 4. Selenium Functions for Login
# ----------------------------------------

def proceed_to_login():
    """Click the button to proceed to the login page."""
    try:
        # Clicking the button on the second page that takes you to the login page
        login_button = driver.find_element(By.CSS_SELECTOR, ".ant-btn.css-ve8idd.ant-btn-primary.ant-btn-color-primary.ant-btn-variant-solid.ant-btn-lg.ant-btn-block")
        login_button.click()
        print("Proceeding to login page...")
        sleep(2)  # Wait for the login page to load
    except Exception as e:
        print(f"Error proceeding to login: {e}")


def fill_login_form(username, password):
    """Fill the login form with provided credentials."""
    driver.find_element(By.ID, "basic_user").send_keys(username)
    driver.find_element(By.ID, "basic_password").send_keys(password)


def submit_login_form():
    """Submit the login form."""
    driver.find_element(By.CSS_SELECTOR, ".ant-btn.css-ve8idd.ant-btn-primary.ant-btn-color-primary.ant-btn-variant-solid.ant-btn-lg.ant-btn-block").click()


def login_page(username, password):
    """Login to the account."""
    driver.get(target_url_login)
    sleep(2)  # Wait for the page to load

    bypass_captcha(target_url_login)  # Try to bypass captcha on login page

    try:
        fill_login_form(username, password)
        submit_login_form()
        print(f"Logged in successfully with username: {username}")
        sleep(5)  # Wait a few seconds after login before looping back to registration
    except Exception as e:
        print(f"Error during login for {username}: {e}")

# ----------------------------------------
# 5. Install & Active Extension
# ----------------------------------------

# Set up Chrome options to load the extension directly
chrome_options = Options()

# Path to unpacked extension folder 1. Go to chrome://extensions/ & find Extension ID 
# 2. Go to C:\Users\<Your_Username>\AppData\Local\Google\Chrome\User Data\Profile Name\Extensions\
# 3. Find ID name Folder & Copy path & paste
chrome_options.add_argument(r"C:\Users\Abdul Moiz Ali\AppData\Local\Google\Chrome\User Data\Default\Extensions\lgmpfmgeabnnlemejacfljbmonaomfmm")

# Path to your ChromeDriver
chrome_driver_path = r"C:\Users\Abdul Moiz Ali\Desktop\New folder\chromedriver-win64\chromedriver.exe"

# Initialize ChromeDriver with the specified options
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.maximize_window()
time.sleep(5)  # Wait for the extension to fully load

try:
    # Open the extension via Chrome’s UI, usually accessible by typing the extension URL
    driver.get("chrome://extensions")
    time.sleep(2)

    # Access the extension popup
    driver.execute_script('''window.open("chrome-extension://lgmpfmgeabnnlemejacfljbmonaomfmm/popup.html", "_blank");''')
    time.sleep(3)  # Wait for the popup to open
    
    # Interact with the button in the extension
    driver.switch_to.window(driver.window_handles[1])  # Switch to the extension's popup tab
    activate_button = driver.find_element(By.CSS_SELECTOR, ".cursor-pointer")  # Assuming CSS class selector
    activate_button.click()
    print("Extension activated successfully.")

except Exception as e:
    print(f"An error occurred while activating the extension: {e}")

# Close the browser
time.sleep(5)
driver.quit()


# ----------------------------------------
# Main Program Execution
# ----------------------------------------

# Initialize SeleniumBase WebDriver
driver = Driver(uc=True)  # 'uc' for undetected Chrome

# Target URLs
target_url_signup = "https://app.nodepay.ai/register"  # Replace with actual signup URL
target_url_login = "https://app.nodepay.ai/login"  # Replace with actual login URL

# Set how many accounts you want to create
num_accounts = 1

# Loop to create multiple accounts and log in
for _ in range(num_accounts):
    signup_account()
    sleep(5)  # Pause between account creations

# Close the browser when done
driver.quit()