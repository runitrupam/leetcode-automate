'''
Author: Runit 


LeetCode Scraper is a python program that logins into your LeetCode account through different options, and copies your code for your solved 
problems into its corresponding file.

For example, your solution to the problem FizzBizz will be stored in the file Fizzbizz.extension
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from dotenv import load_dotenv

from selenium.webdriver.support import expected_conditions as EC
import time
import os  # for the cwd 
import re
import json
import sys
import requests
import leetcode
import datetime
# import tkinter as tk  # for the copy of text to clipboard or from clipboard , somehow not working to clear the clipboard
import pyperclip  # can be used to copy from clipboard as well as clear the clipboard

from utils import *

SLEEP_TIMER = 5  # used in time.sleep(SLEEP_TIMER) for slow internet
TIME_DELAY = 5  # will wait until the location of xpath is not found then throw error if not found
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
# DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver.exe")
# 
# PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
# DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")
# CODE_DRIVER = webdriver.Chrome(executable_path = "./chromedriver.exe")

CODE_DRIVER = webdriver.Chrome()
load_dotenv()  # To load the .env file


def sign_into_leetcode():
    '''
    This function will ask the user for the preferred method to login(Currently only Linkedin,github or using facebook)
    Leetcode restricts automatic login , as captcha is there and selenium can't bypass it.
    Google auth doesn't allow automation os you can use undetected_chromedriver

    '''

    CODE_DRIVER.get("https://leetcode.com/accounts/logout")
    CODE_DRIVER.implicitly_wait(TIME_DELAY)

    valid_choice = True

    while (valid_choice):
        valid_choice = False

        # Pick the login creds from .env else from user
        username = os.environ.get('username')
        password = os.environ.get('password')
        option = os.environ.get('option')
        file = open('.env', 'a')
        if username is None:
            username = input("Enter your username: ")
            save_username = input("Do you want to save the login username enter 1 else 0: ")
            if save_username == '1':
                file.write('\n' + 'username=' + username)
        if password is None:
            password = input("Enter your password: ")
            save_pass = input("Do you want to save the login password enter 1 else 0: ")
            if save_pass == '1':
                file.write('\n' + 'password=' + password)
        if option is None:
            option = input(
                "Type in method to login \n 1. Leetcode \n 2. Facebook \n 3. Google \n 4. Linkedin \n 5. Github \n")
            save_option = input("Do you want to save the login method enter 1 else 0: ")
            if save_option == '1':
                file.write('\n' + 'option=' + option)
        file.close()

        try:
            # username = "ss@gmail.com"
            # password = "dedd"
            # option = "4"
            CODE_DRIVER.maximize_window()

            if option == "1":
                # leetcode default login(Captcha might be an issue sometimes)
                print("You have choosen to go with leetcode default login, "
                      "captcha might create an issue, be prepared to solve it \n ")
                CODE_DRIVER.get("https://leetcode.com/accounts/login/")
                CODE_DRIVER.find_element(By.ID, "id_login").send_keys(username)
                CODE_DRIVER.implicitly_wait(TIME_DELAY)
                CODE_DRIVER.find_element(By.ID, "id_password").send_keys(password)
                CODE_DRIVER.implicitly_wait(TIME_DELAY)
                time.sleep(SLEEP_TIMER)
                CODE_DRIVER.find_element(By.ID, "id_password").send_keys(Keys.ENTER)
            elif option == '2':
                print("You have choosen to login to leetcode using the facebook creds, "
                      "be sure to add the facebook login creds\n ")
                CODE_DRIVER.get("https://leetcode.com/accounts/facebook/login/")
                CODE_DRIVER.find_element(By.ID, "email").send_keys(username)
                CODE_DRIVER.implicitly_wait(TIME_DELAY)
                CODE_DRIVER.find_element(By.ID, "pass").send_keys(password)
                CODE_DRIVER.implicitly_wait(TIME_DELAY)
                CODE_DRIVER.find_element(By.ID, "pass").send_keys(Keys.ENTER)

            elif option == '3':
                print("selenium doesn't bypass the goggle auth, so you have to use undetected_chromedriver")
                # import undetected_chromedriver as uc
                # CODE_DRIVER = uc.Chrome()
                CODE_DRIVER.get("https://leetcode.com/accounts/google/login/")
                CODE_DRIVER.find_element(By.ID, "identifierId").send_keys(username + Keys.ENTER)
                CODE_DRIVER.implicitly_wait(TIME_DELAY)
                CODE_DRIVER.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(
                    password + Keys.ENTER)
                print("You might receive an otp or auth on your mobile phone")


            elif option == '4':
                # login_url = "https://www.linkedin.com/"
                login_url = 'https://www.linkedin.com/uas/login?fromSignIn=true&trk=cold_join_sign_in'
                CODE_DRIVER.get(login_url)
                CODE_DRIVER.find_element(By.ID, "username").send_keys(username)
                CODE_DRIVER.find_element(By.ID, "password").send_keys(password + Keys.ENTER)

                CODE_DRIVER.implicitly_wait(TIME_DELAY)
                CODE_DRIVER.execute_script("window.open('');")  # New tab
                # Switch to the new window and open new URL
                CODE_DRIVER.switch_to.window(CODE_DRIVER.window_handles[-1])
                CODE_DRIVER.get("https://leetcode.com/accounts/linkedin_oauth2/login/?next=%2F")
                try:
                    CODE_DRIVER.find_element(By.XPATH, '//*[@id="oauth__auth-form__submit-btn"]').click()
                except Exception as e:
                    pass
                CODE_DRIVER.implicitly_wait(TIME_DELAY)
            elif option == '5':

                CODE_DRIVER.get("https://leetcode.com/accounts/github/login/")
                CODE_DRIVER.find_element(By.XPATH, '// *[ @ id = "login_field"]').send_keys(username)
                CODE_DRIVER.implicitly_wait(TIME_DELAY)
                CODE_DRIVER.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
                CODE_DRIVER.implicitly_wait(TIME_DELAY)
                CODE_DRIVER.find_element(By.XPATH, '//*[@id="password"]').send_keys(Keys.ENTER)
                CODE_DRIVER.implicitly_wait(TIME_DELAY)
                # auth = input("Enter Device Verification Code:")
                # CODE_DRIVER.find_element_by_xpath('//*[@id="otp"]').send_keys(auth)
                # CODE_DRIVER.find_element_by_xpath('//*[@id="otp"]').send_keys(Keys.ENTER)
            else:
                valid_choice = True
                print("Invalid Choice. Please choose a number from 1 to 5 \n")
            print("User is logged in.\n")

        except Exception as e:
            print("Wrong username and/or password", e)
            print('Do you want to try login again then Enter 1 else 0')
            valid_choice = int(input())

        CODE_DRIVER.implicitly_wait(TIME_DELAY)


def scrape_code(href, url=None):
    '''
    This function scrapes the code off Leetcode.
    This is neccessary because Leetcode's code text area is modified to provide highlighting and other features to the
    text.

    '''
    language = 'Python'  # default if none selected
    wait = WebDriverWait(CODE_DRIVER, 80)
    code = ""
    # CODE_DRIVER.execute_script("window.open('');")
    CODE_DRIVER.switch_to.window(CODE_DRIVER.window_handles[-1])
    if url is None:
        CODE_DRIVER.get(href + "/submissions/")
    else:
        CODE_DRIVER.get(url)
    CODE_DRIVER.implicitly_wait(TIME_DELAY)
    time.sleep(SLEEP_TIMER)  # LET THE PAGE LOAD FULLY
    # GO forward only if new theme is selected , as copying the solution is easier
    try:
        # if "go to newer theme" found , so older theme is on
        CODE_DRIVER.find_element(By.CLASS_NAME, 'css-1xbubfu-StyledBanner').click()
        CODE_DRIVER.implicitly_wait(TIME_DELAY)
        print('   newer theme is now selected to scrap data     ')
    except Exception as e:
        print('    newer theme is already on to scrap data      ')

    # Show only the Accepted solution
    try:
        # CODE_DRIVER.find_element(By.XPATH,
        #                          '/html/body/div[1]/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div[1]/button').click()
        # CODE_DRIVER.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div[2]/div[2]').click()
        time.sleep(SLEEP_TIMER)  # very imp for slow internet or lag from leetcode server
        xpath_all_status = '//*[@id="qd-content"]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]'
        CODE_DRIVER.find_element(By.XPATH, xpath_all_status).click()
        CODE_DRIVER.implicitly_wait(TIME_DELAY)
        xpath_choose_accepted = '//*[@id="qd-content"]/div[1]/div/div/div/div[2]/div/div[1]/div/div[1]/div[2]/div[2]'
        CODE_DRIVER.find_element(By.XPATH, xpath_choose_accepted).click()
        CODE_DRIVER.implicitly_wait(TIME_DELAY)
    except Exception as e:
        print('Unable to choose Accepted solution, picking the 1st solution', e)

    accepted_code = CODE_DRIVER.find_element(By.XPATH,
                                             '//*[@id="qd-content"]/div[1]/div/div/div/div[2]/div/div[2]/div[1]')
    CODE_DRIVER.implicitly_wait(TIME_DELAY)
    accepted_code.click()

    try:
        # root = tk.Tk() # uses tkinter object
        # root.clipboard_clear()
        # root.clipboard_append('')
        pyperclip.copy('')  # To clear the clipboard
        temp_elem_cp = CODE_DRIVER.find_element(By.XPATH,
                                                '//*[@id="qd-content"]/div[3]/div/div[1]/div/div[1]/div[2]/div[7]/div/div')
        temp_elem_cp.click()  # this is the leetcode built in copy to clipboard
        CODE_DRIVER.implicitly_wait(TIME_DELAY)
        # copied_text = root.clipboard_get() # to get the copied text
        copied_text = pyperclip.paste()
        if len(copied_text) == 0:
            raise Exception('Nothing copied')
        code = copied_text
        language = CODE_DRIVER.find_element(By.XPATH,
                                            '//*[@id="qd-content"]/div[3]/div/div[1]/div/div[1]/div[2]/div[2]/span').text
        CODE_DRIVER.implicitly_wait(TIME_DELAY)
    except Exception as e:
        print('Error in copying the solution of', href, e)
        # very slow code below 
        '''
        spans = CODE_DRIVER.find_element(By.TAG_NAME, 'pre').find_elements(By.TAG_NAME, 'span')
        CODE_DRIVER.implicitly_wait(TIME_DELAY)

        # Trying to remove time.sleep()
        # if wait.until(EC.staleness_of(lines)) :
        #    lines = CODE_DRIVER.find_elements_by_class_name("ace_line_group")
        code = ''
        for line in spans:
            # for character in line:
            try:
                inner_span = line.find_elements(By.TAG_NAME, 'span')
                # CODE_DRIVER.implicitly_wait(TIME_DELAY)
                if len(inner_span) > 0:
                    continue
            except:
                pass
            try:
                code += line.text + " "
            except:
                pass

            # code += "\n"
        # print(1)
        print(code)
        '''
    return code, language


def scrap_all_accepted_solution():
    """
    This function opens the algorithms and scrapes your code off each problem.
    It then stores it into a file.

    CODE_DRIVER.window_handles
    ['EC67B05D6F71D8AFF123982E651AD526', '1791841035D8AF2AFFF16A6E8E295ECC', '069B870E90881E5FDE402C88D9DC4DC5']
    CODE_DRIVER.current_window_handle
    '069B870E90881E5FDE402C88D9DC4DC5'

    """

    make_directory("leet_code_solutions")

    # Opens new window
    CODE_DRIVER.execute_script("window.open('');")
    CODE_DRIVER.switch_to.window(CODE_DRIVER.window_handles[-1])

    CODE_DRIVER.get("https://leetcode.com/problemset/algorithms/")
    CODE_DRIVER.implicitly_wait(TIME_DELAY)
    time.sleep(SLEEP_TIMER)

    # Shows only problems that are solved
    # solved_dropdown = CODE_DRIVER.find_element(By.XPATH, '//*[@id="question-app"]/div/div[2]/div[2]/div/div[2]/div[4]')
    # solved_dropdown.click()

    # GO forward only if old theme is selected
    try:
        # if "go to newer theme" found , so older theme is on
        CODE_DRIVER.find_element(By.XPATH, '//*[@id="question-app"]/div[2]/div/div')
        CODE_DRIVER.implicitly_wait(TIME_DELAY)
    except Exception as e:
        print('Choosing the older theme')
        # if "go to older theme" found  go to older theme
        CODE_DRIVER.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div[2]/div/div').click()
        CODE_DRIVER.implicitly_wait(TIME_DELAY)

    # Status button clicked
    xpath = '//*[@id="question-app"]/div[1]/div[2]/div[2]/div[1]/div[2]/div[4]/button'
    elem = CODE_DRIVER.find_element(By.XPATH, xpath)
    elem.click()
    CODE_DRIVER.implicitly_wait(TIME_DELAY)
    time.sleep(SLEEP_TIMER)

    # choose solved problems
    xp = "//div[@class='pull-right dropdown show filter-item filterStatus open']//div[2]"
    CODE_DRIVER.find_element(By.XPATH, xp).click()
    CODE_DRIVER.implicitly_wait(TIME_DELAY)

    print("Getting the title and link for each solved question.")

    # Opens every problem and then copies their data into a file
    title_href = {}
    while (True):
        try:
            table = CODE_DRIVER.find_element(By.CLASS_NAME, 'reactable-data')
            CODE_DRIVER.implicitly_wait(TIME_DELAY)

            for row in table.find_elements(By.TAG_NAME, 'tr'):
                title = row.find_element(By.TAG_NAME, 'a').text
                href = row.find_element(By.TAG_NAME, 'a').get_attribute("href")
                CODE_DRIVER.implicitly_wait(TIME_DELAY)
                title_href[title] = href

            # Go to next page
            CODE_DRIVER.find_element(By.XPATH, '//*[@class="reactable-next-page"]').click()
            CODE_DRIVER.implicitly_wait(TIME_DELAY)
        except Exception as e:
            print('Error in getting the question links', e)
            break

    print('Export all the title and links to a json file')
    title_href_json_obj = json.dumps(title_href)
    file = open('leetcode_solved_problems_links.json', 'w')
    file.write(title_href_json_obj)
    '''
    To read the written file.
    f = open('leetcode_solved_links.json','r' )
    f.seek(0) # to bring cursor to start of file
    title_href_json_obj = f.read()
    title_href_dict = json.loads(title_href_json_obj)
    '''

    for title in title_href:
        file_exists = create_file(title, code = '', check_file_exists = 1)
        if file_exists:
            print("Code exists for :- ", title)
            continue
        print("Scraping the code for :- ", title)

        code, language = scrape_code(title_href[title])
        create_file(title, code, language)


def choose_top_solutions(CODE_DRIVER, language_selected):
    xpath_click_on_solution = '//*[@id="qd-content"]/div[1]/div/div/div/div[1]/div/div/a[3]/div'
    CODE_DRIVER.find_element(By.XPATH, xpath_click_on_solution).click()
    xpath_click_on_tag = '//*[@id="qd-content"]/div[1]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/span'
    tags = CODE_DRIVER.find_elements(By.XPATH, xpath_click_on_tag)
    CODE_DRIVER.implicitly_wait(TIME_DELAY)
    for tag in tags:
        if language_selected in tag.text:  # tag.text = Python3\n1234
            tag.click()
            break

    # Go through top 15 solutions and try those.
    xpath_all_solutions = '//*[@id="qd-content"]/div[1]/div/div/div/div[2]/div/div/div[2]/div[3]/div[1]/div'
    all_solution_links = CODE_DRIVER.find_elements(By.XPATH, xpath_all_solutions)
    CODE_DRIVER.implicitly_wait(TIME_DELAY)
    return all_solution_links


def scrap_sol_of_daily_solution():
    make_directory("leet_code_daily_solutions")

    choosen_language = os.environ.get('choosen_language')
    file = open('.env', 'a')
    if choosen_language is None:
        print('Choose your coding language C++, Java , Python, Python3, Javascript...')
        choosen_language = input('')
        save_choosen_language = input("Do you want to save the Coding language enter 1 else 0: ")
        if save_choosen_language == '1':
            file.write('\n' + 'choosen_language=' + choosen_language)
    file.close()

    CODE_DRIVER.get('https://leetcode.com/problems/two-sum/')  # sometimes the daily soution is already done.
    CODE_DRIVER.implicitly_wait(TIME_DELAY)

    # GETTING TO THE CODE OF DAILY SOLUTION AUTOMATE
    try:
        time.sleep(SLEEP_TIMER)  # delay in loading of page , implicitly_wait doesn't work here
        x_path = '/html/body/div[1]/div/div/div/nav/div/div/div[2]/a[2]'
        # xpath = '/html/body/div[1]/div/div/div[2]/div[3]'
        CODE_DRIVER.find_element(By.XPATH, x_path).click()
        CODE_DRIVER.implicitly_wait(TIME_DELAY)

    except Exception as e:
        pass
    CODE_DRIVER.implicitly_wait(TIME_DELAY)

    # GO forward only if new theme is selected , as copying the solution is easier
    try:
        # if "go to newer theme" found , so older theme is on
        CODE_DRIVER.find_element(By.CLASS_NAME, 'css-ly0btt-NewDiv').click()
        CODE_DRIVER.implicitly_wait(3)
        print('    newer theme is selected to scrap data')
    except Exception as e:
        print('    newer theme is already on to scrap data')

    try:
        # Choose language

        # CODE_DRIVER.find_element(By.CLASS_NAME , 'relative notranslate').click()
        CODE_DRIVER.switch_to.window(CODE_DRIVER.window_handles[-1])
        xpath = '/html/body/div[1]/div/div/div/div/div/div[3]/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div/button'
        CODE_DRIVER.find_element(By.XPATH, xpath).click()

        CODE_DRIVER.implicitly_wait(TIME_DELAY)

        # all language list
        xpath = '/html/body/div[1]/div/div/div/div/div/div[3]/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div/ul/li'
        # xpath = '/html/body/div[1]/div/div/div/div/div/div[3]/div/div[1]/div/div/div/div[3]/div[1]/div[1]/div/ul/li'
        all_lang = CODE_DRIVER.find_elements(By.XPATH, xpath)
        CODE_DRIVER.implicitly_wait(TIME_DELAY)

        for lang in all_lang:
            if lang.text == choosen_language:
                lang.click()
                break
    except Exception as e:
        print('Not able to choose the desired language.', e)

    try:
        xpath = '/html/body/div[1]/div/div/div/div/div/div[3]/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div/button/div/div'
        CODE_DRIVER.implicitly_wait(TIME_DELAY)
        language_selected = CODE_DRIVER.find_element(By.XPATH, xpath).text
        print('Going with the -> ', language_selected, 'language')
    except Exception as e:
        language_selected = 'C++'
        print('default coding language = C++ selected', e)
        

    # choose_top_solutions
    all_solution_links = choose_top_solutions(CODE_DRIVER, language_selected)

    # CODE_DRIVER.get_cookie('LEETCODE_SESSION')['value']
    LEETCODE_SESSION = CODE_DRIVER.get_cookie('LEETCODE_SESSION')['value']

    # just check whether your username is printed or not.
    get_logged_in_confirmation_using_leetcode_api(LEETCODE_SESSION)

    # get the problem title
    current_problem_url = CODE_DRIVER.current_url
    prob_title = current_problem_url.split('/')[4]
    # get the questionId
    questionId = get_question_id_using_leetcode_api(LEETCODE_SESSION, prob_title)
    # get the language_id usi post request ,or hard code it. like Python3  = 11 , cpp = 0 ,python = 2
    language_id = get_language_id_using_leetocde_api(LEETCODE_SESSION, language_selected)

    href_list = []
    for curr_sol in all_solution_links:
        try:
            href = curr_sol.find_element(By.TAG_NAME, 'a').get_attribute("href")
            href_list.append(href)
        except Exception as e:
            print('Unable to get the solution link', e)

    i = 0
    while i < (len(href_list)):
        try:
            print('trying the solution', i, href)
            # curr_sol = all_solution_links[i]
            # href = curr_sol.find_element(By.TAG_NAME, 'a').get_attribute("href")
            href = href_list[i]
            CODE_DRIVER.implicitly_wait(TIME_DELAY)
            solution_id = href.split('/')[6]
            if not solution_id.isnumeric():
                raise Exception('solution id is wrongly picked')
            solution_id = int(solution_id)
            solution_string = fetch_the_solution_content(solution_id)

            if solution_string.find('```'):
                new_cont = solution_string[solution_string.find('```') + 3:]
                if new_cont.find('```'):
                    new_solution = new_cont[:new_cont.find('```')]
                    # print(new_solution)
            solution_string = new_solution.replace('\\n', '\n').replace('\\', '')
            # # fill this new_solution and Run the COde then submit
            # xpath_code_editor = '//*[@id="editor"]/div[4]/div[1]/div/div/div[1]/div[2]/div[1]/div[4]'
            # elem = CODE_DRIVER.find_element(By.XPATH, xpath_code_editor)

            # Update code editor code
            update_code_editor_solution_using_leetcode_api(LEETCODE_SESSION, solution_string, questionId = questionId,
                                                           language_id = language_id)
            # Run the code
            CODE_DRIVER.get(current_problem_url)
            time.sleep(SLEEP_TIMER + 5)  # wait for the code to load
            xpath_run_code = '//*[@id="qd-content"]/div[3]/div/div[3]/div/div/div/div/div[2]/div[3]/button[2]'
            CODE_DRIVER.find_element(By.XPATH, xpath_run_code).click()
            CODE_DRIVER.implicitly_wait(TIME_DELAY)
            time.sleep(SLEEP_TIMER)  # check for errors

            xpath_check_for_errors_and_accepted = '//*[@id="qd-content"]/div[3]/div/div[3]/div/div/div[2]/div/div[3]/div[1]'
            elem = CODE_DRIVER.find_element(By.XPATH, xpath_check_for_errors_and_accepted)
            CODE_DRIVER.implicitly_wait(TIME_DELAY)
            status = elem.text.lower()
            if 'runtime error' in status or 'wrong answer' in status or 'time limit exceeded' in status:
                raise Exception('Error in Code for solution_id = ', solution_id)
            if 'accepted' in status:  # Submit only if accepted
                time.sleep(SLEEP_TIMER)
                xpath_submit_code = '//*[@id="qd-content"]/div[3]/div/div[3]/div/div/div[3]/div/div[2]/div[3]/button[3]'
                CODE_DRIVER.find_element(By.XPATH, xpath_submit_code).click()
                CODE_DRIVER.implicitly_wait(TIME_DELAY)

                # some pop up comes so refresh THE PAGE
                CODE_DRIVER.refresh()
                CODE_DRIVER.execute_script("window.open('');")
                time.sleep(SLEEP_TIMER + 5)
                code, language = scrape_code('https://leetcode.com/problems/' + prob_title)
                print('code fetched = ', code)
                print('language used for submit=', language)
                file_name = prob_title + str(datetime.datetime.now().strftime("  %Y %m %d   %H %M %S"))
                create_file(file_name, code,
                            language = language, dir = './leet_code_daily_solutions/')
                print('Solution submitted and saved in the dir = leet_code_daily_solutions and file name = ', file_name)
                break
                # check whether the solution is accepted or not

                # get the submissionId
                # Submit code 
                # submit_code_solution_using_leetcode_api(LEETCODE_SESSION, submissionId = 123)
            i += 1
        except Exception as e:
            # all_solution_links = choose_top_solutions(CODE_DRIVER, language_selected)
            i += 1
            print('Not able to choose the solution', e)

    CODE_DRIVER.implicitly_wait(TIME_DELAY)


if __name__ == "__main__":
    print("##########################", datetime.datetime.now(), "##########################")
    choose_program = os.environ.get('choose_program')
    file = open('.env', 'a')
    if choose_program is None:
        print(
            "There are two parts:-\n PART A: Scrap and submit daily solution \n PART B: Scrap and save all accepted solution")
        choose_program = input('Enter A or B')
        save_choose_program = input("Do you want to save the program choice ,enter 1 else 0: ")
        if save_choose_program == '1':
            file.write('\n' + 'choose_program=' + choose_program)
    file.close()

    old_stdout = sys.stdout
    log_file = open("message.log", "a")
    if os.path.getsize('message.log') / 1024 / 1024 >= 5:  # > than 5Mb
        log_file = open("message.log", "w")

    try:
        sign_into_leetcode()
        sys.stdout = log_file
        print("##########################", datetime.datetime.now(), "##########################")
        print("Output will be written to message.log")
        if choose_program == 'A':
            scrap_sol_of_daily_solution()
        else:
            scrap_all_accepted_solution()

        CODE_DRIVER.close()
    except Exception as e:
        print('Some error in main', e)
        pass
    # Revert to old stdout
    sys.stdout = old_stdout
    log_file.close()

'''

SOME NOT USED CODES,
ALGORITHMS_ENDPOINT_URL = "https://leetcode.com/api/problems/algorithms/"
algorithms_problems_json = requests.get(ALGORITHMS_ENDPOINT_URL).content
'''
