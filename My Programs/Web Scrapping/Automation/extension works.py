from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
import string

class SignupLoginAutomation:
    def __init__(self, chrome_driver_path, extension_path, target_url_signup, target_url_login, num_accounts=1):
        self.chrome_driver_path = chrome_driver_path
        self.extension_path = extension_path
        self.target_url_signup = target_url_signup
        self.target_url_login = target_url_login
        self.num_accounts = num_accounts
        self.driver = None

    def initialize_browser(self):
        """Initialize the browser and open the signup page."""
        chrome_options = Options()
        service = Service(executable_path=self.chrome_driver_path)
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

        # Open signup page in a new tab
        self.driver.get(self.target_url_signup)
        time.sleep(5)  # Wait for the page to load

    def generate_username(self, length=8):
        """Generate a random username."""
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    def generate_email(self):
        """Generate a random email address."""
        return f"{self.generate_username()}@example.com"

    def generate_password(self, length=12):
        """Generate a random password."""
        return ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))

    def bypass_captcha(self, url):
        """Bypass the captcha by reconnecting and clicking the captcha."""
        try:
            # Open and reconnect if necessary
            self.driver.uc_open_with_reconnect(url, 10)
            # Click the captcha using seleniumbase method (ensure you have seleniumbase installed)
            self.driver.uc_gu_click_captcha()  
            time.sleep(2)  # Give time for captcha to process
        except Exception as e:
            print(f"Captcha bypass attempt failed: {e}")
            

    def fill_signup_form(self, username, email, password):
        """Fill the signup form with generated data."""
        self.driver.find_element(By.ID, "basic_username").send_keys(username)
        self.driver.find_element(By.ID, "basic_email").send_keys(email)
        self.driver.find_element(By.ID, "basic_password").send_keys(password)
        self.driver.find_element(By.ID, "basic_confirm_password").send_keys(password)
        self.driver.find_element(By.ID, "basic_referral_code").send_keys("DsKWpmUv3K9qiZX")  # Referral code
        self.driver.find_element(By.ID, "basic_agree").click()  # Agree to terms and conditions

    def submit_signup_form(self):
        """Submit the signup form."""
        self.driver.find_element(By.CSS_SELECTOR, ".ant-btn.css-ve8idd.ant-btn-primary.ant-btn-color-primary.ant-btn-variant-solid.ant-btn-lg.ant-btn-block.mt-8").click()

    def proceed_to_login(self):
        """Click the button to proceed to the login page."""
        try:
            login_button = self.driver.find_element(By.CSS_SELECTOR, ".ant-btn.css-ve8idd.ant-btn-primary.ant-btn-color-primary.ant-btn-variant-solid.ant-btn-lg.ant-btn-block")
            login_button.click()
            print("Proceeding to login page...")
            time.sleep(5)  # Wait for the login page to load
        except Exception as e:
            print(f"Error proceeding to login: {e}")

    def fill_login_form(self, username, password):
        """Fill the login form with provided credentials."""
        self.driver.find_element(By.ID, "basic_user").send_keys(username)
        self.driver.find_element(By.ID, "basic_password").send_keys(password)

    def submit_login_form(self):
        """Submit the login form."""
        self.driver.find_element(By.CSS_SELECTOR, ".ant-btn.css-ve8idd.ant-btn-primary.ant-btn-color-primary.ant-btn-variant-solid.ant-btn-lg.ant-btn-block").click()

    def interact_with_extension(self):
        """Interact with the extension (click the activate button) only after login is successful."""
        try:
            self.driver.execute_script("""
                let button = document.querySelector("img.cursor-pointer[src*='img-button-activate']");
                if (button) {
                    button.click();
                } else {
                    console.log("Button not found");
                }
            """)
        except Exception as e:
            print("Error interacting with extension:", e)

    def signup_account(self):
        """Sign up a new account with random data."""
        username = self.generate_username()
        email = self.generate_email()
        password = self.generate_password()

        # Sign up process
        self.driver.get(self.target_url_signup)
        time.sleep(5)  # Wait for the page to load
        
        self.bypass_captcha(self.target_url_signup)  # Bypass captcha before filling out signup form
        
        try:
            self.fill_signup_form(username, email, password)
            self.submit_signup_form()
            print(f"Account created for {username} with email {email}")
            
            # After signup, proceed to the login page
            time.sleep(2)  # Wait for the next page to load
            self.proceed_to_login()  # Proceed to the login page
            self.login_page(username, password)  # Proceed to login with generated credentials
        except Exception as e:
            print(f"Error during signup for {username}: {e}")

    def login_page(self, username, password):
        """Login to the account."""
        self.driver.get(self.target_url_login)
        time.sleep(2)  # Wait for the page to load

        self.bypass_captcha(self.target_url_login)  # Bypass captcha before filling out login form

        try:
            self.fill_login_form(username, password)
            self.submit_login_form()
            print(f"Logged in successfully with username: {username}")
            time.sleep(5)  # Wait a few seconds after login
        except Exception as e:
            print(f"Error during login for {username}: {e}")

    def install_extension_after_login(self):
        """Install the extension and interact with it after login is complete."""
        chrome_options = Options()
        chrome_options.add_extension(self.extension_path)
        service = Service(executable_path=self.chrome_driver_path)
        self.driver.quit()  # Quit the previous driver instance
        
        # Initialize the browser with extension
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.driver.get(self.target_url_login)  # Revisit the login page
        time.sleep(5)  # Wait for the page to load

        # Now that the user is logged in, interact with the extension
        self.interact_with_extension()

    def run(self):
        """Run the complete automation loop."""
        self.initialize_browser()

        # Loop to create multiple accounts and log in
        for _ in range(self.num_accounts):
            self.signup_account()
            time.sleep(5)  # Pause between account creations

            # Install and interact with the extension only after login is complete
            self.install_extension_after_login()

        # Close the browser when done
        self.driver.quit()


# Paths for the chromedriver and extension
chrome_driver_path = r"C:\Users\Abdul Moiz Ali\Desktop\Automation\chromedriver-win64\chromedriver.exe"
extension_path = r"C:\Users\Abdul Moiz Ali\Desktop\Automation\nodepay.crx"
target_url_signup = "https://app.nodepay.ai/register"  # Replace with actual signup URL
target_url_login = "https://app.nodepay.ai/login"  # Replace with actual login URL

# Initialize the automation object
automation = SignupLoginAutomation(chrome_driver_path, extension_path, target_url_signup, target_url_login, num_accounts=1)

# Run the automation process
automation.run()