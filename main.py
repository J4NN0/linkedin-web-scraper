import configparser
import time
from selenium import webdriver
from BrowserNavigator.browserNavigator import BrowserNavigator
from BrowserNavigator.cookieManager import CookieManager


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
        print("Set in config.in file as WEBDRIVER either Firefox or Chrome. Restarting...")
        time.sleep(5)
        exit()

    page = BrowserNavigator(browser)
    page.log_in()

    CookieManager.save_cookies(browser)

    links_company = page.get_companies_name(f"https://www.linkedin.com/search/results/companies/?keywords={config['COMPANIES']['CITY']}")

    print(str(links_company))

    # at this point it could be used also the scrapy spider web scraper but you need to retrieve cookie and send it in
    # request message
    # Scraper(links)

    # or continuing to use selenium to retrieve the data from linkedin
    page.retrieve_data(links_company, 'companies.xlsx')

    print("Closing browser...")
    browser.close()


if __name__ == '__main__':
    main()
