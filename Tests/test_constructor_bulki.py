
from Pages.base_page import BasePage
from Pages.login_page import LoginPageHelper
from conftest import driver_init



class TestConstructor:
    def test_click_on_constructor(self, driver_init):
        BasePage(driver_init).open_url("https://stellarburgers.nomoreparties.site/")
        login_page = LoginPageHelper(driver_init)
        login_page.click_login_in_my_account()
        login_page.click_personal_cabinet_email("alfavlady124@gmail.com")
        login_page.click_personal_cabinet_password("2763213")
        login_page.click_personal_cabinet_login()
        login_page.click_on_nachinki_button()
        login_page.click_on_bulki_button()
        assert login_page.waiting_for_bulki_tab(), "Таймаут ожидания: вкладка 'Булки' не появилась на странице в течение заданного времени"

