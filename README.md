# 김하늘 | QA Automation Portfolio

> **품질을 검증하는 것을 넘어, 반복 가능한 검증 체계를 만드는 QA Engineer**

실무에서 수행한 **API / CLI / UI 테스트 자동화 경험**을 바탕으로,
자동화 구조와 핵심 검증 로직을 개인 환경에서 재구성한 QA Automation Portfolio입니다.

단순 테스트 스크립트 작성보다 **시나리오 설계 → 실행 → 데이터 검증 → 예외 처리 → 결과 확인**까지 이어지는 자동화 구조를 만드는 데 초점을 두었습니다.

---

## About

QA 업무를 수행하며 API, CLI, Web/Mobile UI 등 다양한 영역의 테스트 자동화를 경험했습니다.

현재는 결제·인증 서비스 QA를 중심으로 **API 자동화, CLI 기반 결제 시나리오 자동화, Playwright UI 자동화**를 구축·운영하고 있으며, 이전에는 커머스 환경에서 API 및 Selenium/Appium 기반 UI 자동화를 수행했습니다.

### Tech Stack

* **API** — Postman, Newman, JavaScript, Node.js
* **UI** — Playwright, Selenium, Appium
* **CLI** — Node.js, YAML, Process Execution
* **CI / Report** — Jenkins, GitLab CI, Newman Report
* **Analysis** — Oracle SQL Developer, SecureCRT, Log Analysis

---

## Security Notice

본 Repository는 실무 경험을 기반으로 구성했지만, 공개 가능한 형태로 재구성한 포트폴리오입니다.

* 실제 회사의 소스 코드 및 내부 시스템 정보는 포함하지 않습니다.
* 사내 URL/IP, MID/TID, 계정·비밀번호 및 인증정보는 사용하지 않습니다.
* 실제 결제 전문 및 사내 실행 파일은 **Mock CLI / Local Demo / Sample Data**로 대체했습니다.
* 서비스명, 변수명, 명령명 및 데이터 구조는 포트폴리오 목적에 맞게 일반화했습니다.
* 암호화 KEY/IV 등 보안 관련 값은 실제 업무와 무관한 샘플 데이터를 사용합니다.

---

## Projects

### 01. `mobile-payment-engine`

**CLI 기반 결제 시나리오 자동화**

YAML로 정의한 테스트 시나리오를 Node.js 엔진에서 순차적으로 실행하고, CLI 응답을 파싱하여 단계별 데이터 정합성을 검증하는 구조입니다.

```text
YAML Scenario
    ↓
CLI Process Execution
    ↓
stdout Parsing
    ↓
Variable Extraction
    ↓
Next Transaction
    ↓
Assertion
    ↓
Test Result
```

**Key Points**

* YAML 기반 테스트 시나리오 관리
* CLI 프로세스 자동 실행
* stdout 응답 파싱
* 이전 단계 응답값을 후속 요청에 자동 전달
* 정상/예외 시나리오 분리
* 응답 필드 및 거래 데이터 정합성 검증
* Mock Payment CLI를 통한 독립 실행 환경 구성

---

### 02. `playwright-payment-ui`

**Playwright 기반 결제 UI 자동화**

실제 결제창 QA 경험을 기반으로 표준/커스텀 결제 UI에서 발생하는 주요 동작을 Local Demo 환경으로 재구성했습니다.

**Key Points**

* 결제수단 및 통신사 선택
* iframe 내부 요소 제어
* 약관 동의 및 활성화 상태 검증
* PASS / SMS 인증 방식 분기
* OTP Timer 검증
* Hidden Input 및 동적 DOM 처리
* Playwright Locator 기반 안정적인 요소 탐색
* Local Demo Server를 이용한 독립 실행 환경 구성

---

### 03. `api-automation`

**JavaScript 기반 API 공통 검증 모듈**

Postman/Newman 기반 API 자동화 경험에서 반복적으로 사용했던 검증 패턴을 Node.js 환경에서 재구성했습니다.

**Key Points**

* HTTP Status 및 응답 Body 검증
* 필수 필드 존재 여부 검증
* 허용값 및 배열 데이터 검증
* 날짜/시간 허용 오차 검증
* HTTP 오류 및 Empty Response 처리
* Retry / Polling 구조
* AES-CBC 암·복호화 Sample
* 공통 Assertion 모듈화

---

### 04. `legacy-apmall`

**Commerce API / UI Automation Archive**

이전 커머스 QA 업무에서 수행했던 API 및 UI 자동화 경험을 정리한 Archive입니다.

**API Automation**

* 상품/전시/주문 영역 API 검증
* Postman 기반 Response Assertion
* 주문 단계별 데이터 및 상태값 검증
* GitLab CI 기반 자동화 운영 경험

**UI Automation**

* Android App UI 자동화
* PC Web UI 자동화
* Selenium / Appium 기반 테스트
* 메인, 마이페이지, 주문/결제 등 주요 사용자 흐름 검증

> Legacy 프로젝트는 이전 자동화 경험을 보여주기 위한 참고 자료이며, 현재 포트폴리오의 주요 구현 프로젝트는 `mobile-payment-engine`, `playwright-payment-ui`, `api-automation`입니다.

---

## Repository Structure

```text
qa-automation-portfolio/
│
├── mobile-payment-engine/
│   ├── scenarios/
│   ├── src/
│   └── mock/
│
├── playwright-payment-ui/
│   ├── tests/
│   ├── pages/
│   └── demo/
│
├── api-automation/
│   ├── src/
│   ├── postman/
│   └── examples/
│
├── legacy-apmall/
│   ├── API/
│   └── UI/
│
├── .gitignore
└── README.md
```

각 프로젝트는 특정 회사의 내부 환경에 의존하지 않도록 구성했으며, 주요 자동화 프로젝트는 개인 환경에서 독립적으로 실행할 수 있도록 재구성했습니다.

---

## Automation Experience

실무에서 자동화 자체를 목표로 하기보다 **반복 검증이 필요한 영역을 식별하고 이를 재사용 가능한 테스트 구조로 전환하는 것**에 중점을 두고 있습니다.

API 검증에서 시작하여 CLI 기반 거래 흐름 자동화, Web UI 회귀 자동화까지 검증 범위를 확장했으며, 테스트 실행뿐 아니라 **응답 파싱, 데이터 연계, 예외 처리, 재시도 및 결과 확인까지 포함하는 자동화 구조**를 구축해 왔습니다.