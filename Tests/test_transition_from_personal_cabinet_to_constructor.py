from Pages.base_page import BasePage
from Pages.transition_through_login import LoginTransitionHelper
from conftest import driver_init


class TestLogin:
    def test_login_by_personal_cabinet(self, driver_init):
        BasePage(driver_init).open_url("https://stellarburgers.nomoreparties.site/")
        login_page = LoginTransitionHelper(driver_init)
        login_page.click_personal_cabinet()
        login_page.click_personal_cabinet_email("alfavlady124@gmail.com")
        login_page.click_personal_cabinet_password("2763213")
        login_page.click_personal_cabinet_login()
        login_page.click_personal_cabinet_authorized()
        login_page.click_to_constructor()
        login_page.waiting_for_page_constructor()