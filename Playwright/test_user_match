test('Совпадение авторизованного пользователя с руководителем компании', async ({ page }) => {
  // Авторизация
  await page.goto('https://dev2.getinfo.radugi.net');
  await page.fill('input[name="email"]', 'dumbledore@sct.team');
  await page.fill('input[name="password"]', '12345678qQ1');
  await page.click('button[type="submit"]');
  
  // Переход на страницу компании
  await page.click('a[href*="company"]');
  
  // Получение данных пользователя и руководителя
  const currentUser = await page.locator('.user-profile .email').innerText();
  const companyHead = await page.locator('.company-head .email').innerText();
  
  // Проверка соответствия
  expect(currentUser).toEqual(companyHead);
});
