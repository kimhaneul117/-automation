import process from 'node:process';
import { loadScenario } from './scenarioLoader.js';
import { interpolateDeep, mergeContext } from './context.js';
import { runCli } from './cliRunner.js';
import { parseKeyValueResponse } from './responseParser.js';
import { assertResponse } from './validator.js';
import { createReports } from './reporter.js';

const scenarioPath = process.argv[2];

if (!scenarioPath) {
  console.error('Usage: node src/runScenario.js <scenario.yaml>');
  process.exit(1);
}

const scenario = loadScenario(scenarioPath);
let context = { ...(scenario.variables ?? {}) };
const stepResults = [];

console.log(`\n[SCENARIO] ${scenario.name}\n`);

for (const [index, rawStep] of scenario.steps.entries()) {
  const step = interpolateDeep(rawStep, context);
  const startedAt = new Date();

  console.log(`[${index + 1}/${scenario.steps.length}] ${step.name}`);

  try {
    const { stdout, stderr, exitCode } = await runCli(step.command, step.params ?? {});
    const actual = parseKeyValueResponse(stdout);

    if (exitCode !== 0 && actual.RESULT !== 'FAIL') {
      throw new Error(`CLI exitCode=${exitCode}, stderr=${stderr}`);
    }

    assertResponse(actual, step.expect ?? {}, {
      baseTime: startedAt
    });

    context = mergeContext(context, actual, step.extract ?? {});

    stepResults.push({
      index: index + 1,
      name: step.name,
      command: step.command,
      status: 'PASS',
      durationMs: new Date() - startedAt,
      actual
    });

    console.log('  PASS\n');
  } catch (error) {
    stepResults.push({
      index: index + 1,
      name: step.name,
      command: step.command,
      status: 'FAIL',
      durationMs: new Date() - startedAt,
      error: error.message
    });

    console.log(`  FAIL - ${error.message}\n`);
    break;
  }
}

const paths = createReports({
  scenarioName: scenario.name,
  description: scenario.description,
  results: stepResults
});

console.table(
  stepResults.map(({ index, name, command, status, durationMs }) => ({
    index, name, command, status, durationMs
  }))
);

console.log(`JSON report: ${paths.json}`);
console.log(`HTML report: ${paths.html}`);

if (stepResults.some(result => result.status === 'FAIL')) {
  process.exitCode = 1;
}
