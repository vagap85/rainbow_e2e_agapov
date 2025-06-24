from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin:
    def test_successful_login(self, driver):
        # Ввод корректного email
        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        email_field.send_keys("dumbledore@sct.team")

        # Ввод корректного пароля
        password_field = driver.find_element(By.NAME, "password")
        password_field.send_keys("12345678qQ1")

        # Клик по кнопке входа
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()

        # Проверка успешной авторизации
        WebDriverWait(driver, 10).until(
            EC.url_contains("dashboard")
        )
        assert "dumbledore" in driver.page_source