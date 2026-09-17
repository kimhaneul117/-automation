# Playwright Payment UI Automation

실제 결제창 대신 로컬 Demo 페이지를 사용해 **휴대폰결제 UI 자동화에서 자주 만나는 요소**를 재현한 포트폴리오 예제입니다.

## 구현 내용

- `selectOption()` 기반 통신사 선택
- iframe 내부 약관 체크
- 주민번호 앞자리 입력 후 뒤 1자리 input으로 자동 focus 이동
- hidden/동적 요소 처리
- PASS 인증과 SMS fallback 분기
- OTP timer의 `mm:ss` 형식 검증
- 인증번호 입력 완료 시 결제 버튼 활성화 검증
- Page Object 기반 표준/커스텀 UI 확장 구조
- 실패 시 trace 보존

## Run

터미널 1:
```bash
npm install
npm run demo
```

터미널 2:
```bash
npm test
```

Demo는 `http://127.0.0.1:4173`에서 실행됩니다.
