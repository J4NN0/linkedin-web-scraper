# DISCLAIMER

Any actions and or activities related to the material contained within this repo is solely your responsibility. The misuse of the information in this repo can result in criminal charges brought against the company in question. The author will not be held responsible in the event any criminal charges be brought against any individuals misusing the information in this repo to break the law.

As written in [Linkedin User Agreement](https://www.linkedin.com/legal/user-agreement): **you agree you will not use**
    
   - bots or other automated methods to access the Services, add or download contacts, send or redirect messages.
   
### Terms And Conditions:

- I do not promote, encourage, support or excite any illegal activity or hacking without written permission in general. The repo and author of the repo is no way responsible for any misuse of the information.
- "linkedin-web-scraper" is just a terms that represents the name of the repo and is not a repo that provides any illegal information.
- This repo is totally meant for providing information on Computer Software, Computer Programming and other related topics.
- The Software's and Scripts provided by the repo should only be used for education purposes. The repo or the author can not be held responsible for the misuse of them by the users.
- I am not responsible for any direct or indirect damage caused due to the usage of the code provided on this site. All the information provided on this repo are for educational purposes only.

# LinkedIn Web Scraper

This is a LinkedIn Python Web Scraper for companies. The script fully simulate a human activity (using [Selenium](https://selenium-python.readthedocs.io) library) in order to get data from LinkedIn web pages. The purpose is store data from companies of a certain zone, such as:

- Name 
- Overview 
- Size
- Website link
- Industry
- etc.

After collected the above information, these will be stored into an `.xls` file.

### Demo

[![Watch the video](https://img.youtube.com/vi/TKkJEo-4NTg/maxresdefault.jpg)](https://youtu.be/TKkJEo-4NTg)

# Table of Contents
- [Usage](https://github.com/J4NN0/linkedin-web-scraper#usage)
- [Troubleshooting](https://github.com/J4NN0/linkedin-web-scraper#troubleshooting)
- [Resources](https://github.com/J4NN0/linkedin-web-scraper#resources)

# Usage

First of all, download the web driver you prefer (either [Firefox](https://github.com/mozilla/geckodriver/releases) or [Chrome](https://chromedriver.chromium.org/downloads)) and put it inside project folder. After that, put your credentials in `config.ini` file and specify the `webdriver` you have downloaded. Also, others kind of parameters can be set. 

Method `get_companies_name(...)` requires a link (in this case a link of a company) and will return an array of links in which each link is the LinkedIn company web page.

After that, you can run `retrieve_data(...)` that requires the array with the links and the name of the `.xls` file in which you want to store all the information that will be collected from each link for each company. 

Class `ManageExcelFile` will handle the I/O operation to the `.xls` file.

# Troubleshooting

It could happen that, after the logging phase, LinkedIn could ask you to perform some actions/operations (e.g. "I'm not a robot", etc.) instead of redirecting you to the feed (https://www.linkedin.com/feed/) page. 

In this case:
  1. Stop the script.
  2. Log in with a browser in your account.
  3. Skip the required actions.
  4. Re-run the code.

# Resources

- [Chrome Webdriver](https://chromedriver.chromium.org/downloads)
- [Firefox Webdriver](https://github.com/mozilla/geckodriver/releases)
- [Selenium](https://selenium-python.readthedocs.io/installation.html)
- [Scrapy](https://docs.scrapy.org/en/latest/intro/tutorial.html)
