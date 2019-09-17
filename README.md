# DISCLAIMER

Any actions and or activities related to the material contained within this repo is solely your responsibility. The misuse of the information in this repo can result in criminal charges brought against the company in question. The author will not be held responsible in the event any criminal charges be brought against any individuals misusing the information in this repo to break the law.

As written in [Linkedin User Agreement](https://www.linkedin.com/legal/user-agreement): *you agree you will not use*
    
   - bots or other automated methods to access the Services, add or download contacts, send or redirect messages.
   
I do not promote, encourage, support or excite any illegal activity or hacking without written permission in general.

# linkedin-web-scraper

Python Web Scraper for LinkedIn companies. Scraping data from web browser and collect it into an .xls file.

# Usage

First of all donwload the web driver you prefer (Firefox or Chrome) and put it inside the folder. Then put you credential inside the **config.ini** file and specify the web driver you donwloaded. Also others kind of parameters can be setted. 

The method *get_companies_name(...)* requires a link (in this case a link of a company likns) and will return an array of links in which each link is the page of the company.

After that, you can run *retrive_data(...)* that requires the array with the links and the name of the .xls file in which you want to store information collected from each link for each company. The class ManageExcelFile will handle the I/O operation for the .xls file.

# Issues

It could happen that, after the loggin phase, LinkedIn could ask you to perform some operations instead of rediricet you to the feed (https://www.linkedin.com/feed/) page. 

In this case just:
  1. Stop the script
  2. Log with a browser in your account
  3. Skip the required operation
  4. Re-run the code

# Utility

- [Chrome Webdriver](https://chromedriver.chromium.org/downloads)
- [Selenium](https://selenium-python.readthedocs.io/installation.html)
- [Scrapy](https://docs.scrapy.org/en/latest/intro/tutorial.html)
