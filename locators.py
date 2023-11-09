from selenium.webdriver.common.by import By

class LoginPageLocators:
    PERSONAL_CABINET = (By.XPATH, '//p[contains(text(),"Личный Кабинет")]')
    # Локатор для кнопки  "Личный кабинет" на главной странице

    PERSONAL_CABINET_EMAIL = (
        By.XPATH, "//label[text()='Email']/following-sibling::input[@type='text']"

    )
    # Локатор для поля ввода email в форме входа в личный кабинет

    PERSONAL_CABINET_PASSWORD = (
        By.XPATH, "//input[@name='Пароль' and @type='password']")
    # Локатор для поля ввода пароля в форме входа в личный кабинет

    PERSONAL_CABINET_LOGIN = (By.XPATH, "//button[contains(text(),'Войти')]")
    # Локатор для кнопки "Войти" в форме входа в личный кабинет

    LOGIN_IN_MY_ACCOUNT = (By.XPATH, "//button[contains(text(),'Войти в аккаунт')]")
    # Локатор для кнопки "Войти в аккаунт"

    LOGIN_THROUGH_REGISTRATION = (By.XPATH, "//a[contains(text(),'Зарегистрироваться')]")
    # Локатор для логина через  переход на страницу регистрации

    LOGIN_THROUGH_ALREADY_REGISTERED = (By.XPATH, "//a[contains(text(),'Войти')]")
    # Локатор для входа (для пользователей, которые уже зарегистрированы)

    LOGIN_THROUGH_RECOVERY_PASSWORD = (By.XPATH, "//a[contains(text(),'Восстановить пароль')]")
    # Локатор для входа  через поле "Восстановить пароль"

    LOGIN_THROUGH_REMEMBERED_PASSWORD = (By.XPATH, "//a[contains(text(),'Войти')]")
    # Локатор для входа  (если пользователь вспомнил пароль, используется для возврата на страницу входа)

    LOGOUT_FROM_ACCOUNT = (By.XPATH, "//button[contains(text(),'Выход')]")
    # Локатор для кнопки выхода из аккаунта

    CLICK_ON_NACHINKI_BUTTON = (By.XPATH, "//span[contains(text(),'Начинки')]")
    # Локатор для кнопки  "Начинки" (для  выбора ингредиентов бургера)

    CLICK_ON_SOUSE_BUTTON = (By.XPATH, "//span[contains(text(),'Соусы')]")
    # Локатор для кнопки "Соусы" (для выбора соусов)

    CLICK_ON_BULKI_BUTTON = (By.XPATH, "//span[contains(text(),'Булки')]")
    # Локатор для кнопки "Булки" (для выбора булок для бургера)

    NACHINKI_TAB_VISIBLE = (By.XPATH, "(//div[contains(@class, 'tab_tab__')])[3]/span[text()='Начинки']")

    BULKI_TAB_VISIBLE = (By.XPATH, "(//div[contains(@class, 'tab_tab__')])[1]/span[text()='Булки']")

    SOUSE_TAB_VISIBLE = (By.XPATH, "(//div[contains(@class, 'tab_tab__')])[2]/span[text()='Соусы']")