export function validateApiResponse({
  status,
  body,
  requestTime = new Date(),
  toleranceSeconds = 60
}) {
  if (status !== 200) {
    throw new Error(`HTTP status expected 200, received ${status}`);
  }

  if (body.code !== 'SUCCESS') {
    throw new Error(`Unexpected code: ${body.code}`);
  }

  if (typeof body.message !== 'string' || body.message.length === 0) {
    throw new Error('message is required');
  }

  if (!body.transactionId) {
    throw new Error('transactionId is required');
  }

  if (body.createdAt) {
    const actual = new Date(body.createdAt);
    const diffSeconds = Math.abs(actual - requestTime) / 1000;

    if (diffSeconds > toleranceSeconds) {
      throw new Error(
        `createdAt exceeded tolerance: ${diffSeconds.toFixed(1)} sec`
      );
    }
  }

  return true;
}
