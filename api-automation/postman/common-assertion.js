const BASE_NOW = pm.variables.get('BASE_NOW')
  ? new Date(pm.variables.get('BASE_NOW'))
  : new Date();

const jsonData = pm.response.json();

pm.test('HTTP Status 200', () => {
  pm.response.to.have.status(200);
});

pm.test('응답 본문 존재 확인', () => {
  pm.expect(pm.response.text()).to.not.eql('');
});

pm.test('응답 코드/메시지 정상 확인', () => {
  pm.expect(jsonData.code).to.eql('SUCCESS');
  pm.expect(jsonData.message).to.eql('성공');
});

pm.test('필수 필드 확인', () => {
  pm.expect(jsonData.transactionId).to.be.a('string').and.not.empty;
});

pm.test('인증수단 허용값 확인', () => {
  const allowedCodes = ['PASS', 'SMS', 'QR'];

  pm.expect(jsonData.authenticates).to.be.an('array');

  jsonData.authenticates.forEach(item => {
    pm.expect(allowedCodes).to.include(item.code);
  });
});

pm.test('createdAt 기준시각 ±60초 확인', () => {
  const createdAt = new Date(jsonData.createdAt);
  const diffSeconds = Math.abs(createdAt - BASE_NOW) / 1000;

  pm.expect(diffSeconds).to.be.at.most(60);
});
