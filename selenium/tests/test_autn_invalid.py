import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from base import TestBase


class TestLoginForm(TestBase):
    def test_invalid_login(self):
        # Ввод неверного email
        email_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        email_field.send_keys("invalid@email.com")

        # Ввод неверного пароля
        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys("wrongPassword")

        # Клик по кнопке входа
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()

        # Проверка сообщения об ошибке
        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'error-message')]"))
        )
        assert "Неверный логин или пароль" in error_message.text