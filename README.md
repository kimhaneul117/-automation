# 김하늘 | QA Engineer

> **품질을 검증하는 것을 넘어, 검증 체계를 만드는 QA Engineer**

안녕하세요.
Web · Mobile · API 환경의 QA 경험을 기반으로, 현재는 **결제 및 본인확인 서비스의 API / CLI / UI 테스트 자동화**를 수행하고 있습니다.

단순히 테스트를 반복 수행하는 것보다 서비스의 흐름과 데이터 구조를 이해하고, 반복되는 검증을 **재사용 가능하고 유지보수할 수 있는 자동화 구조로 개선하는 것**에 집중하고 있습니다.

---

## About Me

* Web · Mobile · API 기능 및 자동화 테스트
* 결제 · 본인확인 서비스 QA
* API Request / Response 및 데이터 정합성 검증
* CLI 기반 테스트 자동화 엔진 설계 및 구현
* Playwright 기반 Web UI 자동화
* 테스트 데이터 기반 시나리오 설계
* 반복 검증 업무의 자동화 및 테스트 프로세스 개선

### Working Principle

> **“반복되는 검증은 자동화하고, 품질은 체계로 관리합니다.”**

테스트 수행 자체에 그치지 않고 반복되는 업무를 자동화하고, 테스트 과정에서 발견한 문제의 원인과 패턴을 분석하여 **더 효율적이고 안정적인 검증 방법을 만드는 것**을 지향합니다.

---

# Automation Portfolio

이 저장소는 실무에서 경험한 테스트 자동화 방식과 구조를 **개인 환경에서 재구성한 Portfolio Sample**입니다.

실제 업무 소스 코드를 공개하는 것이 아니라, 제가 자동화 테스트를 어떤 방식으로 설계하고 구현하는지 보여주는 것을 목적으로 합니다.

> ### Security Notice
>
> 실제 회사 소스 코드, 사내 URL/IP, 인증정보, 테스트 계정, 거래정보 및 내부 시스템 정보는 포함하지 않습니다.
>
> 실제 사내 CLI 및 서비스 대신 **Mock CLI / Local Demo / Sample Data**를 사용하며, 명령어·변수·데이터 구조 역시 포트폴리오 목적으로 일반화했습니다.

---

# 01. Mobile Payment Scenario Engine

### YAML + Node.js 기반 CLI 테스트 자동화 엔진

반복적인 CLI 테스트를 효율적으로 수행하기 위해 **YAML 기반 Scenario Engine 구조**를 구현한 예제입니다.

테스트 데이터와 실행 로직을 분리하고, 이전 단계에서 반환된 데이터를 다음 단계에 전달하여 **여러 단계로 이루어진 거래 시나리오를 하나의 Flow로 자동 검증**하도록 구성했습니다.

### Architecture

```text
YAML Scenario
      │
      ▼
Scenario Loader
      │
      ▼
Variable / Context Manager
      │
      ▼
Scenario Engine
      │
      ▼
CLI Process Runner
      │
      ▼
Response Parser
      │
      ▼
Assertion Engine
      │
      ▼
JSON / HTML Report
```

### 주요 구현 내용

* YAML 기반 테스트 시나리오 및 테스트 데이터 관리
* Node.js 기반 Scenario Engine
* `child_process.spawn()` 기반 CLI 프로세스 실행
* CLI stdout `KEY=VALUE` 응답 파싱
* Step 간 Context 및 Transaction ID 전달
* `${VARIABLE}` 형태의 동적 데이터 치환
* 정상 / 오류 시나리오 분리
* 응답값 Assertion 모듈화
* JSON / HTML 테스트 결과 리포트 생성

### Assertion

다양한 응답 패턴을 검증할 수 있도록 공통 Assertion을 구성했습니다.

```text
required
equals
oneOf
regex
time tolerance
```

예를 들어 거래 식별자는 존재 여부와 형식을 함께 검증하고, 응답 시간값은 테스트 시작 시간을 기준으로 허용 범위 내에 존재하는지 검증합니다.

### Scenario Example

```yaml
name: MOBILE_PAYMENT_AND_CANCEL

variables:
  AMOUNT: "1000"
  CARRIER: "SAMPLE"

steps:
  - name: 결제 요청
    command: ITEM_SEND
    params:
      amount: "${AMOUNT}"
      carrier: "${CARRIER}"

    expect:
      RESULT:
        equals: "SUCCESS"

      TID:
        required: true
        regex: "^T[0-9]{14}[A-Z0-9]{4}$"

      DATE:
        isoTimeWithinSeconds: 5

    extract:
      PAYMENT_TID: "TID"

  - name: 결제 승인
    command: DELIVERY
    params:
      tid: "${PAYMENT_TID}"

    expect:
      RESULT:
        equals: "SUCCESS"

  - name: 결제 취소
    command: CANCEL
    params:
      tid: "${PAYMENT_TID}"

    expect:
      RESULT:
        equals: "SUCCESS"
```

실제 사내 실행 프로그램 대신 Mock CLI를 별도 프로세스로 실행하여 포트폴리오 환경에서도 전체 자동화 Flow를 확인할 수 있도록 구성했습니다.

📂 **Source**

[`mobile-payment-engine/`](./mobile-payment-engine/)

---

# 02. Playwright Payment UI Automation

### Playwright 기반 휴대폰결제 UI 테스트 자동화

표준 및 다양한 형태의 결제 UI를 자동화했던 경험을 바탕으로, **가상의 휴대폰결제 페이지를 직접 구성하여 Playwright 테스트를 재현한 프로젝트**입니다.

실제 서비스 페이지 및 가맹점 정보는 사용하지 않고 Local Demo 환경에서 UI 동작을 재현했습니다.

### Test Flow

```text
결제창 진입
   ↓
약관 동의
   ↓
통신사 선택
   ↓
사용자 정보 입력
   ↓
PASS / SMS 인증
   ↓
OTP 검증
   ↓
결제 버튼 활성화
   ↓
결제 결과 검증
```

### 주요 구현 내용

* Playwright 기반 Web UI 자동화
* Page Object Pattern 적용
* iframe 내부 약관 요소 제어
* `selectOption()` 기반 Select UI 처리
* 입력 완료 후 자동 Focus 이동 검증
* Keyboard 입력 방식 처리
* PASS / SMS 인증 방식별 UI 분기
* PASS → SMS 인증 전환 처리
* OTP Timer `mm:ss` 형식 검증
* `pressSequentially()` 기반 인증번호 입력
* 결제 버튼 `disabled → enabled` 상태 검증
* 동적 Class 변경 검증
* 실패 시 Screenshot / Trace 보존

### Example

```javascript
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
```

Local Demo 페이지가 포함되어 있어 실제 외부 서비스에 접근하지 않고 테스트를 실행할 수 있습니다.

📂 **Source**

[`playwright-payment-ui/`](./playwright-payment-ui/)

---

# 03. API Test Automation

### JavaScript 기반 API Response Validation

API 테스트에서 반복적으로 사용되는 검증 로직을 공통 모듈로 구성한 예제입니다.

단순 HTTP Status 검증을 넘어 응답 데이터의 **필수값, 배열 구조, 허용값, 시간 정합성 및 네트워크 오류 상황**까지 검증하도록 구성했습니다.

### 주요 구현 내용

* HTTP Status 검증
* Empty Response 검증
* Response Code / Message 검증
* 필수 필드 존재 여부 검증
* Array 구조 및 허용값 검증
* 요청 시각 대비 응답 시간값 허용범위 검증
* 일시적인 네트워크 오류 Retry 처리
* AES-128-CBC 암·복호화 Sample
* Postman / Newman Assertion Sample

### Response Validation Example

```javascript
assertHttpSuccess(response);

assertSuccessResponse(body);

assertRequired(body, [
  'transactionId',
  'createdAt'
]);

assertArrayContainsAllowedCodes(
  body.authenticates,
  ['PASS', 'SMS', 'QR']
);

assertTimeWithin({
  actual: body.createdAt,
  base: BASE_NOW,
  toleranceSeconds: 60,
  fieldName: 'createdAt'
});
```

### Network Error Handling

일시적인 Connection Reset, Timeout 및 응답을 받지 못한 상황을 구분하여 재시도할 수 있도록 Retry 구조를 분리했습니다.

```javascript
error.code === 'ECONNRESET'
error.code === 'ETIMEDOUT'
error.status === 0
```

📂 **Source**

[`api-automation/`](./api-automation/)

---

# Previous Automation Experience

현재 프로젝트 이전에도 Web · Mobile · API 환경에서 다양한 테스트 자동화를 수행했습니다.

### UI Automation

* PC Web / Android / iOS UI 자동화
* Selenium / Appium 기반 테스트
* 반복 Regression Test 자동화
* UI 테스트 구조 개선 및 유지보수

### API Automation

* 주문 / 클레임 API 자동화
* Postman 기반 API 테스트
* STG / PRD 환경별 API 검증
* 반복 API 시나리오 자동 실행

### Performance Test

* JMeter / nGrinder 기반 성능 테스트
* API 부하 테스트
* 응답시간 및 성능 결과 분석

### CI/CD

* GitLab CI/CD 기반 자동화 테스트 실행
* Jenkins 기반 테스트 실행
* 테스트 결과 및 이슈 관리 프로세스 개선

---

# Tech Stack

### Test Automation

![Playwright](https://img.shields.io/badge/Playwright-Test_Automation-45ba4b)
![Selenium](https://img.shields.io/badge/Selenium-Web_Automation-43B02A)
![Appium](https://img.shields.io/badge/Appium-Mobile_Automation-662D91)

### API

![Postman](https://img.shields.io/badge/Postman-API_Testing-FF6C37)
![Newman](https://img.shields.io/badge/Newman-Collection_Runner-FF6C37)

### Language & Runtime

![JavaScript](https://img.shields.io/badge/JavaScript-Automation-F7DF1E)
![Node.js](https://img.shields.io/badge/Node.js-Runtime-339933)
![Python](https://img.shields.io/badge/Python-Automation-3776AB)

### Test Data & Security

`JSON` · `YAML` · `AES-CBC` · `SEED` · `URL Encoding` · `EUC-KR`

### Performance

`JMeter` · `nGrinder`

### CI/CD & Collaboration

`GitLab CI/CD` · `Jenkins` · `Jira` · `Confluence`

### Tools

`VSCode` · `SecureCRT` · `Oracle SQL Developer`

---

# Certification

**AWS Certified Solutions Architect – Associate (SAA-C03)**

---

# Contact

**Email**
[hnkim117@gmail.com](mailto:hnkim117@gmail.com)

**GitHub**
kimhaneul117

---

> **반복되는 검증은 자동화하고, 품질은 체계로 관리합니다.**
