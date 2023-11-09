from Pages.base_page import BasePage
from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    REGISTRATION_PAGE_NEW_USER = (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]")
    # Локатор для перехода на страницу регистрации нового пользователя

    NAME_INPUT = (
        By.XPATH, "//label[text()='Имя']/following-sibling::input[@type='text']"

    )
    # Локатор для поля ввода имени пользователя на странице регистрации

    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input[@type='text']")
    # Локатор для поля ввода электронной почты на странице регистрации

    PASSWORD_INPUT = (
    By.XPATH, "//input[@name='Пароль' and @type='password']")
    # Локатор для поля ввода пароля на странице регистрации

    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(),'Зарегистрироваться')]")
    # Локатор для кнопки подтверждения регистрации

    PASSWORD_ERROR_LOCATOR = (By.XPATH, "//p[contains(text(),'Некорректный пароль')]")
    # Локатор для сообщения об ошибке в случае ввода некорректного пароля



class RegistrationHelper(BasePage):
    def __init__(self, driver_init):
        super().__init__(driver_init)
        self.__check_page()

    def __check_page(self):
        self.find_element(RegistrationPageLocators.REGISTRATION_PAGE_NEW_USER)

    def click_registration_new_user(self):
        self.find_element(RegistrationPageLocators.REGISTRATION_PAGE_NEW_USER).click()

    def enter_name(self, name):
        name_field = self.find_element(RegistrationPageLocators.NAME_INPUT)
        name_field.clear()
        name_field.send_keys(name)
    def enter_email(self, email):
        email_field = self.find_element(RegistrationPageLocators.EMAIL_INPUT)
        email_field.clear()
        email_field.send_keys(email)

    def enter_password(self, password):
        self.check_password_length(password)
        password_field = self.find_element(RegistrationPageLocators.PASSWORD_INPUT)
        password_field.clear()
        password_field.send_keys(password)

    def click_register_button(self):
        self.find_element(RegistrationPageLocators.REGISTER_BUTTON).click()

    def check_password_length(self, password):
        assert len(password) >= 6, "Пароль должен содержать минимум 6 символов"

    def is_name_field_empty(self):
        name_field = self.find_element(RegistrationPageLocators.NAME_INPUT)
        return not bool(name_field.get_attribute("value"))

    def is_redirected_to_login_page(self):
        return self.driver.current_url == "https://stellarburgers.nomoreparties.site/login"




