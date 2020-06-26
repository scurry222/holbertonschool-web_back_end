export default function iterateThroughObject (reportWithIterator) {
  const object = ''
  for (let next = reportWithIterator.next(); !next.done;
    next = reportWithIterator.next()) object.append(next.value + ' | ')
  return object
}
