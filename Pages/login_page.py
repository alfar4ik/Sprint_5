from Pages.base_page import BasePage
from locators import LoginPageLocators



class LoginPageHelper(BasePage):
    def __init__(self, driver_init):
        super().__init__(driver_init)
        self.__check_page()

    def __check_page(self):
        self.find_element(LoginPageLocators.PERSONAL_CABINET)
    def click_personal_cabinet(self):
        self.find_element(LoginPageLocators.PERSONAL_CABINET).click()

    def click_personal_cabinet_email(self, email):
        email_field = self.find_element(LoginPageLocators.PERSONAL_CABINET_EMAIL)
        email_field.clear()
        email_field.send_keys(email)
    def click_personal_cabinet_password(self, password):
        password_field = self.find_element(LoginPageLocators.PERSONAL_CABINET_PASSWORD)
        password_field.clear()
        password_field.send_keys(password)

    def click_personal_cabinet_login(self):
        self.find_element(LoginPageLocators.PERSONAL_CABINET_LOGIN).click()


    def click_login_in_my_account(self):
        self.find_element(LoginPageLocators.LOGIN_IN_MY_ACCOUNT).click()

    def click_login_through_registration(self):
        self.find_element(LoginPageLocators.LOGIN_THROUGH_REGISTRATION).click()


    def click_login_through_already_registered(self):
        self.find_element(LoginPageLocators.LOGIN_THROUGH_ALREADY_REGISTERED).click()


    def click_login_through_recovery_password(self):
        self.find_element(LoginPageLocators.LOGIN_THROUGH_RECOVERY_PASSWORD).click()

    def click_login_through_remembered_password(self):
        self.find_element(LoginPageLocators.LOGIN_THROUGH_REMEMBERED_PASSWORD).click()

    def click_log_out_from_my_account(self):
        self.find_element(LoginPageLocators.LOGOUT_FROM_ACCOUNT).click()


    def click_on_nachinki_button(self):
        self.find_element(LoginPageLocators.CLICK_ON_NACHINKI_BUTTON).click()

    def click_on_souse_button(self):
        self.find_element(LoginPageLocators.CLICK_ON_SOUSE_BUTTON).click()

    def click_on_bulki_button(self):
        self.find_element(LoginPageLocators.CLICK_ON_BULKI_BUTTON).click()






