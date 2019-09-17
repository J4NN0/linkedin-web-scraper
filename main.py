import configparser
import time
from selenium import webdriver
from browserNavigator import BrowserNavigator
from cookieManager import CookieManager


def main():
    config = configparser.ConfigParser()
    config.read('config.ini')

    print("Loading browser...")
    browser = None

    if config['BROWSER']['WEBDRIVER'] == "Firefox":
        browser = webdriver.Firefox()
    elif config['BROWSER']['WEBDRIVER'] == "Chrome":
        browser = webdriver.Chrome("./chromedriver")
    else:
        print("Set in the config.in file as WEBDRIVER Firefox or Chrome. Restarting...")
        time.sleep(5)
        exit()

    page = BrowserNavigator(browser)
    page.log_in()

    CookieManager.save_cookies(browser)

    links_company_lyon = page.get_companies_name('https://www.linkedin.com/search/results/companies/?keywords=Lyon')

    print(str(links_company_lyon))

    # at this point it could be used also the scrapy spider web scraper but you need to retrive cookie and send it in
    # request message
    # Scraper(links)

    # or continuing to use selenium to retrive the data from linkedin
    page.retrieve_data(links_company_lyon, 'lyon_companies.xlsx')

    print("Closing browser...")
    browser.close()


if __name__ == '__main__':
    main()
