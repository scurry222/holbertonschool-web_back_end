const fs = require('fs');

module.exports = function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, { encoding: 'utf-8' }, (err, data) => {
      try {
        if (err) reject(Error('Cannot load the database'));
        const totalData = data.split('\n').slice(1);

        console.log(`Number of students: ${data.length}`);

        let csCount = 0;
        let csStudents = '';

        let sweCount = 0;
        let sweStudents = '';

        totalData.forEach((line) => {
          const students = line.split(',');
          if (students[3] === 'CS') {
            csCount += 1;
            csStudents += csStudents ? `, ${students[0]}` : students[0];
          } else if (students[3] === 'SWE') {
            sweCount += 1;
            sweStudents += sweStudents ? `, ${students[0]}` : students[0];
          }
        });

        console.log(
          `Number of students in CS:\
                     ${csCount}. List: ${csStudents}`,
        );
        console.log(
          `Number of students in SWE:\
                     ${sweCount}. List: ${sweStudents}`,
        );
        resolve();
      } catch (err) { reject(Error('Cannot load the database')); }
    });
  });
};
