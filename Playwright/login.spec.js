test('Успешная авторизация', async ({ page }) => {
  await page.goto('https://dev2.getinfo.radugi.net');
  
  // Ввод корректных данных
  await page.fill('input[name="email"]', 'dumbledore@sct.team');
  await page.fill('input[name="password"]', '12345678qQ1');
  await page.click('button[type="submit"]');
  
  // Проверка перехода после авторизации
  await expect(page).toHaveURL(/dashboard/); // или другой ожидаемый URL
  await expect(page.locator('.user-profile')).toBeVisible();
});
