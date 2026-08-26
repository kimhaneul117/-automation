const jsonData = pm.response.json();

pm.test('Status code is 200', () => {
  pm.response.to.have.status(200);
});

pm.test('응답 코드 정상 확인', () => {
  pm.expect(jsonData.code).to.eql('SUCCESS');
});

pm.test('필수 transactionId 존재 확인', () => {
  pm.expect(jsonData.transactionId).to.be.a('string').and.not.empty;
});

pm.test('createdAt 요청 시각 기준 ±60초 확인', () => {
  const requestTime = new Date(pm.variables.get('BASE_NOW'));
  const createdAt = new Date(jsonData.createdAt);
  const diffSeconds = Math.abs(createdAt - requestTime) / 1000;

  pm.expect(diffSeconds).to.be.below(60);
});
