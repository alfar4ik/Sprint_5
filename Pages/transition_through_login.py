from Pages.base_page import BasePage
from selenium.webdriver.common.by import By



class TransitionLocators:
    PERSONAL_CABINET = (By.XPATH, '//p[contains(text(),"Личный Кабинет")]')
    # Локатор для кнопки перехода в личный кабинет пользователя

    PERSONAL_CABINET_EMAIL = (
    By.XPATH, "//label[text()='Email']/following-sibling::input[@type='text']")
    # Локатор для поля ввода электронной почты в форме входа в личный кабинет

    PERSONAL_CABINET_PASSWORD = (
    By.XPATH, "//input[@name='Пароль' and @type='password']")
    # Локатор для поля ввода пароля в форме входа в личный кабинет

    PERSONAL_CABINET_LOGIN = (By.XPATH, "//button[contains(text(),'Войти')]")
    # Локатор для кнопки входа в личный кабинет

    PERSONAL_CABINET_AUTHORIZED = (By.XPATH, "//p[contains(text(),'Личный Кабинет')]")
    # Локатор для проверки успешного входа в личный кабинет

    PERSONAL_CABINET_CONSTRUCTOR = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    # Локатор для кнопки  перехода к конструктору бургеров


class LoginTransitionHelper(BasePage):
    def __init__(self, driver_init):
        super().__init__(driver_init)
        self.__check_page()

    def __check_page(self):
        self.find_element(TransitionLocators.PERSONAL_CABINET)


    def click_personal_cabinet(self):
        self.find_element(TransitionLocators.PERSONAL_CABINET).click()

    def click_personal_cabinet_email(self, email):
        email_field = self.find_element(TransitionLocators.PERSONAL_CABINET_EMAIL)
        email_field.clear()
        email_field.send_keys(email)

    def click_personal_cabinet_password(self, password):
        password_field = self.find_element(TransitionLocators.PERSONAL_CABINET_PASSWORD)
        password_field.clear()
        password_field.send_keys(password)

    def click_personal_cabinet_login(self):
        self.find_element(TransitionLocators.PERSONAL_CABINET_LOGIN).click()

    def click_personal_cabinet_authorized(self):
        self.find_element(TransitionLocators.PERSONAL_CABINET_AUTHORIZED).click()


    def click_to_constructor(self):
        self.find_element(TransitionLocators.PERSONAL_CABINET_CONSTRUCTOR).click()


