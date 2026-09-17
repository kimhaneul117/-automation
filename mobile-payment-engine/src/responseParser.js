export function parseKeyValueResponse(stdout) {
  if (!stdout) {
    throw new Error('Empty CLI response');
  }

  return stdout
    .split(';')
    .filter(Boolean)
    .reduce((acc, pair) => {
      const index = pair.indexOf('=');

      if (index < 1) {
        throw new Error(`Invalid response pair: ${pair}`);
      }

      const key = pair.slice(0, index).trim();
      const value = pair.slice(index + 1).trim();
      acc[key] = value;

      return acc;
    }, {});
}
