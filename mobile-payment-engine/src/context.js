const VARIABLE_PATTERN = /\$\{([A-Z0-9_]+)\}/g;

export function interpolateString(value, context) {
  return value.replace(VARIABLE_PATTERN, (_, key) => {
    if (!(key in context)) {
      throw new Error(`Undefined scenario variable: ${key}`);
    }
    return String(context[key]);
  });
}

export function interpolateDeep(value, context) {
  if (typeof value === 'string') {
    return interpolateString(value, context);
  }

  if (Array.isArray(value)) {
    return value.map(item => interpolateDeep(item, context));
  }

  if (value && typeof value === 'object') {
    return Object.fromEntries(
      Object.entries(value).map(([key, item]) => [
        key,
        interpolateDeep(item, context)
      ])
    );
  }

  return value;
}

export function mergeContext(context, response, extractMap) {
  const next = { ...context };

  for (const [variableName, responseKey] of Object.entries(extractMap)) {
    if (!(responseKey in response)) {
      throw new Error(`Cannot extract "${responseKey}" from response`);
    }
    next[variableName] = response[responseKey];
  }

  return next;
}
