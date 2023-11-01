import pytest
from successfull_login_beta import initialize_sproutsai

test_cases = ['1.Providing username instead of formatted email', '2.Providing invalid email and password', '3.Providing correct email and wrong password', '4.Providing correct email and correct password']
email_password = {'case1':['pankaj','12345'], 'case2':['pankaj@gmail.com','123456'], 'case3' : ['pankaj+natera@sproutsai.com','Demo@13'],'case4' : ['pankaj+natera@sproutsai.com','Demo@123']}

def test_login():
    log_file = 'Login_test_cases.log'  # Specify the log file here
    sproutsai = initialize_sproutsai(username='Dhanunjaya', log_file=log_file)

    for i in range(len(test_cases)):
        case_key = f'case{i + 1}'
        username, password = email_password[case_key]
        sproutsai.login(username=username, password=password, test_name=test_cases[i])

        # Check for the "Post new job" text on the page
        if "Post new job" in sproutsai.driver.page_source:
            sproutsai.logger.info(" ----------- Success Test case -- Login test completed ---------")
        else:
            sproutsai.logger.error(" ---------- Login test failed ------------- ")
        
    sproutsai.close()

# Run pytest with your test file and specify the log file
if __name__ == '__main__':
    pytest.main()
