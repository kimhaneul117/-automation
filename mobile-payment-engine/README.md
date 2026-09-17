# Mobile Payment Scenario Engine

실무에서 경험한 **CLI 기반 휴대폰결제 자동화 엔진**을 공개 가능한 수준으로 재구성한 예제입니다.

## 핵심 포인트

- YAML로 승인/취소 시나리오 관리
- `child_process.spawn()` 기반 CLI 실행
- `KEY=VALUE;...` 형식 stdout 파싱
- 응답값을 context 변수로 저장하여 후속 step에 재사용
- required / equals / regex / time tolerance Assertion
- 실패 step도 결과에 남기는 JSON + HTML report
- 실제 사내 CLI 대신 `mock-payment-cli.js` 사용

## Example Flow

```text
ITEM_SEND
   ↓ extract TID
DELIVERY (${TID})
   ↓
REPORT (${TID})
   ↓
CANCEL (${TID})
```

## Run

```bash
npm install
npm test
```

실제 회사 실행 파일, 결제 전문, 암호화 키, URL은 포함하지 않습니다.
