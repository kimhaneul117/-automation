import fs from 'node:fs';
import path from 'node:path';

function escapeHtml(value) {
  return String(value)
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;');
}

export function createReports({ scenarioName, description, results }) {
  const reportDir = path.resolve('reports');
  fs.mkdirSync(reportDir, { recursive: true });

  const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
  const baseName = `${scenarioName}-${timestamp}`;

  const report = {
    scenarioName,
    description,
    executedAt: new Date().toISOString(),
    summary: {
      total: results.length,
      passed: results.filter(item => item.status === 'PASS').length,
      failed: results.filter(item => item.status === 'FAIL').length
    },
    results
  };

  const jsonPath = path.join(reportDir, `${baseName}.json`);
  const htmlPath = path.join(reportDir, `${baseName}.html`);

  fs.writeFileSync(jsonPath, JSON.stringify(report, null, 2), 'utf8');

  const rows = results.map(item => `
    <tr>
      <td>${item.index}</td>
      <td>${escapeHtml(item.name)}</td>
      <td>${escapeHtml(item.command)}</td>
      <td>${item.status}</td>
      <td>${item.durationMs}</td>
      <td><pre>${escapeHtml(item.error ?? JSON.stringify(item.actual, null, 2))}</pre></td>
    </tr>
  `).join('');

  fs.writeFileSync(htmlPath, `
<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8" />
  <title>${escapeHtml(scenarioName)}</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 32px; }
    table { border-collapse: collapse; width: 100%; }
    th, td { border: 1px solid #ddd; padding: 10px; vertical-align: top; }
    th { background: #f5f5f5; }
    pre { white-space: pre-wrap; margin: 0; }
  </style>
</head>
<body>
  <h1>${escapeHtml(scenarioName)}</h1>
  <p>${escapeHtml(description ?? '')}</p>
  <p>PASS ${report.summary.passed} / FAIL ${report.summary.failed}</p>
  <table>
    <thead>
      <tr>
        <th>#</th><th>Step</th><th>Command</th><th>Status</th><th>ms</th><th>Detail</th>
      </tr>
    </thead>
    <tbody>${rows}</tbody>
  </table>
</body>
</html>
  `, 'utf8');

  return { json: jsonPath, html: htmlPath };
}
