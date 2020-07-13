const fs = require('fs');

module.exports = function countStudents(path) {
    return new Promise((resolve, reject) => {
        fs.readFile(path, { encoding: 'utf-8' }, (err, data) => {
            try {
                if (err) reject(Error('Cannot load the database'));
                data = data.split('\n').slice(1);

                console.log(`Number of students: ${data.length}`);

                let csCount = 0;
                let csStudents = '';

                let sweCount = 0;
                let sweStudents = '';

                data.forEach((line) => {
                    line = line.split(',');
                    if (line[3] === 'CS') {
                        csCount += 1;
                        csStudents += csStudents ? `, ${line[0]}` : line[0];
                    } else if (line[3] === 'SWE') {
                        sweCount += 1;
                        sweStudents += sweStudents ? `, ${line[0]}` : line[0];
                    }
                });
                
                console.log(`Number of students in CS: ${csCount}. List: ${csStudents}`);
                console.log(`Number of students in SWE: ${sweCount}. List: ${sweStudents}`);
                resolve();
            } catch (err) {reject(Error('Cannot load the database'))};
        });
    })
}
