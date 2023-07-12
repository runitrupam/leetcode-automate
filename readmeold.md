# Leetcode-Scrapper

##### This is web scraping program to download all your Leetcode solved problems. And Automate the leetcode daily solution

<br />

1. #### Scrape the leetcode solution
    - [X] Login
    - [X] store problems solved links in a leetcode_solved_links.json
    - [X] Read from leetcode_solved_links.json to check if the solution exists or not.
    - [X] Get the solutions and add to the directory leet_code_solutions,
      with their respective extension .py , .js or .cpp.
2. #### Automate the leetcode daily solution.
    - [X] Automatic Login(Pick creds from .env
    - [X] get all language specific solutions and try all solutions until Run code is correct.
    - [X] Submit and save the solution to the directory leet_code_daily_solutions,
      with their respective extension .py , .js or .cpp. .
    - [X] Create a cron to run daily
<br/>

https://youtu.be/yl3zF6ZVpDg

##### Click on video to play!
[![img.png](images/leetcode_product.png)](https://youtu.be/yl3zF6ZVpDg)

<br/>
For more details, must read -

1. https://medium.com/@runitranjankumar/leetcode-automate-solving-problems-4f6dfa35f2fd <br />
2. https://pypi.org/project/python-leetcode/

<br />
How to use?
<br />
You just need 2 things. <br />
- Check your Chrome browser version and download suitable chromedriver.  <br />  

- All the code files
  <br />

Required directory/files will be created during runtime. Go through the comments in the codes.<br />
<br />

**source new_venv/bin/activate**
**pip3 install -r requirements.txt**


Run linux_autorunner.sh or windows_autorunner.bat code file.
Windows user might get warning pop-up, click on "More Info" and then "Run Anyway" button. <br>
You can run the "leetcode_scrapper.py" directly.
<br />
Follow the on-screen instruction.
You will be asked for your login credentials.<br />
<br />

Since Leetcode website gets updated after few months of interval, you might face WebDriver Errors. Please do not
hesitate to raise an issue with error screenshot. This will help me to update the codebase in efficient manner.
<br />
<br />

Watch automation on browser, it is fun :) <br />
<br />

Share this with your friends! Happy Leetcoding!! <br />
Put a star, if you like this project.
