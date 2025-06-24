test('Доступность страницы Компания после авторизации', async ({ page }) => {
  // Авторизация
  await page.goto('https://dev2.getinfo.radugi.net');
  await page.fill('input[name="email"]', 'dumbledore@sct.team');
  await page.fill('input[name="password"]', '12345678qQ1');
  await page.click('button[type="submit"]');
  
  // Переход на страницу компании
  await page.click('a[href*="company"]');
  await expect(page).toHaveURL(/company/);
  await expect(page.locator('.company-page')).toBeVisible();
});
