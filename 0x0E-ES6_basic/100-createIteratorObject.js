export function createIteratorObject (report) {
  const total = Object.values(report.allEmployees).reduce((a, b) => {
    a.push(...b)
    return a
  }, [])
  let curr = 0
  return {
    [Symbol.iterator]: () => ({
      next () {
        if (curr < total.length) {
          const res = { data: total[curr], done: false }
          curr += 1
          return res
        } else {
          return { data: null, done: true }
        }
      }
    })
  }
}
