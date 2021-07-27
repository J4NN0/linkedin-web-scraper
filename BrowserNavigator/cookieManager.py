import json
from selenium import webdriver
from BrowserNavigator.browserNavigator import BrowserNavigator


class CookieManager:

    @staticmethod
    def save_cookies(browser):
        print("Saving cookies")
        data = browser.get_cookies()
        with open('cookie.json', 'w') as cookies_file:
            json.dump(data, cookies_file)
        cookies_file.close()

    def get_cookies(self):
            cookie = None
            while cookie is None:
                try:
                    cookie = self._get_cookies_from_file()
                except FileNotFoundError:
                    self._generate_cookies_file()
            return cookie

    @staticmethod
    def _get_cookies_from_file():
        with open('cookie.json', 'r') as input_file:
            cookie = json.load(input_file)
        input_file.close()
        return cookie

    def _generate_cookies_file(self):
        print("Failed loading cookies. Retrieving them again.")
        browser = webdriver.Firefox()
        page = BrowserNavigator(browser)
        page.log_in()
        self.save_cookies(browser)
        print("closing browser")
        browser.close()
