import fs from 'node:fs';
import path from 'node:path';
import YAML from 'yaml';

export function loadScenario(inputPath) {
  const resolved = path.resolve(inputPath);
  const raw = fs.readFileSync(resolved, 'utf8');
  const scenario = YAML.parse(raw);

  if (!scenario?.name) {
    throw new Error('Scenario name is required');
  }

  if (!Array.isArray(scenario.steps) || scenario.steps.length === 0) {
    throw new Error('Scenario steps must be a non-empty array');
  }

  return scenario;
}
