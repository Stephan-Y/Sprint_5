from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import *

class TestSignIn(Locators):

    def input_user_data(self, driver):
        driver.find_element(*self.FIELD_EMAIL).send_keys(users_email)  # поле "Email"
        driver.find_element(*self.FIELD_PASSWORD).send_keys(users_password)  # поле "Пароль"
        driver.find_element(*self.ENTER_BUTTON).click()  # кнопка "Войти"
    def test_sign_in_button_on_main_page(self, driver):
        driver.find_element(*self.ENTER_TO_ACCOUNT_BUTTON).click()  # кнопка "Войти в аккаунт"
        self.input_user_data(driver)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((self.MAKE_ORDER_BUTTON)))
        assert driver.find_element(*self.MAKE_ORDER_BUTTON).text == 'Оформить заказ'
        driver.quit()

    def test_personal_account_button_on_main_page(self, driver):
        driver.find_element(*self.PERSONAL_ACCOUNT_BUTTON).click()  # кнопка "Личный кабинет"
        self.input_user_data(driver)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((self.MAKE_ORDER_BUTTON)))
        assert driver.find_element(*self.MAKE_ORDER_BUTTON).text == 'Оформить заказ'
        driver.quit()

    def test_sign_in_button_on_register_page(self, driver):
        driver.find_element(*self.PERSONAL_ACCOUNT_BUTTON).click()  # кнопка "Личный кабинет"
        driver.find_element(*self.REGISTRATION_ON_ENTER_PAGE).click()  # кнопка "Зарегистрироваться"
        driver.find_element(*self.PERSONAL_ACCOUNT_BUTTON).click()  # кнопка "Войти"
        self.input_user_data(driver)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((self.MAKE_ORDER_BUTTON)))
        assert driver.find_element(*self.MAKE_ORDER_BUTTON).text == 'Оформить заказ'
        driver.quit()

    def test_sign_in_button_on_recovery_password_page(self, driver):
        driver.find_element(*self.PERSONAL_ACCOUNT_BUTTON).click()  # кнопка "Личный кабинет"
        driver.find_element(*self.RECOVERY_PASSWORD_ON_ENTER_PAGE).click()  # кнопка "Восстановить пароль"
        driver.find_element(*self.PERSONAL_ACCOUNT_BUTTON).click()  # кнопка "Войти"
        self.input_user_data(driver)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((self.MAKE_ORDER_BUTTON)))
        assert driver.find_element(*self.MAKE_ORDER_BUTTON).text == 'Оформить заказ'
        driver.quit()