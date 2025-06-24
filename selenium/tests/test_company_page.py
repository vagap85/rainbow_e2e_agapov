from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base import TestBase

class TestCompanyPage(TestBase):
    def test_company_page_access(self):
        # Авторизация
        email_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        email_field.send_keys("dumbledore@sct.team")
        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys("12345678qQ1")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

        # Ожидание загрузки главной страницы
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("dashboard")
        )

        # Переход на страницу компании (предполагаем, что есть ссылка в меню)
        company_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, 'company')]"))
        )
        company_link.click()

        # Проверка загрузки страницы компании
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("company")
        )
        assert "Компания" in self.driver.title