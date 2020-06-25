export default function appendToEachArrayValue(array, appendString) {
  for (var idx of array) {
    var value = idx;
    idx = appendString + value;
  }

  return array;
}
