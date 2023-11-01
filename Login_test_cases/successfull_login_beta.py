import time
import logging
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
# Import the necessary exception classes
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException



class SproutsaiAutomation:
    def __init__(self, username='dj', log_file='Login_test_cases.log'):
        # Configure logging
        self.logger = logging.getLogger(username)
        self.logger.setLevel(logging.INFO)

        # Check if the logger already has a file handler
        if not any(isinstance(handler, logging.FileHandler) for handler in self.logger.handlers):
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
        
        try:
            
            self.logger.info('')
            
            # Create the driver instance and set up the browser
            options = webdriver.ChromeOptions()
            chrome_driver_path = r'C:\Users\dhana\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'
            chrome_driver_service = Service(executable_path=chrome_driver_path)
            self.driver = webdriver.Chrome(service=chrome_driver_service, options=options)
            self.logger.info(f"success driver is found")

            home_url = "https://beta.sproutsai.com/"
            login_url = "https://beta.sproutsai.com/login"
            self.home_url = home_url
            self.log_in_url = login_url
            
        except Exception as e:
            self.logger.error(f"Failed to initialize the driver")

    def login(self, username, password, test_name=''):
        self.logger.info(f"Test Case : {test_name}")
        try:
            try:
                self.driver.get(self.log_in_url)

            except Exception as e:
                print(e)
                
            else:
                try:
                    # Find the email input element by its attributes using CSS selector
                    email_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="email"][placeholder="Enter Email"]')))
                    email_input.clear()
                    email_input.send_keys(username)
                    self.logger.info(f"email_input is entered")

                    # Find the password input element by its attributes using CSS selector
                    password_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="password"][placeholder="Password"]')))
                    password_input.clear()
                    password_input.send_keys(password)
                    self.logger.info(f"password_input is entered")
                except Exception as e:
                    self.logger.error(f"Failed to enter the email and password")

                else:
                    # Find the login button and click it
                    login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')))
                    login_button.click()
                    self.logger.info(f"login_button is clicked")
                    time.sleep(5)
                    try:
                        error_element = self.driver.find_element(By.XPATH,"//*[text()='Invalid email or password. Please try again.']")
                        self.logger.info('wrong password or username')
                    except Exception as e:
                        pass

                finally:
                    self.logger.info(f"exceution completed")

        except Exception as e:
            self.logger.error(f"Failed TO LOGIN ")



    def close(self):
        self.driver.quit()




def initialize_sproutsai(username='dj', log_file='Login_test_cases.log'):
    return SproutsaiAutomation(username, log_file)

