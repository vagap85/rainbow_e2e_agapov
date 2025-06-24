from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base import TestBase

class TestUserMatch(TestBase):
    def test_user_company_head_match(self):
        # Авторизация
        email_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        email_field.send_keys("dumbledore@sct.team")
        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys("12345678qQ1")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

        # Переход на страницу компании
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'company')]"))
        ).click()

        # Получение email текущего пользователя (предполагаем, что отображается в профиле)
        user_email = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='user-profile']//span[@class='email']"))
        ).text

        # Получение email руководителя компании
        company_head_email = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='company-head']//span[@class='email']"))
        ).text

        # Проверка соответствия
        assert user_email == company_head_email