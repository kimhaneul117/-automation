# 김하늘 | QA Engineer

> **품질을 검증하는 것을 넘어, 검증 체계를 만드는 QA Engineer**

안녕하세요.
서비스의 품질을 검증하고, 반복적인 테스트를 **자동화된 검증 체계로 개선하는 QA Engineer 김하늘**입니다.

Web · Mobile · API 환경의 기능 및 자동화 테스트 경험을 기반으로 현재는 **결제·본인확인 서비스의 API / CLI / UI 자동화**를 수행하고 있습니다.

단순히 테스트 스크립트를 작성하는 것보다 서비스의 흐름과 데이터 구조를 이해하고, **반복 가능하고 유지보수할 수 있는 테스트 구조를 설계하는 것**을 중요하게 생각합니다.

---

## 1. About Me

* **QA / Test Automation Engineer**
* Web · Mobile · API 기능 및 자동화 테스트
* 결제 · 본인확인 서비스 QA 및 테스트 자동화
* API Request / Response 및 결제 전문 데이터 검증
* CLI 기반 테스트 자동화 엔진 설계 및 개발
* Playwright 기반 Web UI 자동화
* 반복 검증 업무의 자동화 및 테스트 프로세스 개선

### Working Principle

**“반복되는 검증은 자동화하고, 품질은 체계로 관리합니다.”**

주어진 테스트를 수행하는 것에 그치지 않고 반복되는 업무를 자동화하고, 테스트 과정에서 발견한 문제의 원인과 패턴을 분석하여 **더 효율적이고 안정적인 검증 방법을 만드는 것**을 지향합니다.

---

# 2. Projects

> ⚠️ **Security Notice**
>
> 업무 프로젝트의 실제 소스 코드, 테스트 데이터, 서버 및 내부 시스템 정보는 보안상 공개하지 않습니다.
> 본 저장소에는 개인적으로 재구성한 예제 코드와 자동화 구조를 중심으로 기술하며, 실제 서비스의 민감 정보 및 비즈니스 로직은 포함하지 않습니다.

---

## PROJECT 01. 본인확인 API 테스트 자동화

### Overview

본인확인 서비스의 반복적인 API 검증을 자동화하여 다양한 인증 방식과 통신사별 시나리오를 일관된 기준으로 검증할 수 있도록 테스트 환경을 구축했습니다.

### 주요 내용

* 일반 / 간편 / PASS 등 본인확인 인증 시나리오 검증
* SKT / KT / LGU+ / MVNO 통신사별 테스트
* Postman Collection 기반 API 테스트 자동화
* JavaScript Assertion을 활용한 Request / Response 검증
* 정상 / 오류 응답 및 필수 데이터 검증
* Newman을 활용한 Collection 자동 실행 및 결과 확인

### Tech

`Postman` `Newman` `JavaScript` `REST API` `JSON`

---

## PROJECT 02. 휴대폰결제 자동화 엔진 개발

### Overview

휴대폰결제 CLI 기반 테스트의 반복 작업을 개선하기 위해 **YAML 기반 시나리오 자동화 엔진**을 설계·개발했습니다.

테스트 시나리오 정의부터 CLI 실행, 암·복호화, 응답 파싱 및 검증까지 하나의 흐름으로 자동화하여 다양한 결제·취소 시나리오를 반복적으로 검증할 수 있도록 구성했습니다.

### Architecture

```text
YAML Scenario
      ↓
SClientScenarioEngine (Node.js)
      ↓
 ┌───────────────┐
 │               │
SClient.exe   dncrypto.exe
 │            SEED / AES
 └───────┬───────┘
         ↓
  결제 전문 자동 실행
         ↓
    응답 파싱 / 검증
         ↓
    테스트 결과 생성
```

### 주요 내용

* YAML 기반 테스트 시나리오 및 데이터 관리
* Node.js 기반 Scenario Engine 설계
* CLI 명령 자동 실행 및 stdout 데이터 파싱
* 결제 승인 / 취소 전문 시나리오 자동화
* SEED / AES 기반 데이터 암·복호화 처리
* Result / ErrMsg / TID / DATE / TRANTIME 등 주요 응답값 검증
* 기대값과 실제 응답 비교를 통한 Assertion 수행

### Tech

`Node.js` `JavaScript` `YAML` `CLI` `SEED` `AES`

---

## PROJECT 03. 휴대폰결제 UI 테스트 자동화

### Overview

휴대폰결제 표준 결제창과 다양한 가맹점 커스텀 결제창의 반복적인 회귀 테스트를 자동화하기 위해 **Playwright 기반 UI 테스트 환경**을 구축했습니다.

### 주요 내용

* 표준 휴대폰결제창 UI 자동화
* 다양한 가맹점 커스텀 결제창 시나리오 자동화
* PC / Mobile Web 결제 프로세스 검증
* 통신사 선택 → 사용자 정보 입력 → 인증 → 결제 흐름 자동화
* PASS / SMS 인증 방식별 UI 검증
* iframe / custom select / timer 등 동적 UI 요소 검증
* 결제창별 상이한 UI 구조 및 예외 시나리오 대응
* 공통 검증 로직을 통한 테스트 코드 유지보수성 개선

### Tech

`Playwright` `JavaScript` `Node.js` `VSCode`

---

## PROJECT 04. 결제 API 테스트 자동화

### Overview

통합결제 및 가상계좌 서비스의 API Request / Response 구조를 분석하고, 정상·오류 시나리오를 반복적으로 검증할 수 있는 자동화 테스트를 구축했습니다.

### 주요 내용

* 다양한 결제수단 API 시나리오 검증
* 정상 / 오류 Response 및 필수 필드 검증
* 결제수단별 응답 데이터 구조 검증
* 가상계좌 발급 / 취소 / 상태조회 등 API 자동화
* 계좌 점유 인증 및 거래 데이터 검증
* AES-CBC 기반 암·복호화 데이터 처리
* UTF-8 / EUC-KR 및 URL Encoding 데이터 검증
* 시간 및 거래 식별 데이터 정합성 검증

### Tech

`Postman` `Newman` `JavaScript` `REST API` `AES-CBC` `JSON`

---

# 3. Previous Automation Experience

이전 프로젝트에서는 이커머스 및 웹·모바일 서비스의 UI / API / 성능 테스트 자동화를 수행했습니다.

### UI Automation

* PC Web / Android / iOS UI 테스트 자동화
* Selenium / Appium 기반 자동화 시나리오 구축
* 반복 회귀 테스트 자동화 및 유지보수

### API Automation

* 주문 / 클레임 API 자동화
* Postman 기반 API 테스트 및 검증
* STG / PRD 환경별 테스트 수행

### Performance Test

* JMeter / nGrinder 기반 성능 테스트
* API 부하 테스트 및 응답 성능 분석

### CI/CD

* GitLab CI/CD 기반 테스트 자동 실행
* Jenkins 기반 자동화 테스트 수행
* 테스트 실행 및 결과 관리 프로세스 개선

---

# 4. Tech Stack

### Test Automation

`Playwright` `Selenium` `Appium`

### API

`Postman` `Newman` `REST API`

### Language / Runtime

`JavaScript` `Node.js` `Python`

### Test Data / Security

`JSON` `YAML` `AES` `SEED` `URL Encoding` `EUC-KR`

### Performance

`JMeter` `nGrinder`

### CI/CD & Collaboration

`GitLab CI/CD` `Jenkins` `Jira` `Confluence`

### Environment & Tools

`VSCode` `SecureCRT` `Oracle SQL Developer`

---

# 5. What I Focus On

**Automation**
반복적인 검증 업무를 자동화하여 테스트 효율성과 일관성을 높입니다.

**Reliability**
단순 실행 성공 여부가 아닌 응답 데이터와 비즈니스 흐름까지 검증하여 테스트의 신뢰성을 높입니다.

**Maintainability**
공통 로직과 데이터 기반 시나리오를 활용하여 변경에 대응하기 쉬운 테스트 구조를 설계합니다.

**Problem Solving**
자동화 과정에서 발생하는 인코딩, 암·복호화, 비동기 UI, 데이터 정합성 등의 문제를 분석하고 해결합니다.

---

# 6. Certification

* **AWS Certified Solutions Architect – Associate (SAA-C03)**

---

# 7. Contact

* **Email**: [hnkim117@gmail.com](mailto:hnkim117@gmail.com)
* **GitHub**: kimhaneul117
