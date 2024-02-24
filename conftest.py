import pytest
import random
from selenium import webdriver

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.set_window_size(1920, 1080)
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()

@pytest.fixture()
def login():
    yield f'stepan_yakovlev_5_{random.randrange(100,999,1)}@ya.py'

@pytest.fixture() # Это не доп задание, для упрощения
def correct_password():
    yield random.randrange(111111,999999999,1)

@pytest.fixture()
def incorrect_password():
    yield random.randrange(1,9999,1)

