import configparser
import time
from selenium import webdriver
from browserNavigator import BrowserNavigator
from cookieManager import CookieManager


def join_list(list1, list2):
    joined_list = []

    for l1 in list1:
        if l1 in list2:
            joined_list.append(l1)

    return joined_list


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

    links_esn_lyon = page.get_companies_name('https://www.linkedin.com/search/results/companies/?keywords=ESN%20Lyon')
    links_ssi_lyon = page.get_companies_name('https://www.linkedin.com/search/results/companies/?keywords=SSII%20Lyon')

    print(str(links_esn_lyon))
    print(str(links_ssi_lyon))

    page.retrieve_data(links_esn_lyon, 'esn_lyon.xlsx')
    page.retrieve_data(links_ssi_lyon, 'ssi_lyon.xlsx')

    joined_links = join_list(links_esn_lyon, links_ssi_lyon)
    print(str(joined_links))
    page.retrieve_data(joined_links, 'join_ssi_lyon.xlsx')

    print("Closing browser...")
    browser.close()


if __name__ == '__main__':
    main()
