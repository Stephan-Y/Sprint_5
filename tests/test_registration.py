from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from data import *
class TestRegistration(Locators):

    def test_correct_registration(self, driver, login, correct_password):
        driver.find_element(*self.PERSONAL_ACCOUNT_BUTTON).click()  # клик на Личный кабинет
        driver.find_element(*self.REGISTRATION_BUTTON).click()  # Зарегистрироваться
        driver.find_element(*self.REGISTRATION_FIELD_NAME).send_keys(user_name)  # Имя
        driver.find_element(*self.REGISTRATION_FIELD_EMAIL).send_keys(login)  # Почта
        driver.find_element(*self.REGISTRATION_FIELD_PASSWORD).send_keys(correct_password)  # Пароль
        driver.find_element(*self.FINAL_REGISTRATION_BUTTON).click()  # Зарегистрироваться
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((self.ENTER_BUTTON)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login', 'URL не совпадает'


    def test_incorrect_registration(self, driver, login, incorrect_password):
        driver.find_element(* self.PERSONAL_ACCOUNT_BUTTON).click()  # клик на Личный кабинет
        driver.find_element(*self.REGISTRATION_BUTTON).click()  # Зарегистрироваться
        driver.find_element(*self.REGISTRATION_FIELD_NAME).send_keys(user_name)  # Имя
        driver.find_element(*self.REGISTRATION_FIELD_EMAIL).send_keys(login)  # Почта
        driver.find_element(*self.REGISTRATION_FIELD_PASSWORD).send_keys(incorrect_password)  # Некорректный ароль
        driver.find_element(*self.FINAL_REGISTRATION_BUTTON).click()  # Зарегистрироваться
        incorrect_password = driver.find_element(By.XPATH, "./html/body/div/div/main/div/form/fieldset[3]/div/p").text
        assert incorrect_password == 'Некорректный пароль'