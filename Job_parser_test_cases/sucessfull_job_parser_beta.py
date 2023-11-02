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

            #replace the driver path here
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
        self.driver.maximize_window()
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


    def successfull_post_new_job(self, file_path_exist=False, file_path='', test_name='test_1',company_name_not_found=False):
        try:
            self.logger.info('  ---------------------------------------------------------  ')
            self.logger.info(f' Name the test case : { test_name } ')
            self.logger.info('')
            self.logger.info('entered the post_new_job')
 
            self.driver.get(self.home_url)
            time.sleep(5)

            try:
                # Select the element by its text content
                element = WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[text()="Post new job"]'))
                )
                element.click()
                self.logger.info("Clicked 'Post new job'")
            except Exception as e:
                self.logger.error("error in  clicking 'Post new job' button")
            
            else:
                try:
                    upload = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "upload-document-first-state")))
                    upload.click()
                    self.logger.info("Clicked 'Upload document'")

                except Exception as e:
                    self.logger.error("error in  clicking 'Upload document'")

                else:
                    try:
                        if file_path_exist:
                            time.sleep(2)
                            pyautogui.write(file_path)
                            pyautogui.press("enter")
                            self.logger.info("Entered file path and confirmed")
                    except Exception as e:
                        self.logger.error("error in  file_path ")

                    try:
                        wait = WebDriverWait(self.driver, 60)
                        autofill_button = wait.until(
                            EC.presence_of_element_located((By.XPATH, '//button[text()="Click to autofill"]'))
                        )
                    except Exception as e:
                        self.logger.error("error in  the document 'Uploading' ")
                        self.driver.get(self.home_url)

                    else:
                        document_name_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "uper-text")))
                        document_name = document_name_element.text
                        self.logger.info(f" Uploaded the document : { document_name } ")
                        
                        click_to_fill = WebDriverWait(self.driver, 10).until(
                            EC.element_to_be_clickable((By.XPATH, '//*[text()="Click to autofill"]'))
                        )
                        click_to_fill.click()

                        try:
                            start_time = time.time()

                            autofill_button = WebDriverWait(self.driver, 310).until(
                                EC.presence_of_element_located(
                                    (By.XPATH, '//button[text()="Parsed"] | //button[text()="Parsing failed"]')
                                )
                            )

                            elapsed_time = time.time() - start_time

                            if "Parsed" in autofill_button.text:
                                autofill_button.click()
                                self.logger.info("clicked the autofill_button")
                            elif "Parsing failed" in autofill_button.text:
                                self.logger.error("Parsing failed")
                                pass
                            else:
                                pass
                        except Exception as e:
                            self.logger.error('error in Parsed field')

                        else:
                            if company_name_not_found :
                                try:
                                    expected_text = "Company Details Required: Please fill in the necessary information about your company"
                                    # Check if the element's text matches the expected text
                                    element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//span[contains(., '{}')]".format(expected_text))))
                                    self.logger.info("expected_text is present in the site")

                                except Exception as e:
                                    self.logger.info(' no error in company name field ')

                                else:
                                    
                                    try:
                                        if element.text == expected_text:
                                            # Wait for the element with the expected text
                                            try:
                                                element = WebDriverWait(self.driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "/html/body/div[1]/div[1]/form/main/div[3]/div[2]/div/div[2]/div/div[1]/div[2]/span"), expected_text))
                                                self.logger.info("Element found with expected text!")


                                                # Locate the "Save company information" button by class name
                                                save_company_button = WebDriverWait(self.driver, 10).until(
                                                EC.element_to_be_clickable((By.CLASS_NAME, "save-button")))

                                                # Click the button
                                                save_company_button.click()
                                                self.logger.info("save_company_button is clicked.")

                                            except Exception as e:
                                                print("Error occurred:", e)


                                    except Exception as e:
                                        self.logger.error('error in company_name field selection when it is not parsed')

                    finally:
                        try:
                            try:
                                # Locate the input element by its name
                                Company_name_element = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.NAME, "company")))

                                # Get the value attribute
                                Company_name = Company_name_element.get_attribute("value")

                                # Print the value
                                self.logger.info(f" Company_name : { Company_name } ")

                            except Exception as e:
                                self.logger.error(f" error in getting the company_name ")

                                
                            try:
                                # Locate the input element by its name
                                job_title_element = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.NAME, "position")))

                                # Get the value attribute
                                job_title = job_title_element.get_attribute("value")
                                self.job_title = job_title

                                # Print the value
                                self.logger.info(f" job_title : { job_title } ")
                            except NoSuchElementException as e:
                                self.logger.error(f" error in getting the job_title ")
                                
                                
                            try:
                                job_description_elements = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.editor-class .public-DraftEditor-content')))
                                job_description = job_description_elements.text
                                self.logger.info(f" job_description : { job_description } ")
                                
                            except NoSuchElementException as e:
                                self.logger.error(f" error in getting the job description ")

                            except Exception as e:
                                self.logger.error(f" error in getting the job description ")

                                
                                
                            try:
                                job_types = WebDriverWait(self.driver, 2).until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/div[1]/div[1]/form/main/div[3]/div[3]/div/div/div[2]/div[3]/div//button[contains(@style, 'background: rgb(0, 185, 141);')]")))
                                for element in job_types:
                                    self.logger.info(f" job_type : { element.text } ")
        
                            except Exception as e:
                                self.logger.error(f" error in getting the job types ")

                            try:
                                Department = WebDriverWait(self.driver, 2).until(EC.presence_of_all_elements_located((By.XPATH,  "/html/body/div[1]/div[1]/form/main/div[3]/div[3]/div/div/div[2]/div[4]/div//button[contains(@style, 'background: rgb(0, 185, 141);')]")))
                                for element in Department:
                                    self.logger.info(f" Department : { element.text } ")

                            except Exception as e:
                                self.logger.error(f" error in getting the Department ")
                                
                                
                            try:
                                # Using Selenium to select the elements with the specified XPath
                                workplace_type = WebDriverWait(self.driver, 2).until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/div[1]/div[1]/form/main/div[3]/div[3]/div/div/div[4]/div[1]//button[contains(@style, 'background: rgb(0, 185, 141);')]")))
                                for element in workplace_type:
                                    self.logger.info(f" workplace_type : { element.text } ")

                            except Exception as e:
                                self.logger.error(f" error in getting the workplace_type ")

                                
                            try:
                                # Using Selenium to select the elements with the specified XPath
                                location = WebDriverWait(self.driver, 2).until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/div[1]/div[1]/form/main/div[3]/div[3]/div/div/div[4]/div[3]//button[contains(@style, 'background: rgb(0, 185, 141);')]")))
                                for element in location:
                                    self.logger.info(f" location : {element.text}")
                            except Exception as e:
                                self.logger.error(f" error in getting the location ")
                                
                                
                            try:
                                # Find all "section-skills" elements
                                skills_sections = WebDriverWait(self.driver, 2).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "section-skills")))

                                # Iterate through each skills section and retrieve heading and skills
                                for skills_section in skills_sections:
                                    try:
                                        # Find the heading element within the current skills section
                                        heading_element = skills_section.find_element(By.CSS_SELECTOR, 'input[type="text"][required]')
                                        
                                        # Extract and print the heading of the current section
                                        heading = heading_element.get_attribute("value")
                                        self.logger.info(f"---- Main Skill Category ---- : { heading } ")
                                        
                                        # Find all skill elements within the current skills section
                                        skill_elements = skills_section.find_elements(By.CLASS_NAME, "auto-complete-input")
                                        
                                        # Extract and print the skills within the current section
                                        skills = [element.get_attribute("value") for element in skill_elements]
                                        for skill in skills:
                                            self.logger.info(f" Sub Skills : { skill } ")
                                            
                                    except NoSuchElementException:
                                        pass

                            except NoSuchElementException as e:
                                self.logger.error(f" error in getting the skills ")



                            try:
                                # Find the input fields and select element by their respective names
                                currency_input = self.driver.find_element(By.NAME, 'expectedSalaryCurrency')
                                min_salary_input = self.driver.find_element(By.NAME, 'expectedSalaryMin')
                                max_salary_input = self.driver.find_element(By.NAME, 'expectedSalaryMax')
                                duration_select = self.driver.find_element(By.NAME, 'expectedSalaryDuration')

                                # Get the values of these elements
                                currency_value = currency_input.get_attribute("value")
                                min_salary_value = min_salary_input.get_attribute("value")
                                max_salary_value = max_salary_input.get_attribute("value")
                                duration_value = duration_select.get_attribute("value")

                                # Print the values
                                self.logger.info(f" Currency : {currency_value} ")
                                self.logger.info(f" Minimum Salary : {min_salary_value} ")
                                self.logger.info(f" Maximum Salary : {max_salary_value} ")
                                self.logger.info(f" Salary Duration : {duration_value} ")

                            except NoSuchElementException as e:
                                self.logger.error(f" error in getting the salary ")
                                
                                
                                
                            try:
                                # Locate all elements with the specified background color
                                Benefits_offered_Add_benefits = WebDriverWait(self.driver, 2).until(EC.presence_of_all_elements_located((By.XPATH, '//button[@style="background: rgb(0, 185, 141); transition: background-color 0.5s ease 0s;"]')))

                                # Iterate through the elements and get their text
                                for element in Benefits_offered_Add_benefits:
                                    self.logger.info(f" Benefits_offered: {element.text} ")
                            except Exception as e:
                                self.logger.error(f" error in getting the Benefits_offered ")

                                
                                
                            try:
                                # Find the "Min" input element for years of experience
                                min_input = self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Min"]')
                                min_value = min_input.get_attribute("value")
                                self.logger.info(f" Minimum Years of experience: {min_value} ")

                                # Find the "Max" input element for years of experience
                                max_input = self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Max"]')
                                max_value = max_input.get_attribute("value")
                                self.logger.info(f" Minimum Years of experience: {max_value} ")

                            except NoSuchElementException as e:
                                print(f" error in getting the years of experience ")
                                
                                
                                
                            try:
                                # Locate the dropdown element by its ID using the By method
                                dropdown = Select(self.driver.find_element(By.ID, "notice"))

                                # Get the currently selected option
                                selected_option = dropdown.first_selected_option

                                # Extract and print the value of the currently selected option
                                option = selected_option.get_attribute("value")
                                self.logger.info(f" Notice period : {option} ")

                            except NoSuchElementException as e:
                                self.logger.error(f" error in the Notice period ")
                                
                                

                        except Exception as e:
                            self.logger.error(f" error in taking the details from the webpage: {e}")

                        else:
                            try:
                                Roles_responsibilities_elements = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/form/main/div[3]/div[6]/div/div[2]/section/div[3]/div/div[2]/div/div/div/div/div/div/span/span')))
                                Roles_responsibilities = Roles_responsibilities_elements.text
                                self.logger.info(f" Roles_and_responsibilities : {Roles_responsibilities} ")

                            except NoSuchElementException as e:
                                self.logger.error(f" error in the Roles_and_responsibilities ")
                                
                                
                            try:
                                experience_education_elements = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/form/main/div[3]/div[6]/div/div[2]/section/div[4]/div/div[2]/div/div/div/div/div/div/span/span')))
                                # Get the text from the element
                                experience_education = experience_education_elements.text
                                self.logger.info(f"experience_and_education : {experience_education}")

                            except NoSuchElementException as e:
                                self.logger.error(f"experience_education not found: {e}")

                            


                    self.logger.info(f"Job Parser took {elapsed_time:.2f} seconds for parsing the job_descriptions")
                            

            finally:
                try:
                    save_and_exit = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Review post"]')))
                    save_and_exit.click()
                    self.logger.info("Save and exited Active clicked")
                        
                except Exception as e:
                    self.logger.error(f"error in  Active section {e}")

                else:
                    try:
                        Publish = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Publish this job"]')))
                        Publish.click()
                        self.logger.info("Publish clicked")

                        total_elapsed_time = time.time() - start_time
                        self.logger.info(f"Element lookup took {total_elapsed_time:.2f} seconds")
                        time.sleep(2)

                    except Exception as e:
                        self.logger.error(f" An error occurred in Publish the file {e} ")
                        self.logger.info('execution completed')

                        

        except Exception as e:
            self.logger.error(f' error in the job parser {e} ')

    def delete_job_title(self):
        job_title_element = self.driver.find_element(By.XPATH, '//div[@class="text"]/h6')

        # Extract the text of the job title
        job_title = job_title_element.text

        self.driver.get('https://beta.sproutsai.com/job/active')
        time.sleep(2)
        
        try:
            try:
                job_title_element = WebDriverWait(self.driver, 10).until(
                                        EC.element_to_be_clickable((By.XPATH, f'//span[contains(@class, "inline-block") and contains(text(), "{job_title}")]')))
                job_title_element.click()
                self.logger.info(f' clicked the job_title_element ')
            except Exception as e:
                self.logger.error(f' error in clicking the job_title_element {e}')
            
            try:
                time.sleep(2)
                menu = WebDriverWait(self.driver, 10).until(
                                        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div/div/main/div[1]/div/div[1]/div[2]/button")))
                                
                # Click the button
                menu.click()
                self.logger.info(f' clicked the menu ')
            except Exception as e:
                self.logger.error(f' error in clicking the menu {e}')


            try:
                delete_job_element = WebDriverWait(self.driver, 10).until(
                                EC.element_to_be_clickable((By.XPATH, f"//li[text()='Delete job']")))

                # Click the "Edit job" element
                delete_job_element.click()
                self.logger.info(f' clicked the delete_job_element ')
            except Exception as e:
                self.logger.error(f' error in clicking the delete_job_element {e}')


            try:
                confirm_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[1]/div/div/main/div[1]/div/div[1]/div[2]/div/div/div[2]/button[2]')))

                time.sleep(2)
                # Click the "Confirm" button
                confirm_button.click()
                time.sleep(2)
                self.logger.info(f' clicked the confirm_button ')
                self.logger.info(f' sucessfully deleted the job title {job_title} ')

            except Exception as e:
                self.logger.error(f' error in clicking the confirm_button {e}')


            

        except Exception as e:
            self.logger.error(f' error in deleted the job title {job_title}  {e} ')


    def testing_post_new_job_for_unsupportive_error(self, file_path_exist=False, file_path='', test_name='test_1'):
        try:
            self.logger.info('')
            self.logger.info('  ------------------------------------------------  ')
            self.logger.info('')
            self.logger.info(f' Name the test case : { test_name } ')
            self.logger.info('entered the post_new_job')
 
            self.driver.get(self.home_url)
            time.sleep(3)

            try:
                # Select the element by its text content
                element = WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[text()="Post new job"]'))
                )
                element.click()
                self.logger.info("Clicked 'Post new job'")
            except Exception as e:
                self.logger.error("error in  clicking 'Post new job' button")
            
            else:
                try:
                    upload = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "upload-document-first-state")))
                    upload.click()
                    self.logger.info("Clicked 'Upload document'")

                except Exception as e:
                    self.logger.error("error in  clicking 'Upload document'")

                else:
                    try:
                        if file_path_exist:
                            time.sleep(2)
                            pyautogui.write(file_path)
                            pyautogui.press("enter")
                            self.logger.info("Entered file path and confirmed")
                    except Exception as e:
                        self.logger.error("error in  file_path ")

                    try:
                        # Locate the notification element using a unique CSS selector
                        notification_element = WebDriverWait(self.driver, 20).until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, '.Toastify__toast--error div'))
                        )

                        # Check the text content of the notification
                        notification_text = notification_element.text

                        # Check if the notification contains the error message you expect
                        if "File format or size not supported" in notification_text:
                            self.logger.info("Error notification for unsupported file format detected.")
                        else:
                            self.logger.info("No error notification found.")

                    except Exception as e:
                        self.logger.error("error in  notification element ")

        except Exception as e:
            self.logger.error("error in  job parser ")



    def testing_post_new_job_for_empty_fields(self, file_path_exist=False, file_path='', test_name='test_1'):
        try:
            self.logger.info('')
            self.logger.info('  ------------------------------------------------  ')
            self.logger.info('')
            self.logger.info(f' Name the test case : { test_name } ')
            self.logger.info('entered the post_new_job')
 
            self.driver.get(self.home_url)
            time.sleep(3)

            try:
                # Select the element by its text content
                element = WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[text()="Post new job"]'))
                )
                element.click()
                self.logger.info("Clicked 'Post new job'")
            except Exception as e:
                self.logger.error("error in  clicking 'Post new job' button")
            
            else:
                try:
                    upload = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "upload-document-first-state")))
                    upload.click()
                    self.logger.info("Clicked 'Upload document'")

                except Exception as e:
                    self.logger.error("error in  clicking 'Upload document'")

                else:
                    try:
                        if file_path_exist:
                            time.sleep(2)
                            pyautogui.write(file_path)
                            pyautogui.press("enter")
                            self.logger.info("Entered file path and confirmed")
                    except Exception as e:
                        self.logger.error("error in  file_path ")

                    try:
                        wait = WebDriverWait(self.driver, 60)
                        autofill_button = wait.until(
                            EC.presence_of_element_located((By.XPATH, '//button[text()="Click to autofill"]'))
                        )
                    except Exception as e:
                        self.logger.error("error in  the document 'Uploading' ")
                        self.driver.get(self.home_url)

                    else:
                        document_name_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "uper-text")))
                        document_name = document_name_element.text
                        self.logger.info(f" Uploaded the document : { document_name } ")
                        
                        click_to_fill = WebDriverWait(self.driver, 10).until(
                            EC.element_to_be_clickable((By.XPATH, '//*[text()="Click to autofill"]'))
                        )
                        click_to_fill.click()

                        try:
                            start_time = time.time()

                            autofill_button = WebDriverWait(self.driver, 310).until(
                                EC.presence_of_element_located(
                                    (By.XPATH, '//button[text()="Parsed"] | //button[text()="Parsing failed"]')
                                )
                            )

                            elapsed_time = time.time() - start_time

                            if "Parsed" in autofill_button.text:
                                autofill_button.click()
                                self.logger.info("clicked the autofill_button")
                            elif "Parsing failed" in autofill_button.text:
                                self.logger.error("Parsing failed")
                                pass
                            else:
                                pass
                        except Exception as e:
                            self.logger.error('error in Parsed field')

                        else:

                            try:
                                # Locate the input element by its placeholder attribute using the By method
                                company_name_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[placeholder="Search here"][name="company"]')))

                                # Check if the input field is empty
                                if company_name_input.get_attribute('value')=='':
                                    # If it's empty, fill it with "N/A"
                                    self.logger.info(' -------- company_name_input is empty --------')

                            except Exception as e:
                                self.logger.error('company_name_input is not empty ')

                            try:
                                # Locate the input element by its placeholder attribute using the By method
                                job_title_input =  WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="text"][name="position"]')))

                                # Check if the input field is empty
                                if job_title_input.get_attribute('value')=='':
                                    # If it's empty, fill it with "N/A"
                                    self.logger.info('-------- job_title_input is empty --------')

                            except Exception as e:
                                self.logger.error(' job_title_input is not empty ')

                            
                            
                            try:
                                # Locate the <span> element using the By method
                                job_description_input_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/form/main/div[3]/div[3]/div/div/div[2]/div[2]/div/div[2]')))
                                time.sleep(2)
                                job_description_input_element.click()

                                # Check if the <span> element has no text content
                                if not job_description_input_element.text.strip():
                                    # If it's empty, execute JavaScript to set the text content to "N/A
                                    self.logger.info(' ------- job_description_input_element is empty --------')


                            except Exception as e:
                                self.logger.error(f' job_description_input_element is not empty {e}')

                            

                        finally:
                            try:
                                try:
                                    # Locate the input element by its name
                                    Company_name_element = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.NAME, "company")))

                                    # Get the value attribute
                                    Company_name = Company_name_element.get_attribute("value")

                                    # Print the value
                                    self.logger.info(f" Company_name : { Company_name } ")

                                except Exception as e:
                                    self.logger.error(f" error in getting the company_name ")

                                    
                                try:
                                    # Locate the input element by its name
                                    job_title_element = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.NAME, "position")))

                                    # Get the value attribute
                                    job_title = job_title_element.get_attribute("value")
                                    self.job_title = job_title

                                    # Print the value
                                    self.logger.info(f" job_title : { job_title } ")
                                except NoSuchElementException as e:
                                    self.logger.error(f" error in getting the job_title ")
                                    
                                    
                                try:
                                    job_description_elements = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.editor-class .public-DraftEditor-content')))
                                    job_description = job_description_elements.text
                                    self.logger.info(f" job_description : { job_description } ")
                                    
                                except NoSuchElementException as e:
                                    self.logger.error(f" error in getting the job description ")

                                    
                                    
                                try:
                                    job_types = WebDriverWait(self.driver, 2).until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/div[1]/div[1]/form/main/div[3]/div[3]/div/div/div[2]/div[3]/div//button[contains(@style, 'background: rgb(0, 185, 141);')]")))
                                    for element in job_types:
                                        self.logger.info(f" job_type : { element.text } ")
            
                                except Exception as e:
                                    self.logger.error(f" error in getting the job types ")

                                try:
                                    Department = WebDriverWait(self.driver, 2).until(EC.presence_of_all_elements_located((By.XPATH,  "/html/body/div[1]/div[1]/form/main/div[3]/div[3]/div/div/div[2]/div[4]/div//button[contains(@style, 'background: rgb(0, 185, 141);')]")))
                                    for element in Department:
                                        self.logger.info(f" Department : { element.text } ")

                                except Exception as e:
                                    self.logger.error(f" error in getting the Department ")
                                    
                                    
                                try:
                                    # Using Selenium to select the elements with the specified XPath
                                    workplace_type = WebDriverWait(self.driver, 2).until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/div[1]/div[1]/form/main/div[3]/div[3]/div/div/div[4]/div[1]//button[contains(@style, 'background: rgb(0, 185, 141);')]")))
                                    for element in workplace_type:
                                        self.logger.info(f" workplace_type : { element.text } ")

                                except Exception as e:
                                    self.logger.error(f" error in getting the workplace_type ")

                                    
                                try:
                                    # Using Selenium to select the elements with the specified XPath
                                    location = WebDriverWait(self.driver, 2).until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/div[1]/div[1]/form/main/div[3]/div[3]/div/div/div[4]/div[3]//button[contains(@style, 'background: rgb(0, 185, 141);')]")))
                                    for element in location:
                                        self.logger.info(f" location : {element.text}")
                                except Exception as e:
                                    self.logger.error(f" error in getting the location ")
                                    
                                    
                                try:
                                    # Find all "section-skills" elements
                                    skills_sections = WebDriverWait(self.driver, 2).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "section-skills")))

                                    # Iterate through each skills section and retrieve heading and skills
                                    for skills_section in skills_sections:
                                        try:
                                            # Find the heading element within the current skills section
                                            heading_element = skills_section.find_element(By.CSS_SELECTOR, 'input[type="text"][required]')
                                            
                                            # Extract and print the heading of the current section
                                            heading = heading_element.get_attribute("value")
                                            self.logger.info(f"---- Main Skill Category ---- : { heading } ")
                                            
                                            # Find all skill elements within the current skills section
                                            skill_elements = skills_section.find_elements(By.CLASS_NAME, "auto-complete-input")
                                            
                                            # Extract and print the skills within the current section
                                            skills = [element.get_attribute("value") for element in skill_elements]
                                            for skill in skills:
                                                self.logger.info(f" Sub Skills : { skill } ")
                                                
                                        except NoSuchElementException:
                                            pass

                                except NoSuchElementException as e:
                                    self.logger.error(f" error in getting the skills ")



                                try:
                                    # Find the input fields and select element by their respective names
                                    currency_input = self.driver.find_element(By.NAME, 'expectedSalaryCurrency')
                                    min_salary_input = self.driver.find_element(By.NAME, 'expectedSalaryMin')
                                    max_salary_input = self.driver.find_element(By.NAME, 'expectedSalaryMax')
                                    duration_select = self.driver.find_element(By.NAME, 'expectedSalaryDuration')

                                    # Get the values of these elements
                                    currency_value = currency_input.get_attribute("value")
                                    min_salary_value = min_salary_input.get_attribute("value")
                                    max_salary_value = max_salary_input.get_attribute("value")
                                    duration_value = duration_select.get_attribute("value")

                                    # Print the values
                                    self.logger.info(f" Currency : {currency_value} ")
                                    self.logger.info(f" Minimum Salary : {min_salary_value} ")
                                    self.logger.info(f" Maximum Salary : {max_salary_value} ")
                                    self.logger.info(f" Salary Duration : {duration_value} ")

                                except NoSuchElementException as e:
                                    self.logger.error(f" error in getting the salary ")
                                    
                                    
                                    
                                try:
                                    # Locate all elements with the specified background color
                                    Benefits_offered_Add_benefits = WebDriverWait(self.driver, 2).until(EC.presence_of_all_elements_located((By.XPATH, '//button[@style="background: rgb(0, 185, 141); transition: background-color 0.5s ease 0s;"]')))

                                    # Iterate through the elements and get their text
                                    for element in Benefits_offered_Add_benefits:
                                        self.logger.info(f" Benefits_offered: {element.text} ")
                                except Exception as e:
                                    self.logger.error(f" error in getting the Benefits_offered ")

                                    
                                    
                                try:
                                    # Find the "Min" input element for years of experience
                                    min_input = self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Min"]')
                                    min_value = min_input.get_attribute("value")
                                    self.logger.info(f" Minimum Years of experience: {min_value} ")

                                    # Find the "Max" input element for years of experience
                                    max_input = self.driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Max"]')
                                    max_value = max_input.get_attribute("value")
                                    self.logger.info(f" Minimum Years of experience: {max_value} ")

                                except NoSuchElementException as e:
                                    print(f" error in getting the years of experience ")
                                    
                                    
                                    
                                try:
                                    # Locate the dropdown element by its ID using the By method
                                    dropdown = Select(self.driver.find_element(By.ID, "notice"))

                                    # Get the currently selected option
                                    selected_option = dropdown.first_selected_option

                                    # Extract and print the value of the currently selected option
                                    option = selected_option.get_attribute("value")
                                    self.logger.info(f" Notice period : {option} ")

                                except NoSuchElementException as e:
                                    self.logger.error(f" error in the Notice period ")
                                    
                                    

                            except Exception as e:
                                self.logger.error(f" error in taking the details from the webpage: {e}")

                            else:
                                try:
                                    Roles_responsibilities_elements = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/form/main/div[3]/div[6]/div/div[2]/section/div[3]/div/div[2]/div/div/div/div/div/div/span/span')))
                                    Roles_responsibilities = Roles_responsibilities_elements.text
                                    self.logger.info(f" Roles_and_responsibilities : {Roles_responsibilities} ")

                                except NoSuchElementException as e:
                                    self.logger.error(f" error in the Roles_and_responsibilities ")
                                    
                                    
                                try:
                                    experience_education_elements = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/form/main/div[3]/div[6]/div/div[2]/section/div[4]/div/div[2]/div/div/div/div/div/div/span/span')))
                                    # Get the text from the element
                                    experience_education = experience_education_elements.text
                                    self.logger.info(f"experience_and_education : {experience_education}")

                                except NoSuchElementException as e:
                                    self.logger.error(f"experience_education not found: {e}")

                                try:
                                    save_and_exit = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Review post"]')))
                                    save_and_exit.click()
                                    self.logger.info("Save and exited Active clicked")
                                        
                                except Exception as e:
                                    self.logger.error(f"error in  Active section {e}")

                            


                    self.logger.info(f"Job Parser took {elapsed_time:.2f} seconds for parsing the job_descriptions")
                        

        except Exception as e:
                self.logger.error("error in finding the empty fields ")




    def close(self):
        self.driver.quit()




def initialize_sproutsai(username='dj', log_file='Login_test_cases.log'):
    return SproutsaiAutomation(username, log_file)

