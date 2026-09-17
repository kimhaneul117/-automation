function parseArgs(argv) {
  return Object.fromEntries(
    argv.map(arg => {
      const normalized = arg.replace(/^--/, '');
      const index = normalized.indexOf('=');
      return index === -1
        ? [normalized, '']
        : [normalized.slice(0, index), normalized.slice(index + 1)];
    })
  );
}

function nowIso() {
  return new Date().toISOString();
}

function createTid() {
  const date = new Date();
  const ymdhms = [
    date.getFullYear(),
    String(date.getMonth() + 1).padStart(2, '0'),
    String(date.getDate()).padStart(2, '0'),
    String(date.getHours()).padStart(2, '0'),
    String(date.getMinutes()).padStart(2, '0'),
    String(date.getSeconds()).padStart(2, '0')
  ].join('');

  return `T${ymdhms}A1B2`;
}

function print(obj) {
  process.stdout.write(
    Object.entries(obj)
      .map(([key, value]) => `${key}=${value}`)
      .join(';')
  );
}

const args = parseArgs(process.argv.slice(2));
const command = args.command;

if (!command) {
  print({
    RESULT: 'FAIL',
    ERROR_CODE: 'MISSING_COMMAND',
    ERROR_MESSAGE: 'command is required'
  });
  process.exit(2);
}

if (command === 'ITEM_SEND' && !args.amount) {
  print({
    RESULT: 'FAIL',
    ERROR_CODE: 'MISSING_AMOUNT',
    ERROR_MESSAGE: 'amount is required'
  });
  process.exit(1);
}

switch (command) {
  case 'ITEM_SEND':
    print({
      RESULT: 'SUCCESS',
      TID: createTid(),
      DATE: nowIso(),
      AMOUNT: args.amount,
      CARRIER: args.carrier ?? 'SAMPLE'
    });
    break;

  case 'DELIVERY':
    print({
      RESULT: 'SUCCESS',
      TID: args.tid,
      DATE: nowIso()
    });
    break;

  case 'REPORT':
    print({
      RESULT: 'SUCCESS',
      TID: args.tid,
      STATUS: 'PAID'
    });
    break;

  case 'CANCEL':
    print({
      RESULT: 'SUCCESS',
      TID: args.tid,
      CANCEL_DATE: nowIso()
    });
    break;

  default:
    print({
      RESULT: 'FAIL',
      ERROR_CODE: 'UNKNOWN_COMMAND',
      ERROR_MESSAGE: `unsupported command: ${command}`
    });
    process.exit(1);
}
