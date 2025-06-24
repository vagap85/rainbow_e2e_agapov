import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

from base import TestBase


class TestPasswordRecovery(TestBase):
    def test_password_recovery_link(self):
        """Тест восстановления пароля: проверка ссылки и перехода на страницу восстановления"""
        try:
            # 1. Проверка видимости и кликабельности ссылки
            recovery_link = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Забыли пароль?")))

            assert recovery_link.is_displayed(), "Ссылка 'Забыли пароль?' не отображается"

            # Сохраняем текущий URL для проверки после перехода
            current_url = self.driver.current_url

            # 2. Клик по ссылке
            recovery_link.click()

            # 3. Ожидание изменения URL
            WebDriverWait(self.driver, 15).until(
                lambda driver: driver.current_url != current_url)

            # 4. Проверка нового URL
            WebDriverWait(self.driver, 15).until(
                EC.url_contains("forgot-password"))

            # 5. Проверка заголовка страницы
            assert "Восстановление пароля" in self.driver.title, \
                f"Заголовок страницы не содержит 'Восстановление пароля'. Фактический заголовок: {self.driver.title}"

        except TimeoutException as e:
            pytest.fail(f"Время ожидания истекло: {str(e)}")
        except NoSuchElementException as e:
            pytest.fail(f"Элемент не найден: {str(e)}")
        except Exception as e:
            pytest.fail(f"Неожиданная ошибка: {str(e)}")