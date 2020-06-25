export function createIteratorObject (report) {
    const total = Object.values(report.allEmployees).reduce((a, b) => {
        a.push(...b)
        return a
    }, [])
    let curr = 0
    return {
        next() {
            if (curr < total.length) {
                const res = {
                    data: total[curr],
                    done: true
                }
                curr += 1;
                return res;
            } else {
                return {
                    data: null,
                    done: false
                }
            }
        }
    }
}