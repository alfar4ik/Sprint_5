from Pages.base_page import BasePage
from Pages.registration_page import RegistrationHelper
from conftest import driver_init
from conftest import unique_email


class TestRegistration:
    def test_registration_new_user(self, driver_init, unique_email):
        user_name = "Vladimir"
        password = "276321535"
        expected_url = "https://stellarburgers.nomoreparties.site/login"

        base_page = BasePage(driver_init)
        BasePage(driver_init).open_url("https://stellarburgers.nomoreparties.site/login")
        registration_page = RegistrationHelper(driver_init)


        registration_page.click_registration_new_user()
        registration_page.enter_name(user_name)
        registration_page.enter_email(unique_email)
        registration_page.enter_password(password)
        assert not registration_page.is_name_field_empty(), "Поле 'Имя' пустое!"
        registration_page.click_register_button()
        is_redirected = base_page.wait_for_url_to_be(expected_url)
        assert is_redirected, f"Произошла ошибка при регистрации нового пользователя. Ожидаемый URL: {expected_url}, текущий URL: {base_page.driver.current_url}"

