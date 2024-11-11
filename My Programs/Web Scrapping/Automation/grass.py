from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from seleniumbase import Driver
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

def accept_cookies(driver):
    """Click the cookie consent button if it appears."""
    try:
        cookie_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".chakra-button.css-1fjpdqi"))
        )
        cookie_button.click()
        print("Cookie consent accepted.")
    except Exception as e:
        print(f"No cookie consent button found or clickable: {e}")

def fill_signup_form(driver, username, email, password):
    """Fill the signup form with generated data."""
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "field-:rb:"))).send_keys(username)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "field-:ra:"))).send_keys(email)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "field-:rc:"))).send_keys(password)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "field-:rd:"))).send_keys(password)

        # Check both terms and conditions checkboxes
        terms_checkboxes = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".chakra-checkbox__control.css-i88593"))
        )
        for checkbox in terms_checkboxes:
            checkbox.click()

        # Handle the captcha manually if needed
        print("Please solve the CAPTCHA manually if required.")
    except Exception as e:
        print(f"Error filling signup form: {e}")


def submit_signup_form(driver):
    """Submit the signup form."""
    try:
        signup_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".chakra-button.css-b4gyfj")))
        signup_button.click()
    except Exception as e:
        print(f"Error submitting signup form: {e}")


# ----------------------------------------
# 4. Selenium Functions for Login
# ----------------------------------------

def fill_login_form(driver, username, password):
    """Fill the login form with provided credentials."""
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "field-:r7:"))).send_keys(username)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "field-:r8:"))).send_keys(password)
    except Exception as e:
        print(f"Error filling login form: {e}")


def submit_login_form(driver):
    """Submit the login form."""
    try:
        login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".chakra-button.css-b4gyfj")))
        login_button.click()
    except Exception as e:
        print(f"Error submitting login form: {e}")


def signup_account(driver, target_url_signup):
    """Sign up a new account with random data."""
    username = generate_username()
    email = generate_email()
    password = generate_password()

    driver.get(target_url_signup)
    sleep(2)  # Wait for the page to load
    
    # Accept cookies if the button appears
    accept_cookies(driver)

    try:
        fill_signup_form(driver, username, email, password)
        submit_signup_form(driver)
        print(f"Account created for {username} with email {email}")
        
        # After signup, proceed to the next page
        sleep(2)  # Wait for the next page to load
        login_page(driver, username, password)  # Proceed to login with generated credentials
    except Exception as e:
        print(f"Error during signup for {username}: {e}")


def login_page(driver, username, password):
    """Login to the account."""
    target_url_login = "https://app.getgrass.io/"  # Replace with actual login URL
    driver.get(target_url_login)
    sleep(2)  # Wait for the page to load

    try:
        fill_login_form(driver, username, password)
        submit_login_form(driver)
        print(f"Logged in successfully with username: {username}")
        sleep(5)  # Wait a few seconds after login before looping back to registration
    except Exception as e:
        print(f"Error during login for {username}: {e}")


# ----------------------------------------
# Debuging
# ----------------------------------------

def fill_signup_form(driver, username, email, password):
    """Fill the signup form with generated data."""
    try:
        print("Filling username field")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "field-:rb:"))).send_keys(username)
        print("Filling email field")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "field-:ra:"))).send_keys(email)
        print("Filling password field")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "field-:rc:"))).send_keys(password)
        print("Filling confirm password field")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "field-:rd:"))).send_keys(password)

        # Check both terms and conditions checkboxes
        print("Selecting terms and conditions checkboxes")
        terms_checkboxes = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".chakra-checkbox__control.css-i88593"))
        )
        for checkbox in terms_checkboxes:
            checkbox.click()

        # Handle the captcha manually if needed
        print("Please solve the CAPTCHA manually if required.")
    except Exception as e:
        print(f"Error filling signup form: {e}")



# ----------------------------------------
# Main Program Execution
# ----------------------------------------

# Initialize SeleniumBase WebDriver
driver = Driver(uc=True)  # 'uc' for undetected Chrome

# Target URLs
target_url_signup = "https://app.getgrass.io/register"  # Replace with actual signup URL

# Set how many accounts you want to create
num_accounts = 1

# Loop to create multiple accounts and log in
for _ in range(num_accounts):
    signup_account(driver, target_url_signup)
    sleep(5)  # Pause between account creations

# Close the browser when done
driver.quit()
