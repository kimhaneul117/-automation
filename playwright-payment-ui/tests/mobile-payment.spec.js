import { test, expect } from '@playwright/test';
import { MobilePaymentPage } from '../pages/MobilePaymentPage.js';

test.describe('휴대폰결제 표준 UI', () => {
  test('PASS 인증 UI 노출 확인', async ({ page }) => {
    const payment = new MobilePaymentPage(page);

    await payment.goto({ mode: 'pass' });
    await payment.agreeTerms();
    await payment.selectCarrier('SKT');

    await payment.enterUserInfo({
      phone: '01000000000',
      birthFront: '900101',
      birthBack: '1'
    });

    await payment.requestAuthentication();
    await payment.expectPassMode();
  });

  test('PASS → SMS 전환 후 결제 완료', async ({ page }) => {
    const payment = new MobilePaymentPage(page);

    await payment.goto({ mode: 'pass' });
    await payment.agreeTerms();
    await payment.selectCarrier('KT');

    await payment.enterUserInfo({
      phone: '01000000000',
      birthFront: '900101',
      birthBack: '2'
    });

    await payment.requestAuthentication();
    await payment.switchToSmsIfNeeded();

    await payment.enterOtp('123456');
    await payment.expectPayEnabled();
    await payment.pay();
  });

  test('SMS 인증 직접 진입', async ({ page }) => {
    const payment = new MobilePaymentPage(page);

    await payment.goto({ mode: 'sms' });
    await payment.agreeTerms();
    await payment.selectCarrier('LGU');

    await payment.enterUserInfo({
      phone: '01000000000',
      birthFront: '900101',
      birthBack: '1'
    });

    await payment.requestAuthentication();
    await payment.expectSmsMode();

    await expect(payment.payButton).toBeDisabled();

    await payment.enterOtp('123456');
    await payment.expectPayEnabled();
  });
});
