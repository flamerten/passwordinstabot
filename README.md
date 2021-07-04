# passwordinstabot
Using Selenium to automate the changing of Instagram's password using a chrome driver

Go to https://chromedriver.chromium.org/downloads and download the chrome webdriver for your version of chrome. 

Add it to the path --> PATH = 'C:\Program Files (x86)\chromedriver.exe', this can be changed in the instabot.py file if you
prefer a different path.

Open pass_gen.py and run the file. Call the function set_password(<your_current_password>) this will record your current
password in the pwds.csv file.

Open instabot.py and change login('flamerten') to login('<your insta username>')

Run instabot.py If your password has changed successfully, the programe should print

"Password changed successfully"

To get your current password, run the function return_latest_pass() Its under pass_gen.py but doing it immediately
after running instabot.py is fine as well, as instabot.py imports all functions from pass_gen.py Opening pwds.csv will show all
the dates and the passwords used.

