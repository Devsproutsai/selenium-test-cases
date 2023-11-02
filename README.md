# selenium-test-cases

From this link download the google chrome and the google chrome driver based on your platform
https://googlechromelabs.github.io/chrome-for-testing/
![image](https://github.com/Devsproutsai/selenium-test-cases/assets/145147092/d22ae066-aaff-4741-8dcf-32f4995856e5)
---------------------------------------------------------------------------------------------------------------------------------------

* once the chrome is installed, extract the chrome driver and try to copy the path of the chrome driver.exe

  ![image](https://github.com/Devsproutsai/selenium-test-cases/assets/145147092/3162975e-3bc2-410a-b79d-f11735bae028)

---------------------------------------------------------------------------------------------------------------------------------------
* then open the file from the
  -- Job_parser_test_cases/sucessfull_job_parser_beta.py --
  
---------------------------------------------------------------------------------------------------------------------------------------
* then replace the path of the chrome_driver_path with your driver path
---------------------------------------------------------------------------------------------------------------------------------------
* just search for chrome_driver_path and then replace the path  dont remove the letter 'r' from it, just replace the path in the quotes like
---------------------------------------------------------------------------------------------------------------------------------------
**example : **
chrome_driver_path = r'C:\Users\dhana\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'

---------------------------------------------------------------------------------------------------------------------------------------
* then open the file -- test_cases_for_job_parser_beta.py --
---------------------------------------------------------------------------------------------------------------------------------------
* try to replace the paths of this files from the folder --- Pdf_files_for_testing ---- 
---------------------------------------------------------------------------------------------------------------------------------------
folder_path_for_unsupported_case = r'C:\Users\dhana\Downloads\testing_job_parser\testing-code\Pdf_files_for_testing\Unsupportive_test_cases'

---------------------------------------------------------------------------------------------------------------------------------------
folder_path_for_empty_case = r'C:\Users\dhana\Downloads\testing_job_parser\testing-code\Pdf_files_for_testing\Empty_fields_test_cases'

---------------------------------------------------------------------------------------------------------------------------------------
folder_path_for_must_parse_case = r'C:\Users\dhana\Downloads\testing_job_parser\testing-code\Pdf_files_for_testing\Must_parse_test_cases'

---------------------------------------------------------------------------------------------------------------------------------------
folder_path_for_must_not_parse_case = r'C:\Users\dhana\Downloads\testing_job_parser\testing-code\Pdf_files_for_testing\Must_not_parse_test_cases'

---------------------------------------------------------------------------------------------------------------------------------------
once the folder paths are replaced :
* then in the terminal try to run this command
pytest test_cases_for_job_parser_beta.py -k test_must_not_parse_job_parser

---------------------------------------------------------------------------------------------------------------------------------------

note : try to give the full path of the file here, if not working like 

pytest C:\Users\dhana\Downloads\testing_job_parser\selenium-test-cases\Job_parser_test_cases\test_cases_for_job_parser_beta.py -k test_must_not_parse_job_parser

---------------------------------------------------------------------------------------------------------------------------------------
note : just change the name of the function from the file, if you want to run another type of test case like : 

---------------------------------------------------------------------------------------------------------------------------------------
pytest C:\Users\dhana\Downloads\testing_job_parser\selenium-test-cases\Job_parser_test_cases\test_cases_for_job_parser_beta.py -k test_sucessfull_job_parser

