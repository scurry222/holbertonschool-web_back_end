const fs = require('fs');

module.exports = function countStudents(path) {
    try {
        let data = fs.readFileSync(path, { encoding: 'utf-8' });
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
        
    } catch (err) { throw new Error("Cannot load the database") }
}

// {CS: {count: count, students: []}, SWE : {count: count, students: []}}