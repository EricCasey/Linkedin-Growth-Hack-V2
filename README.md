# The Headhunter.py Growth Hack
## By Eric Casey

* *Disclaimer #0: This is a work in progress (Sept/Oct 2020)*   
* *Disclaimer #1: If you're from Linkedin and want this taken down pls LMK.* 

### wtf is this?
This is a proof-of-concept for a bot that conducts wide searches on Linkedin for user-provided lists of job titles (like 'Ice Salesman, Penguin Whisperer, Flat Earther') and locales (like 'Casey Station, Puerto Baquerizo Moreno, North Pole') and automatically views each user's profile for a few seconds.

Then, depending on that user's number of connections or notificaitons or settings, they might receive notifications to their accounts. 

At what rate you might ask? 

Well, if I can get a reciprocal view rate of > 0.03% (a typical programmatic marketing CTR benchmark) I will consider this to be a success.

(If I have results they'll be summarized in ./postmortem.ipynb)

### The Story

When I signed up for LinkedIn after business school I quickly noticed that you get a notification when someone else views your profile.

In 2014-ish I was looking for work and noticed that when I viewed a person's profile they would sometimes look at my profile hours, days or weeks later. At that point I had ~50 connections, and at the time, I thought that having that fancy blue [500+]() on my profile would help in the future. 

The first iteration of this tool was [Galaxy-Screen-Scripts](https://github.com/EricCasey/Galaxy-Screen-Scripts) and was simply a thumb-recorded screen script using a program that was typically used at the time to make bots for Farmville. All I had to do was search for something like 'recruiter london', start the script, and it would view 1 profile every 2 seconds (throttled a little to let the page load). It got me the 500+ then I stopped, in fear of getting banned.

**This time though...** I'm going all in using what I've learned since then, and doing my best to document it. 

(If I have results they'll be in ./results.ipynb)

### Recommendations

Linkedin could mitigate this by setting a internal limit of notifications sent to users stemming from a single user.

### See It In Action

<center>
* gif here
<img scr=""/>
</center>

### Results

<center>
* line graph here, other vis
<img scr=""/>
</center>

### Contents

Heads Up: files with * next to them you need to download yourself.

```python
./README.md                   # You're lookin' at it
./headhunter.py               # Main bot script
./postmortem.ipynb            # Analysis of Results. 
./cities.txt                  # Custom list of cities to search in 
./keywords.txt                # Custom list of keywords to search
./chromedriver              * # https://chromedriver.chromium.org/downloads
./template.json               # DB Record Template
./logs/                       # v- Generated after first run -v
    ./master_user_log.txt     # All users viewed so far
    ./master_query_log.txt    # All queries completed so far
    ./log-dd-mm-yyyy.json     # Log of actions taken by day
```

### Usage

* Tested on Macbook & Raspberry Pi 2

1. **`~$`**`git clone https://github.com/EricCasey/Linkedin-Growth-Hack-V2.git`

2. Download the correct [Chromedriver](https://chromedriver.chromium.org/downloads) for your version of Chrome and put it in the project root. Use `apt-get install chromium-driver` on and ARM chip (rpi)

3. **`~$`**`pip3 install shutil signal random datetime selenium`

4. **`~$`**`python3 ./headhunter.py <linkedin_email> <linkedin_password> <speed>`  


<!-- * https://stackoverflow.com/questions/33225947/can-a-website-detect-when-you-are-using-selenium-with-chromedriver -->

