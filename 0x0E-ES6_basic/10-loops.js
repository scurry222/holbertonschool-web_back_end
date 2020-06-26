export default function appendToEachArrayValue(array, appendString) {
  const arrayCopy = array;
  for (const value of array) {
    const idx = array.indexOf(value);
    arrayCopy[idx] = appendString + value;
  }

  return arrayCopy;
}
