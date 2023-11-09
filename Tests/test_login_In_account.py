from Pages.base_page  import BasePage
from Pages.login_page import LoginPageHelper
from conftest import driver_init


class TestLoginMyAccount:
    def test_login_in_my_account(self, driver_init):
        BasePage(driver_init).open_url("https://stellarburgers.nomoreparties.site/")
        login_page = LoginPageHelper(driver_init)
        login_page.click_login_in_my_account()
        login_page.click_personal_cabinet_email("alfavlady124@gmail.com")
        login_page.click_personal_cabinet_password("2763213")
        login_page.click_personal_cabinet_login()
        login_page.waiting_for_page()

