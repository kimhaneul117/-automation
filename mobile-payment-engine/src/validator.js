function fail(field, message, actualValue) {
  throw new Error(`${field}: ${message} (actual=${JSON.stringify(actualValue)})`);
}

export function assertResponse(actual, rules, options = {}) {
  for (const [field, rule] of Object.entries(rules)) {
    const value = actual[field];

    if (rule.required && (value === undefined || value === null || value === '')) {
      fail(field, 'required value is missing', value);
    }

    if ('equals' in rule && String(value) !== String(rule.equals)) {
      fail(field, `expected ${JSON.stringify(rule.equals)}`, value);
    }

    if (rule.oneOf && !rule.oneOf.map(String).includes(String(value))) {
      fail(field, `expected one of ${JSON.stringify(rule.oneOf)}`, value);
    }

    if (rule.regex) {
      const regex = new RegExp(rule.regex);
      if (!regex.test(String(value ?? ''))) {
        fail(field, `does not match ${rule.regex}`, value);
      }
    }

    if (rule.isoTimeWithinSeconds !== undefined) {
      const actualTime = new Date(value);
      const baseTime = options.baseTime ?? new Date();

      if (Number.isNaN(actualTime.getTime())) {
        fail(field, 'is not a valid ISO date', value);
      }

      const diffSeconds = Math.abs(actualTime - baseTime) / 1000;
      if (diffSeconds > rule.isoTimeWithinSeconds) {
        fail(
          field,
          `time difference ${diffSeconds.toFixed(2)}s exceeds ${rule.isoTimeWithinSeconds}s`,
          value
        );
      }
    }
  }
}
