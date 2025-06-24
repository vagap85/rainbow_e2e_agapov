import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class TestBase:
    @pytest.fixture(autouse=True)
    def setup(self, driver, base_url):
        """Фикстура для инициализации тестов"""
        self.driver = driver
        self.base_url = base_url
        self.driver.get(self.base_url)