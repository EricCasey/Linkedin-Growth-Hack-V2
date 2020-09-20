import sys
import json
import time
import signal
import random
import datetime
import selenium

from datetime import datetime, timedelta

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

u = "<linkedin_username>"    # username placeholder for debugging
p = "<linkedin_password>"    # password placeholder for debugging

# print('Number of arguments:', len(sys.argv), 'arguments.')
# print('Argument List:', str(sys.argv))

# if(len(sys.argv) != 3):
#     print("Usage: ~$ python3 ./headhunter.py <linkedin_email> <linkedin_password>")
#     exit()
# else:
#     u = list(sys.argv)[1]
#     p = list(sys.argv)[2]

print(u,p)

def keyboardInterruptHandler(signal, frame):
    save()
    exit(0)

browser = webdriver.Chrome(executable_path="./chromedriver")
signal.signal(signal.SIGINT, keyboardInterruptHandler)

def save():
    print("===== ENDING GRACEFULLY ==========")
    end_time = int(round(time.time() * 1000))

    log['stats']['runtime'] = log['stats']['runtime'] + ( end_time - start_time )
    log['last_updated'] = str(datetime.now())

    with open('log.json', 'w') as fp:
        json.dump(log, fp)

    browser.quit()



print("=== Linkedin Social Engineering Script ===")

print("=---- TODO")
print("_ Download chromedriver and edit it to avoid detection") # https://stackoverflow.com/questions/33225947/can-a-website-detect-when-you-are-using-selenium-with-chromedriver
print("_ ")

print("=---- Loading Chromedriver")


print("=---- Loading Cities")
text_file = open("./cities.txt", "r").read()
cities = text_file.splitlines()
print("-" + str(len(cities)) + " Cities Loaded")

print("=---- Loading Log")

## TODO GET DATE

with open('log.json') as json_file: 
    log = json.load(json_file) 
for city in cities:
    try:
        if(log['cities'][city.replace(" ", "")] == 0):
            log['cities'][city.replace(" ", "")] = 0
    except KeyError:
        log['cities'][city.replace(" ", "")] = 0


# TODO : update my profile stats

print("- This Week Number: " + str(datetime.now().isocalendar()[1]))
print("- Views This Week: " + str(log['stats']['views']['2020'][datetime.now().isocalendar()[1] - 1]))
print("- Total Connections: " + str(log['stats']['connections']['2020'][datetime.now().isocalendar()[1] - 1]))
print("- Total Profiles Viewed: " + str(len(log['users'])))

def login():
    browser.get("https://www.linkedin.com/login")
    in_user = browser.find_element_by_id("username")
    in_user.send_keys(u)
    in_pass = browser.find_element_by_id("password")
    in_pass.send_keys(p)
    in_pass.send_keys(Keys.ENTER)

filt_keywords = ['recruiter', 'hiring', 'headhunter', 'human resources', 'acquisition', 'personnel', 'talent', 'placement']
filt_language = '["en","fr"]'
filt_connections = '["O"]'
filt_location = ''
filt_page = 1

search_slug = 'https://www.linkedin.com/search/results/people/?origin=GLOBAL_SEARCH_HEADER&facetNetwork=' + filt_connections + '&facetProfileLanguage=' + filt_language + '&'

# print("- Base Search Slug: " + search_slug)

def get_stats():
    print("--- get stats in this func")

def kill_session():
    browser.close()

def hol_up():
    time.sleep(3)

def links_2_users(links):
    usernames = []
    for link in links:
    # print(link.get_attribute("href"))
        if "https://www.linkedin.com/in/" in link.get_attribute("href"):
            # print(link.get_attribute("href"))
            username = link.get_attribute("href").replace("https://www.linkedin.com/in/", "").replace("/", "")
            if username not in usernames:
                usernames.append(username)

    print("- " + str(len(usernames)) + " usernames extracted")

    return usernames

def begin():
    print("=---- STARTING SEARCHES")

    # LOOP CITIES
    #   LOOP KEYWORDS

    # for city in cities:
# try: 

    for city in [ "San Diego, California", "Tokyo, Japan" ]:

        print("=-- Searching in  + city")

        # for job_title in list_of_hr-related_job_titles
        for keyword in filt_keywords:

            browser.get(search_slug)

            print('=- "' + keyword + '"')

            hol_up()
            # browser.find_element_by_id('ember286').click()                                # Close Chat
            browser.find_element_by_xpath('/html/body/div[7]/aside/div[1]/header/section[2]/button[2]').click()
            browser.execute_script("document.getElementById('msg-overlay').style.display = 'none';")
            hol_up()
            # browser.find_element_by_id('ember180').click()                                # Click Location Dropdown
            browser.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[1]/header/div/div/div[2]/div/div/div[2]/ul/li[4]/form/button').click()
            hol_up()
            # browser.find_element_by_xpath('//*[@id="ember185"]/input').send_keys(city)    # Input City
            browser.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[1]/header/div/div/div[2]/div/div/div[2]/ul/li[4]/form/div/fieldset/div/div[1]/div/div/input').send_keys(city)
            hol_up()
            # browser.find_element_by_id('triggered-expanded-ember184').click()             # Click Dropdown Result
            browser.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[1]/header/div/div/div[2]/div/div/div[2]/ul/li[4]/form/div/fieldset/div/div[1]/div/div[2]').click()
            hol_up()
            # browser.find_element_by_id('ember189').click()                                # Click Apply
            browser.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[1]/header/div/div/div[2]/div/div/div[2]/ul/li[4]/form/div/fieldset/div/div[2]/div/button[2]/span').click()
            hol_up()
            # browser.find_element_by_xpath('//*[@id="ember16"]/input').send_keys("test")   # Input Keyword To Search 
            browser.find_element_by_xpath('/html/body/div[7]/header/div[2]/div/div/div[1]/div/input').send_keys(keyword)
            browser.find_element_by_class_name('search-global-typeahead__button').click() # Click search button
            hol_up()
            
            res_count = browser.find_element_by_class_name('search-results__total').text.split(" ")[1]
            page_count = 100
            if int(res_count.replace(",","")) < 100: 
                page_count = res_count / 10

            print("- " + str(res_count) + " Results For '" + keyword + "' in '" + city + "'.")
            print("- " + str(page_count) + " Pages of Results")
            
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            hol_up()

            query_url = browser.current_url
            batch = []
    
            print("===== Collecting Usernames From Query")
            print("=--- Page 1 ----")
            links = browser.find_elements_by_xpath("//a[@href]")
            users = links_2_users(links)
            batch.extend(users)
            print(users)

            # TMP
            page_count = 3
            # TMP

            for page in range(2, page_count):
                print("=--- Page " + str(page) + " ----")
                page_url = query_url + "&page=" + str(page)
                hol_up()
                browser.get(page_url)
                hol_up()
                links = browser.find_elements_by_xpath("//a[@href]")
                users = links_2_users(links)
                hol_up()
                batch.extend(users)
            
            print("===== Viewing Each Profile ")
            print("- " + str(len(batch)) + " Usernames Connected in this batch")
        
            for usr in batch:
                
                if usr not in log['users']:
                    hol_up()
                    browser.get("https://www.linkedin.com/in/" + usr + "/")
                    log['users'].append(usr)
                    log['cities'][city.replace(" ", "")] += 1
                    hol_up()

            #################################


            # time.sleep(30)

            # kill_session()

# except(err):
#     print(err)
#     save()      

print('=== MAIN ===')
start_time = int(round(time.time() * 1000))
# login()
# get_stats()
# begin()




# !!! https://stackoverflow.com/questions/33225947/can-a-website-detect-when-you-are-using-selenium-with-chromedriver

# https://en.wikipedia.org/wiki/List_of_towns_and_cities_with_100,000_or_more_inhabitants/country:_C

# https://www.linkedin.com/search/results/all/?keywords=recruiter&origin=GLOBAL_SEARCH_HEADER
# https://www.linkedin.com/search/results/people/?facetNetwork=%5B%22O%22%5D&facetProfileLanguage=%5B%22en%22%2C%22fr%22%5D&keywords=recruiter&origin=FACETED_SEARCH
# https://www.linkedin.com/search/results/people/?facetNetwork=%5B%22O%22%5D&facetProfileLanguage=%5B%22en%22%2C%22fr%22%5D&keywords=recruiter%2C%20acquisition&origin=GLOBAL_SEARCH_HEADER&page=2


