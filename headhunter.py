import os, sys, json, time, shutil, signal, random

import datetime
from datetime import datetime, timedelta

import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
####################################################################
# pls don't use this to bother anyone.
####################################################################
if(len(sys.argv) != 4):
    print("Usage: ~$ python3 ./headhunter.py <linkedin_email> <linkedin_password> <delay_in_seconds>")
    exit()
else:
    u = list(sys.argv)[1]
    p = list(sys.argv)[2]
    delay = int(list(sys.argv)[3])
#######-####-#####-#################################################
def keyboardInterruptHandler(signal, frame):
    save()
    exit(0)
signal.signal(signal.SIGINT, keyboardInterruptHandler)
#######-####-#####-#################################################
def save():
    # if there's an error save what's in the log variable to the json file for today
    print("*********** ENDING GRACEFULLY *****************************")
    end_time = int(round(time.time() * 1000))

    log['runtime'] = log['runtime'] + ( end_time - start_time )
    log['last_updated'] = str(datetime.now())

    date = datetime.now().strftime("%d-%m-%Y")
    todays_log = "./logs/log-" + date + ".json"

    with open(todays_log, 'w') as fp:
        json.dump(log, fp)

    with open("./logs/master_user_log.txt", 'w') as fp:
        for user in master_users:
            fp.write('%s\n' % user)

    browser.quit()
#######-####-#####-#################################################
def check_log():
    # check if the program is using the right log. i.e. it's 12:01
    print("- Log_Name: " + log['log_name'])
    current_log = "log-" + datetime.now().strftime("%d-%m-%Y") + ".json"
    if current_log == log['log_name']:
        print("Current log is Correct")
    else:
        print("Current log is Wrong")
        # TODO : 
#######-####-#####-#################################################
print("=========== Linkedin Social Engineering Script ============")
print("       -------'IF YOU VIEW IT THEY WILL COME'-------        ")
# TODO : gracefully change logs at midnight

print("=---- Checking for ./chromedriver")
# TODO : edit file to make less recognizable to the site
# https://stackoverflow.com/questions/33225947/can-a-website-detect-when-you-are-using-selenium-with-chromedriver
if os.path.isfile("./chromedriver") is False:
    print("- CHOMEDRIVER IS NOT INSTALLED! Get it here: https://chromedriver.chromium.org/downloads")
    exit(0)
else:
    print("- Chromedriver is installed.")
#######-####-#####-#################################################
print("=---- Loading Keywords")
text_file = open("./keywords.txt", "r").read()
keywords = text_file.splitlines()
print("- " + str(len(keywords)) + " Keywords Loaded.")
#######-####-#####-#################################################
print("=---- Loading User List")
text_file = open("./logs/master_user_log.txt", "r").read()
master_users = text_file.splitlines()
print("- " + str(len(master_users)) + " Users Loaded.")
#######-####-#####-#################################################
print("=---- Loading Log")
date = datetime.now().strftime("%d-%m-%Y")
print("=- Today's Date: " + date)
todays_log = "log-" + date + ".json"

if os.path.isfile("./" + todays_log) is False:
    print("=- Creating A New Log For Today.")
    log_path = "./logs/" + todays_log
    shutil.copy("./template.json", log_path) 
else:
    print("=- Log Exists, Loading it")

with open("./logs/" + todays_log) as json_file: 
    log = json.load(json_file) 

log["log_name"] = "log-" + date + ".json"
#######-####-#####-#################################################
print("=---- Loading Cities")
text_file = open("./cities.txt", "r").read()
cities = text_file.splitlines()
print("-" + str(len(cities)) + " Cities Loaded.")

for city in cities:
    try:
        if(log['cities'][city.split("#")[1].replace(" ", "")] == 0):
            log['cities'][city.split("#")[1].replace(" ", "")] = 0
    except KeyError:
        log['cities'][city.split("#")[1].replace(" ", "")] = 0

#######-####-#####-#################################################
# Search URL Setup
profile_languages = '["en","fr"]'   # tea & baguette
connection_degree = '["O"]'         # 3rd deg connections only
search_slug = 'https://www.linkedin.com/search/results/people/?origin=GLOBAL_SEARCH_HEADER&facetNetwork=' + connection_degree + '&facetProfileLanguage=' + profile_languages + '&'
#######-####-#####-#################################################
def hol_up(x):    # wait a x
    time.sleep(x) # act normal
#######-####-#####-#################################################
def links_2_users(links):
    # Takes a list of URLs and strips the usernames.
    usernames = []
    for link in links:
        if "https://www.linkedin.com/in/" in link.get_attribute("href"):
            username = link.get_attribute("href").replace("https://www.linkedin.com/in/", "").replace("/", "")
            if username not in usernames:
                usernames.append(username)
    print("- " + str(len(usernames)) + " Usernames extracted.")
    return usernames
#######-####-#####-#################################################
def add_query(city_id, keyword):
    if city_id + "-" + keyword not in log['queries']:
        log['queries'].append(city_id + "-" + keyword)
#######-####-#####-#################################################
def login():
    browser.get("https://www.linkedin.com/login")
    in_user = browser.find_element_by_id("username")
    in_user.send_keys(u)
    in_pass = browser.find_element_by_id("password")
    in_pass.send_keys(p)
    in_pass.send_keys(Keys.ENTER)
#######-####-#####-#################################################
def heck():
    for city in cities:
        city_id = city.split("#")[1].replace(" ", "")
        city_slug = search_slug + '&facetGeoUrn=%5b"' + city_id + '"%5D'

        for keyword in keywords:

            check_log()
            add_query(city_id, keyword)

            browser.get(city_slug)

            hol_up(delay)
            browser.execute_script("document.getElementById('msg-overlay').style.display = 'none';")                       # Close Chat
            browser.find_element_by_xpath('/html/body/div[7]/header/div[2]/div/div/div[1]/div/input').send_keys(keyword)   # Input keyword
            browser.find_element_by_class_name('search-global-typeahead__button').click()                                  # Click search button
            hol_up(delay)
            
            res_count = browser.find_element_by_class_name('search-results__total').text.split(" ")[1]
            page_count = 100
            if int(res_count.replace(",","")) < 100: 
                page_count = res_count / 10

            print("- " + str(res_count) + " Results For '" + keyword + "' in '" + city.split("#")[0].replace(" ", "") + "'.")
            print("- " + str(page_count) + " Pages of Results")
            
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            hol_up(delay)

            query_url = browser.current_url
            batch = []
    
            print("===== Collecting Usernames From Query")
            print("=--- Page 1 ----")

            links = browser.find_elements_by_xpath("//a[@href]")
            users = links_2_users(links)
            batch.extend(users)
            print("- " + str(len(batch)) + " Users in this batch so far.")

            for page in range(2, page_count):  # page_count
                print("=--- Page " + str(page) + " ----")
                page_url = query_url + "&page=" + str(page)
                browser.get(page_url)
                hol_up(delay)
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                links = browser.find_elements_by_xpath("//a[@href]")
                users = links_2_users(links)
                batch.extend(users)
                hol_up(delay)
            
            # print("===== Viewing Each Profile In This Batch")
            # print("- " + str(len(batch)) + " Usernames Connected in this batch")
        
            for usr in batch:
                
                if usr not in log['users'] and usr not in master_users:
                    hol_up(delay)
                    browser.get("https://www.linkedin.com/in/" + usr + "/")
                    log['users'].append(usr)
                    master_users.append(usr)
                    log['cities'][city.split("#")[1].replace(" ", "")] += 1
                    hol_up(delay)   
#######-####-#####-#################################################
print('=========== STARTING HECK =================================')

start_time = int(round(time.time() * 1000))
browser = webdriver.Chrome(executable_path="./chromedriver")
login()
try:
    heck()
except:
    save()
