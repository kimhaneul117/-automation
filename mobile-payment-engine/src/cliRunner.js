import { spawn } from 'node:child_process';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const mockCliPath = path.resolve(__dirname, '../mock/mock-payment-cli.js');

export function runCli(command, params = {}, timeoutMs = 5000) {
  return new Promise((resolve, reject) => {
    const args = [
      mockCliPath,
      `--command=${command}`,
      ...Object.entries(params).map(([key, value]) => `--${key}=${value}`)
    ];

    const child = spawn(process.execPath, args, {
      windowsHide: true
    });

    let stdout = '';
    let stderr = '';

    const timer = setTimeout(() => {
      child.kill();
      reject(new Error(`CLI timeout after ${timeoutMs}ms`));
    }, timeoutMs);

    child.stdout.on('data', chunk => {
      stdout += chunk.toString('utf8');
    });

    child.stderr.on('data', chunk => {
      stderr += chunk.toString('utf8');
    });

    child.on('error', error => {
      clearTimeout(timer);
      reject(error);
    });

    child.on('close', exitCode => {
      clearTimeout(timer);
      resolve({
        stdout: stdout.trim(),
        stderr: stderr.trim(),
        exitCode
      });
    });
  });
}
