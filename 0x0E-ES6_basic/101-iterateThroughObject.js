export default function iterateThroughObject(reportWithIterator) {
  let object = '';
  let curr = reportWithIterator[Symbol.iterator]().next();
  while (!curr.done) {
    object += `${curr.data} | `;
    curr = reportWithIterator[Symbol.iterator]().next();
  }
  return object.slice(0, object.length - 3);
}
