test('Проверка ссылки восстановления пароля', async ({ page }) => {
  await page.goto('https://dev2.getinfo.radugi.net');
  
  // Проверка наличия ссылки
  const forgotPasswordLink = page.locator('a[href*="forgot-password"]');
  await expect(forgotPasswordLink).toBeVisible();
  
  // Проверка перехода по ссылке
  await forgotPasswordLink.click();
  await expect(page).toHaveURL(/forgot-password/);
  await expect(page.locator('h1')).toContainText('Восстановление пароля');
});
