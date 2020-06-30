export default function divideFunction(numerator, denominator) {
  const div = numerator / denominator;
  if (div !== Infinity) {
    return div;
  }
  throw Error('cannot divide by 0');
}
