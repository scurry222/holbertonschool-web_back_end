export default function guardrail(mathFunction) {
  const queue = [];
  try {
    const res = mathFunction();
    queue.push(res);
  } catch (err) {
    queue.push(err);
  }
  queue.push('Guardrail was processed');
  return queue;
}
