# Автоматизированное тестирование с Selenium WebDriver,<br> 
для тестового задания от "Студия Цифровых Технологий Радуга"

## Требования
- Python 3.8+
- pip 20+
- Браузеры:
  - Chrome (последняя версия)
  - Firefox (опционально)
- ChromeDriver (устанавливается автоматически через webdriver-manager)

## Установка
1. *Клонировать репозиторий*:
   ```bash
   git clone https://github.com/ваш-username/ваш-репозиторий.git
   cd ваш-репозиторий
2. Создать и активировать виртуальное окружение:
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows
3. Установить зависимости: pip install -r requirements.txt
4. Запуск тестов: 
Все тесты- pytest -v
Конкретный тест- pytest tests/test_auth.py -v

## Основные настройки в .env

## Описание файлов:
- base.py - Базовый класс страницы
- conftest.py - Фикстуры pytest
- requirements.py - Зависимости
- 
