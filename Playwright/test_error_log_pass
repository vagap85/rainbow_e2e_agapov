test('Неудачная авторизация с неверными данными', async ({ page }) => {
  await page.goto('https://dev2.getinfo.radugi.net');
  
  // Ввод неверного логина
  await page.fill('input[name="email"]', 'wrong@email.com');
  await page.fill('input[name="password"]', 'wrongPassword');
  await page.click('button[type="submit"]');
  
  // Проверка сообщения об ошибке
  await expect(page.locator('.error-message')).toContainText('Неверный логин или пароль');
});
