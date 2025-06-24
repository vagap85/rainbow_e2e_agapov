import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture(scope="function")
def driver():
    # Настройка опций Chrome
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--start-maximized")  # Максимизировать окно
    chrome_options.add_argument("--disable-extensions")  # Отключить расширения
    chrome_options.add_argument("--disable-notifications")  # Отключить уведомления
    chrome_options.add_argument("--lang=ru")  # Установить язык браузера

    # Инициализация драйвера с автоматической установкой через webdriver-manager
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=chrome_options
    )

    # Установка неявного ожидания
    driver.implicitly_wait(10)

    yield driver  # Возвращаем драйвер тестовой функции

    # Закрытие браузера после теста
    driver.quit()


@pytest.fixture(scope="session")
def base_url():
    return "https://dev2.getinfo.radugi.net"