from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from data import *
class TestRegistration(Locators):
    def test_correct_registration(self, driver, login, correct_password):
        driver.find_element(*self.personal_account_button).click()  # клик на Личный кабинет
        driver.find_element(*self.registration_button).click()  # Зарегистрироваться
        driver.find_element(*self.registration_field_name).send_keys(user_name)  # Имя
        driver.find_element(*self.registration_field_email).send_keys(login)  # Почта
        driver.find_element(*self.registration_field_password).send_keys(correct_password)  # Пароль
        driver.find_element(*self.final_registration_button).click()  # Зарегистрироваться
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((self.enter_button)))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login', 'URL не совпадает'
        driver.quit()


    def test_incorrect_registration(self, driver, login, incorrect_password):
        driver.find_element(* self.personal_account_button).click()  # клик на Личный кабинет
        driver.find_element(*self.registration_button).click()  # Зарегистрироваться
        driver.find_element(*self.registration_field_name).send_keys(user_name)  # Имя
        driver.find_element(*self.registration_field_email).send_keys(login)  # Почта
        driver.find_element(*self.registration_field_password).send_keys(incorrect_password)  # Некорректный ароль
        driver.find_element(*self.final_registration_button).click()  # Зарегистрироваться
        incorrect_password = driver.find_element(By.XPATH, "./html/body/div/div/main/div/form/fieldset[3]/div/p").text
        assert incorrect_password == 'Некорректный пароль'
        driver.quit()