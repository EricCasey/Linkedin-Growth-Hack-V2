# The Headhunter.py Growth Hack
## By Eric Casey

* *Disclaimer #0: This is a work in progress (Sept/Oct 2020)*   
* *Disclaimer #1: If you're from Linkedin and want this taken down LMK.*   
* *Disclaimer #2: If I viewed your profile recently I've kept track of every profile I've viewed so I don't bother anyone twice, the last time I did this was several years ago.* 

### wtf is this?
This is a proof-of-concept for a bot that conducts wide searches for user-provided job titles (like 'recruiter') and locales (like Lima, Peru) and automatically views each user's profile.

Then, depending on that user's number of connections or notificaitons or settings, they might receive notifications to their accounts. 

If I can get a reciprocal view rate of > 0.03% (a typical programmatic marketing CTR benchmark) I will consider this to be a success.

(If I have results they'll be in ./results.ipynb)

### The Story

When I signed up for LinkedIn after business school I quickly noticed that you get a notification when someone else views your profile. This was the root of the whole idea.

In 2014-ish I was looking for work and noticed that when I viewed a person's profile they would sometimes look at my profile hours, days or weeks later. At that point I had ~50 connections, and at the time, I thought that having that fancy blue [500+]() on my profile would help in the future. Maybe a recruiter would see [500+]() and think "damn, this guy is connected. my client/boss is going to love this guy" or my enemies from middle school would see it and it would be nice cold revenge (_yikes_, I know...).  

Anyway, the first iteration of this tool was [Galaxy-Screen-Scripts](https://github.com/EricCasey/Galaxy-Screen-Scripts) and was simply a thumb-recorded screen script using a program that was typically used at the time to make bots for Farmville. All I had to do was search for something like 'recruiter london', start the script, and it would view 1 profile every 2 seconds (to let the page load). It got me the 500+ then I stopped, in fear of getting banned.

**This time though...** I'm going all in using what I've learned since then, and doing my best to document it.

(If I have results they'll be in ./results.ipynb)

### See It In Action

<center>
*gif here
<img scr=""/>
</center>


### Results

<center>
* line graph here
<img scr=""/>
</center>

### Contents
```python
./README.md                   # You're lookin' at it
./headhunter.py               # Main bot script
./results.ipynb               # Post-Mortem
./cities.txt                  # Custom list of cities to search in
./keywords.txt                # Custom list of keywords to search
./logs/
    ./master_user_log.txt     # All users viewed so far
    ./template.json           # DB R\record T\template
    ./log-dd-mm-yyyy.json     # Log of actions taken by day
```

### Usage

* Download Chromedriver for Selenium

`pip3 install json, time, shutil, signal, random, datetime, selenium`

`~$ python3 ./headhunter.py <linkedin_email> <linkedin_password>`  

Then don't touch that computer or use Linkedin on other devices for a few weeks... I ran it on a Raspberry Pi connected to an old TV.



<!-- 
# !!! https://stackoverflow.com/questions/33225947/can-a-website-detect-when-you-are-using-selenium-with-chromedriver
# https://en.wikipedia.org/wiki/List_of_towns_and_cities_with_100,000_or_more_inhabitants/country:_C
# https://www.linkedin.com/search/results/all/?keywords=recruiter&origin=GLOBAL_SEARCH_HEADER
# https://www.linkedin.com/search/results/people/?facetNetwork=%5B%22O%22%5D&facetProfileLanguage=%5B%22en%22%2C%22fr%22%5D&keywords=recruiter&origin=FACETED_SEARCH
# https://www.linkedin.com/search/results/people/?facetNetwork=%5B%22O%22%5D&facetProfileLanguage=%5B%22en%22%2C%22fr%22%5D&keywords=recruiter%2C%20acquisition&origin=GLOBAL_SEARCH_HEADER&page=2 -->



