import pytest
from sucessfull_job_parser_beta import initialize_sproutsai
import time
import os

folder_path_for_unsupported_case = r'C:\Users\dhana\Downloads\testing_job_parser\testing-code\Pdf_files_for_testing\Unsupportive_test_cases'

folder_path_for_empty_case = r'C:\Users\dhana\Downloads\testing_job_parser\testing-code\Pdf_files_for_testing\Empty_fields_test_cases'

folder_path_for_must_parse_case = r'C:\Users\dhana\Downloads\testing_job_parser\testing-code\Pdf_files_for_testing\Must_parse_test_cases'

folder_path_for_must_not_parse_case = r'C:\Users\dhana\Downloads\testing_job_parser\testing-code\Pdf_files_for_testing\Must_not_parse_test_cases'

error_jd_paths= []
empty_jd_paths = []
must_parse_jd_paths = []
must_not_parse_jd_paths = []

if os.path.exists(folder_path_for_unsupported_case) and os.path.isdir(folder_path_for_unsupported_case):
    files = os.listdir(folder_path_for_unsupported_case)

    for i in files:
        error_jd_paths.append(folder_path_for_unsupported_case+'\\'+str(i))


if os.path.exists(folder_path_for_empty_case) and os.path.isdir(folder_path_for_empty_case):
    files = os.listdir(folder_path_for_empty_case)

    for i in files:
        empty_jd_paths.append(folder_path_for_empty_case+'\\'+str(i))

if os.path.exists(folder_path_for_must_parse_case) and os.path.isdir(folder_path_for_must_parse_case):
    files = os.listdir(folder_path_for_must_parse_case)

    for i in files:
        must_parse_jd_paths.append(folder_path_for_must_parse_case+'\\'+str(i))

if os.path.exists(folder_path_for_must_not_parse_case) and os.path.isdir(folder_path_for_must_not_parse_case):
    files = os.listdir(folder_path_for_must_not_parse_case)

    for i in files:
        must_not_parse_jd_paths.append(folder_path_for_must_not_parse_case+'\\'+str(i))




def test_sucessfull_job_parser():
    log_file = 'test_cases1.log'  # Specify the log file here
    sproutsai = initialize_sproutsai(username='Dhanunjaya', log_file=log_file)

    sproutsai.login(username='pankaj+natera@sproutsai.com', password='Demo@123', test_name=' ---- sucessfull login ----')

    for i in must_parse_jd_paths:
        sproutsai.successfull_post_new_job(file_path_exist=True,file_path=i,test_name=' ------ normal job parsing without handling any errors -------- ')

        time.sleep(1)
        if "Job created successfully" in sproutsai.driver.page_source:
            sproutsai.logger.info(" --------------------")
            sproutsai.logger.info(" ----------- Success Test case -- job parsed successfully ---------")
            sproutsai.logger.info(" --------------------")
            sproutsai.delete_job_title()
            
        else:
            sproutsai.logger.info(" --------------------")
            sproutsai.logger.error(" ---------- Job parsed test failed ------------- ")
            sproutsai.logger.info(" --------------------")

            sproutsai.successfull_post_new_job(file_path_exist=True,file_path=i,test_name=' -------- successfull job parsing with company name handling ------- ',company_name_not_found=True)
            time.sleep(1)
            if "Job created successfully" in sproutsai.driver.page_source:
                sproutsai.logger.info(" --------------------")
                sproutsai.logger.info(" ----------- Success job parsing with company name handling -- job parsed successfully ---------")
                sproutsai.logger.info(" --------------------")
                sproutsai.delete_job_title()
             
            else:
                sproutsai.logger.error(" ---------- job parsed test failed ------------- ")
   
    sproutsai.close()


def test_must_not_parse_job_parser():
    log_file = 'test_cases_must_not_parse.log'  # Specify the log file here
    sproutsai = initialize_sproutsai(username='Dhanunjaya', log_file=log_file)

    sproutsai.login(username='pankaj+natera@sproutsai.com', password='Demo@123', test_name=' ---- sucessfull login ----')

    for i in must_not_parse_jd_paths:
        sproutsai.successfull_post_new_job(file_path_exist=True,file_path=i,test_name=' ------ normal job parsing without handling any errors -------- ')

        time.sleep(1)
        if "Job created successfully" in sproutsai.driver.page_source:
            sproutsai.logger.info(" --------------------")
            sproutsai.logger.info(" ----------- Success Test case -- job parsed successfully ---------")
            sproutsai.logger.info(" --------------------")
            sproutsai.delete_job_title()
            
        else:
            sproutsai.logger.info(" --------------------")
            sproutsai.logger.error(" ---------- Job parsed test failed ------------- ")
            sproutsai.logger.info(" --------------------")

            sproutsai.successfull_post_new_job(file_path_exist=True,file_path=i,test_name=' -------- successfull job parsing with company name handling ------- ',company_name_not_found=True)
            time.sleep(1)
            if "Job created successfully" in sproutsai.driver.page_source:
                sproutsai.logger.info(" --------------------")
                sproutsai.logger.info(" ----------- Success job parsing with company name handling -- job parsed successfully ---------")
                sproutsai.logger.info(" --------------------")
                sproutsai.delete_job_title()
             
            else:
                sproutsai.logger.error(" ---------- job parsed test failed ------------- ")
   
    sproutsai.close()



def test_unsupportive_format_testing():
    log_file = 'unsupportive_format_test_cases.log'  # Specify the log file here
    sproutsai = initialize_sproutsai(username='Dhanunjaya', log_file=log_file)

    sproutsai.login(username='pankaj+natera@sproutsai.com', password='Demo@123', test_name=' ---- sucessfull login ----')

    for i in error_jd_paths:
        sproutsai.testing_post_new_job_for_unsupportive_error(file_path_exist=True,file_path=i,test_name=' ------ testing with unsupportive/corruted jds -------- ')

        time.sleep(1)
        if "File format or size not supported" in sproutsai.driver.page_source:
            sproutsai.logger.info(" --------------------")
            sproutsai.logger.info(" ----------- Success Test case -- Found the unsupportive/corruted jds ---------")
            sproutsai.logger.info(" --------------------")
            
        else:
            sproutsai.logger.info(" --------------------")
            sproutsai.logger.error(" ---------- Job parsed -- unsupportive/corruted jds -- test failed ------------- ")
            sproutsai.logger.info(" --------------------")

    sproutsai.close()


def test_empty_fields_testing():
    log_file = 'empty_format_test_cases.log'  # Specify the log file here
    sproutsai = initialize_sproutsai(username='Dhanunjaya', log_file=log_file)

    sproutsai.login(username='pankaj+natera@sproutsai.com', password='Demo@123', test_name=' ---- sucessfull login ----')

    for i in empty_jd_paths:
        sproutsai.testing_post_new_job_for_empty_fields(file_path_exist=True,file_path=i,test_name=' ------ testing with empty fields jds -------- ')
        # Find the input element by its attributes
        
        if "Search here" in sproutsai.driver.page_source:
            sproutsai.logger.info(" --------------------")
            sproutsai.logger.info(" ----------- Success Test case -- Found the empty fields ---------")
            sproutsai.logger.info(" --------------------")
        else:
            sproutsai.logger.info(" --------------------")
            sproutsai.logger.error(" ---------- Job parsed -- empty fields -- test failed ------------- ")
            sproutsai.logger.info(" --------------------")

    sproutsai.close()
            


# Run pytest with your test file and specify the log file
if __name__ == '__main__':
    pytest.main()
