import { expect } from '@playwright/test';

export class MobilePaymentPage {
  constructor(page) {
    this.page = page;

    this.carrier = page.getByLabel('통신사선택');
    this.phone = page.getByLabel('휴대폰번호');
    this.birthFront = page.getByLabel('주민번호 앞 6자리');
    this.birthBack = page.getByLabel('주민번호 뒤 1자리');

    this.requestAuthButton = page.getByRole('button', { name: '인증 요청' });
    this.authMode = page.locator('#auth-mode');
    this.passMessage = page.locator('#pass-message');
    this.smsArea = page.locator('#sms-area');
    this.otp = page.getByLabel('인증번호');
    this.timer = page.locator('#otp-timer');

    this.payButton = page.getByRole('button', { name: '결제하기' });
    this.result = page.locator('#payment-result');
  }

  async goto({ mode = 'pass' } = {}) {
    await this.page.goto(`/payment.html?mode=${mode}`);
  }

  async agreeTerms() {
    const frame = this.page.frameLocator('#terms-frame');
    await frame.getByLabel('전체 약관 동의').check();
    await expect(frame.getByLabel('전체 약관 동의')).toBeChecked();
  }

  async selectCarrier(carrier) {
    await this.carrier.selectOption(carrier);
    await expect(this.carrier).toHaveValue(carrier);
  }

  async enterUserInfo({ phone, birthFront, birthBack }) {
    await this.phone.fill(phone);

    await this.birthFront.fill(birthFront);
    await expect(this.birthBack).toBeFocused();

    // 실제 환경에서 자동 focus 이동 후 fill이 불안정할 수 있는 상황을
    // 재현하기 위해 focused element에 key 입력 방식 사용
    await this.page.keyboard.type(birthBack);

    await expect(this.birthBack).toHaveValue(birthBack);
  }

  async requestAuthentication() {
    await this.requestAuthButton.click();
  }

  async expectPassMode() {
    await expect(this.authMode).toHaveText('PASS');
    await expect(this.passMessage).toBeVisible();
    await expect(this.smsArea).toBeHidden();
  }

  async expectSmsMode() {
    await expect(this.authMode).toHaveText('SMS');
    await expect(this.smsArea).toBeVisible();
    await expect(this.timer).toHaveText(/^\d{2}:\d{2}$/);
  }

  async switchToSmsIfNeeded() {
    const mode = (await this.authMode.textContent())?.trim();

    if (mode === 'PASS') {
      await this.page.getByRole('button', { name: 'SMS 인증으로 전환' }).click();
    }

    await this.expectSmsMode();
  }

  async enterOtp(value) {
    await this.otp.pressSequentially(value, { delay: 30 });
    await expect(this.otp).toHaveValue(value);
  }

  async expectPayEnabled() {
    await expect(this.payButton).toBeEnabled();
    await expect(this.payButton).toHaveClass(/ready/);
  }

  async pay() {
    await this.payButton.click();
    await expect(this.result).toHaveText('결제가 완료되었습니다.');
  }
}
