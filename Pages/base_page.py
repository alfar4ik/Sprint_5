from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators import LoginPageLocators

class BasePage:
    def __init__(self, driver_init):
        self.driver = driver_init

    def find_element(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(locator), message=f" Не дождались {locator}")

    def wait_for_url_to_be(self, url, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(lambda driver: driver.current_url == url)
            return True
        except TimeoutException:
            return False

    def waiting_for_bulki_tab(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(LoginPageLocators.BULKI_TAB_VISIBLE))
            return True
        except TimeoutException:
            return False

    def waiting_for_nachinki_tab(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(LoginPageLocators.NACHINKI_TAB_VISIBLE))
            return True
        except TimeoutException:
            return False


    def waiting_for_souse_tab(self, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(LoginPageLocators.SOUSE_TAB_VISIBLE))
            return True
        except TimeoutException:
            return False


    def waiting_for_log_out_page(self):
        expected_url = "https://stellarburgers.nomoreparties.site/login"
        WebDriverWait(self.driver, 10).until(EC.url_to_be(expected_url))
        assert self.driver.current_url == expected_url


    def waiting_for_page(self):
        expected_url = "https://stellarburgers.nomoreparties.site/"
        WebDriverWait(self.driver, 10).until(EC.url_to_be(expected_url))
        assert self.driver.current_url == expected_url


    def waiting_for_page_constructor(self):
        expected_url = "https://stellarburgers.nomoreparties.site/"
        WebDriverWait(self.driver, 10).until(EC.url_to_be(expected_url))
        assert self.driver.current_url == expected_url


    def waiting_for_pages(self):
        expected_url = "https://stellarburgers.nomoreparties.site/account/profile"
        WebDriverWait(self.driver, 10).until(EC.url_to_be(expected_url))
        assert self.driver.current_url == expected_url


    def open_url(self, url):
        return self.driver.get(url)

