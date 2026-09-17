import express from 'express';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const app = express();

app.use(express.static(path.join(__dirname, 'public')));

app.listen(4173, '127.0.0.1', () => {
  console.log('Demo server: http://127.0.0.1:4173/payment.html');
});
