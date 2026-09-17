# 김하늘 | QA Automation Portfolio

> 품질을 검증하는 것을 넘어, 반복 가능한 검증 체계를 만드는 QA Engineer

실무에서 경험한 **API / CLI / UI 자동화 구조와 문제 해결 방식**을 개인 환경에서 재구성한 포트폴리오입니다.

## Security Notice

- 실제 회사 소스 코드, 사내 URL/IP, MID/TID, 인증정보, 테스트 계정은 포함하지 않습니다.
- 실제 결제 전문과 사내 실행 파일 대신 **Mock CLI / Local Demo / Sample API**를 사용합니다.
- 변수명·명령명·데이터 형식은 포트폴리오 목적에 맞게 일반화했습니다.
- 암호화 예제의 KEY/IV는 샘플 값이며 실제 업무 정보와 무관합니다.

## Projects

### 01. `mobile-payment-engine`
YAML 기반 시나리오 → CLI 프로세스 실행 → stdout 파싱 → 변수 추출 → 후속 전문 연결 → Assertion → JSON/HTML 리포트 생성

### 02. `playwright-payment-ui`
표준/커스텀 결제창을 가정한 Local Demo와 Playwright 테스트.  
통신사 선택, iframe, PASS/SMS 분기, OTP timer, hidden input, 동적 활성화 등 결제 UI에서 자주 발생하는 요소를 재현합니다.

### 03. `api-automation`
Postman/Newman 스타일의 API Assertion을 Node.js 형태로 재구성했습니다.  
필수값, 배열 허용값, createdAt 허용범위, HTTP/빈 응답 오류, AES-CBC 샘플 등을 포함합니다.

## Structure

```text
qa-automation-portfolio-v2/
├─ mobile-payment-engine/
├─ playwright-payment-ui/
└─ api-automation/
```

각 프로젝트는 독립적으로 실행 가능합니다.
