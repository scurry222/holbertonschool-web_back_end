const fs = require('fs');

module.exports = function countStudents(path) {
  try {
    const data = fs.readFileSync(path, { encoding: 'utf-8' });
    const totalData = data.split('\n').filter((line) => line).slice(1);

    console.log(`Number of students: ${totalData.length}`);

    let csCount = 0;
    let csStudents = '';

    let sweCount = 0;
    let sweStudents = '';

    totalData.forEach((line) => {
      let students = line;
      students = students.split(',');
      if (students[3] === 'CS') {
        csCount += 1;
        csStudents += csStudents ? `, ${students[0]}` : students[0];
      } else if (students[3] === 'SWE') {
        sweCount += 1;
        sweStudents += sweStudents ? `, ${students[0]}` : students[0];
      }
    });

    console.log(`Number of students in CS: ${csCount}. List: ${csStudents}`);
    console.log(`Number of students in SWE: ${sweCount}. List: ${sweStudents}`);
  } catch (err) { throw new Error('Cannot load the database'); }
};

// {CS: {count: count, students: []}, SWE : {count: count, students: []}}
