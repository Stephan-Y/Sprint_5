from locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_sign_in_to_account import TestSignIn


class TestAccountsButtons(Locators):

    def test_transfer_to_bread_section(self, driver):
        driver.find_element(*self.PERSONAL_ACCOUNT_BUTTON).click()  # кнопка "Личный кабинет"
        TestSignIn().input_user_data(driver)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((self.TRANSFER_SAUCES_SECTION)))
        driver.find_element(*self.TRANSFER_SAUCES_SECTION).click()  # кнопка "Соусы"
        driver.find_element(*self.TRANSFER_BREAD_SECTION).click()  # кнопка "Булки"
        bread_section = driver.find_element(*self.TRANSFER_BREAD_SECTION).__class__
        current_section = driver.find_element(*self.CONSTRUCTOR_CURRENT_SECTION).__class__
        assert bread_section == current_section

    def test_transfer_to_sauce_section(self, driver):
        driver.find_element(*self.PERSONAL_ACCOUNT_BUTTON).click()  # кнопка "Личный кабинет"
        TestSignIn().input_user_data(driver)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((self.TRANSFER_SAUCES_SECTION)))
        driver.find_element(*self.TRANSFER_SAUCES_SECTION).click()  # кнопка "Соусы"
        sauce_section = driver.find_element(*self.TRANSFER_SAUCES_SECTION).__class__
        current_section = driver.find_element(*self.CONSTRUCTOR_CURRENT_SECTION).__class__
        assert sauce_section == current_section

    def test_transfer_to_fillings_section(self, driver):
        driver.find_element(*self.PERSONAL_ACCOUNT_BUTTON).click()  # кнопка "Личный кабинет"
        TestSignIn().input_user_data(driver)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((self.TRANSFER_FILLINGS_SECTION)))
        driver.find_element(*self.TRANSFER_FILLINGS_SECTION).click()  # кнопка "Соусы"
        fillings_section = driver.find_element(*self.TRANSFER_FILLINGS_SECTION).__class__
        current_section = driver.find_element(*self.CONSTRUCTOR_CURRENT_SECTION).__class__
        assert fillings_section == current_section