// @ts-check
const { defineConfig, devices } = require('@playwright/test');
require('dotenv').config();

/**
 * Основная конфигурация Playwright.
 * Документация: https://playwright.dev/docs/test-configuration
 */
module.exports = defineConfig({
  // Базовый URL тестируемого приложения
  timeout: 60000,
  
  // Глобальные таймауты
  timeout: 30000,
  expect: {
    timeout: 5000
  },

  // Полный путь к директории с тестами
  testDir: './tests',

  /* Запускать тесты в файлах параллельно */
  fullyParallel: true,

  /* Запускать тесты в CI параллельно */
  workers: process.env.CI ? 2 : 3,

  /* Репортеры для генерации отчетов */
  reporter: [
    ['list'],
    ['html', { 
      outputFolder: 'playwright-report',
      open: process.env.CI ? 'never' : 'on-failure'
    }],
    ['junit', { outputFile: 'test-results/results.xml' }]
  ],

  /* Общие настройки для всех проектов */
  use: {
    // Базовый URL берется из .env или используется значение по умолчанию
    baseURL: process.env.BASE_URL || 'https://dev2.getinfo.radugi.net',

    // Настройки трассировки
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',

    // Дополнительные HTTP-заголовки
    extraHTTPHeaders: {
      'Accept': 'application/json',
    },

    // Настройки viewport
    viewport: { width: 1920, height: 1080 },
  },

  /* Конфигурация проектов для разных браузеров */
  projects: [
    {
      name: 'chromium',
      use: { 
        ...devices['Desktop Chrome'],
        // Можно переопределить user-agent
        // userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
      },
    },

    {
      name: 'firefox',
      use: { ...devices['Desktop Firefox'] },
    },

    {
      name: 'webkit',
      use: { ...devices['Desktop Safari'] },
    },

    /* Конфигурация для мобильных тестов */
    {
      name: 'Mobile Chrome',
      use: { ...devices['Pixel 5'] },
    },
    {
      name: 'Mobile Safari',
      use: { ...devices['iPhone 12'] },
    },
  ],

  /* Настройки веб-сервера для локального тестирования */
  // webServer: {
  //   command: 'npm run start',
  //   url: 'http://localhost:3000',
  //   reuseExistingServer: !process.env.CI,
  //   timeout: 120 * 1000,
  // },
});
