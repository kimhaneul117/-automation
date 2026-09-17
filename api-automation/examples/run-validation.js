import {
  assertHttpSuccess,
  assertRequired,
  assertSuccessResponse,
  assertArrayContainsAllowedCodes,
  assertTimeWithin
} from '../src/assertions.js';

import {
  encryptAes128Cbc,
  decryptAes128Cbc
} from '../src/cryptoSample.js';

const BASE_NOW = new Date();

const response = {
  status: 200,
  bodyText: JSON.stringify({
    code: 'SUCCESS',
    message: '성공'
  })
};

const body = {
  code: 'SUCCESS',
  message: '성공',
  transactionId: 'SAMPLE-TID-001',
  createdAt: new Date().toISOString(),
  authenticates: [
    { code: 'PASS' },
    { code: 'SMS' }
  ]
};

assertHttpSuccess(response);
assertSuccessResponse(body);
assertRequired(body, ['transactionId', 'createdAt']);

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

const encrypted = encryptAes128Cbc(
  JSON.stringify({ amount: 1000, orderId: 'SAMPLE-001' })
);

const decrypted = decryptAes128Cbc(encrypted);

console.log('All assertions PASS');
console.log('AES round-trip:', decrypted);
