# linkedin-web-scraper
Python Web Scraper for LinkedIn companies. It performs search for companies to collect data about them. Then it stores the collected information into an .xls file.

# Usage

First of all donwload the web driver you prefer (Firefox or Chrome) and put it inside the folder. Then put you credential inside the **config.ini** file and specify the web driver you donwloaded. Also others kind of parameters can be setted. 

The method *get_companies_name(...)* requires a link (in this case a link of a company likns) and will return an array of links in which each link is the page of the company.

After that, you can run *retrive_data(...)* that requires the array with the links and the name of the .xls file in which you want to store information collected from each link for each company. The class ManageExcelFile will handle the I/O operation for the .xls file.

# Issues

It could happen that, after the loggin phase, LinkedIn could ask you to perform some operations (such as recaptcha, etc.) instead of rediricet you to the feed (https://www.linkedin.com/feed/) page. 

In this case just:
  1. Stop the script
  2. Log with a browser in your account
  3. Skip the required operation
  4. Re-run the code

# Utility

- [Chrome Webdriver](https://chromedriver.chromium.org/downloads)
- [Selenium](https://selenium-python.readthedocs.io/installation.html)
- [Scrapy](https://docs.scrapy.org/en/latest/intro/tutorial.html)
