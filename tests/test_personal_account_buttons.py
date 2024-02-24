from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_sign_in_to_account import TestSignIn


class TestAccountsButtons(Locators):
    def test_personal_account_page(self, driver):
        driver.find_element(*self.PERSONAL_ACCOUNT_BUTTON).click()  # кнопка "Личный кабинет"
        TestSignIn().input_user_data(driver)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((self.PERSONAL_ACCOUNT_BUTTON)))
        driver.find_element(*self.PERSONAL_ACCOUNT_BUTTON).click()  # кнопка "Личный кабинет"
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((self.SAVE_BUTTON_ON_PERSONAL_PAGE)))
        assert driver.find_element(*self.SAVE_BUTTON_ON_PERSONAL_PAGE).text == 'Сохранить'

    def test_constructor_buttton_on_personal_account_page(self, driver):
        driver.find_element(*self.PERSONAL_ACCOUNT_BUTTON).click()  # кнопка "Личный кабинет"
        TestSignIn().input_user_data(driver)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((self.PERSONAL_ACCOUNT_BUTTON)))
        driver.find_element(*self.PERSONAL_ACCOUNT_BUTTON).click()  # кнопка "Личный кабинет"
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((self.SAVE_BUTTON_ON_PERSONAL_PAGE)))
        driver.find_element(*self.CONSTRUCTOR_BUTTON).click()  # кнопка "Конструктор"
        assert driver.find_element(*self.PERSONAL_ACCOUNT_BUTTON).text == 'Личный Кабинет'

    def test_logotip_on_personal_account_page(self, driver):
        driver.find_element(*self.PERSONAL_ACCOUNT_BUTTON).click()  # кнопка "Личный кабинет"
        TestSignIn().input_user_data(driver)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((self.PERSONAL_ACCOUNT_BUTTON)))
        driver.find_element(*self.PERSONAL_ACCOUNT_BUTTON).click()  # кнопка "Личный кабинет"
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((self.SAVE_BUTTON_ON_PERSONAL_PAGE)))
        driver.find_element(*self.LOGO_BURGERS).click()  # Логотип в хедере
        assert driver.find_element(*self.PERSONAL_ACCOUNT_BUTTON).text == 'Личный Кабинет'

    def test_log_out_from_personal_account_page(self, driver):
        driver.find_element(*self.PERSONAL_ACCOUNT_BUTTON).click()  # кнопка "Личный кабинет"
        TestSignIn().input_user_data(driver)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((self.PERSONAL_ACCOUNT_BUTTON)))
        driver.find_element(*self.PERSONAL_ACCOUNT_BUTTON).click()  # кнопка "Личный кабинет"
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((self.SAVE_BUTTON_ON_PERSONAL_PAGE)))
        driver.find_element(*self.LOG_OUT_BUTTON).click()  # кнопка "Выход"
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((self.ENTER_BUTTON)))
        assert driver.find_element(*self.ENTER_BUTTON).text == 'Войти'