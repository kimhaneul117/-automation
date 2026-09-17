export function assertHttpSuccess({ status, bodyText }) {
  if (status !== 200) {
    throw new Error(`HTTP_STATUS expected 200, received ${status}`);
  }

  if (!bodyText || bodyText.length === 0) {
    throw new Error('RESPONSE_BODY is empty');
  }
}

export function assertRequired(object, fields) {
  for (const field of fields) {
    const value = object[field];

    if (value === undefined || value === null || value === '') {
      throw new Error(`Required field missing: ${field}`);
    }
  }
}

export function assertSuccessResponse(body) {
  if (body.code !== 'SUCCESS') {
    throw new Error(`Expected code=SUCCESS, received ${body.code}`);
  }

  if (body.message !== '성공') {
    throw new Error(`Unexpected message: ${body.message}`);
  }
}

export function assertArrayContainsAllowedCodes(actualItems, allowedCodes) {
  if (!Array.isArray(actualItems)) {
    throw new Error('Expected an array');
  }

  const unexpected = actualItems.filter(
    item => !allowedCodes.includes(item.code)
  );

  if (unexpected.length > 0) {
    throw new Error(
      `Unexpected codes: ${unexpected.map(item => item.code).join(', ')}`
    );
  }
}

export function assertTimeWithin({
  actual,
  base,
  toleranceSeconds,
  fieldName = 'time'
}) {
  const actualDate = new Date(actual);
  const baseDate = new Date(base);

  if (
    Number.isNaN(actualDate.getTime()) ||
    Number.isNaN(baseDate.getTime())
  ) {
    throw new Error(`${fieldName}: invalid date`);
  }

  const diffSeconds = Math.abs(actualDate - baseDate) / 1000;

  if (diffSeconds > toleranceSeconds) {
    throw new Error(
      `${fieldName}: ${diffSeconds.toFixed(2)}s exceeds ±${toleranceSeconds}s`
    );
  }
}
