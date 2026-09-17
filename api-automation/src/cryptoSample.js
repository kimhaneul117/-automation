import crypto from 'node:crypto';

// Portfolio sample only.
// 실제 서비스 KEY/IV와 무관한 임의의 값입니다.
const SAMPLE_KEY = Buffer.from('0123456789abcdef', 'utf8');
const SAMPLE_IV = Buffer.from('abcdef0123456789', 'utf8');

export function encryptAes128Cbc(plainText) {
  const cipher = crypto.createCipheriv('aes-128-cbc', SAMPLE_KEY, SAMPLE_IV);
  return Buffer.concat([
    cipher.update(plainText, 'utf8'),
    cipher.final()
  ]).toString('base64');
}

export function decryptAes128Cbc(base64CipherText) {
  const decipher = crypto.createDecipheriv(
    'aes-128-cbc',
    SAMPLE_KEY,
    SAMPLE_IV
  );

  return Buffer.concat([
    decipher.update(Buffer.from(base64CipherText, 'base64')),
    decipher.final()
  ]).toString('utf8');
}
