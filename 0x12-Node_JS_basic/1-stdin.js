const { spawn } = require('child_process');

const child = spawn('cat');

process.stdin.pipe(child.stdin);

console.log('Welcome to Holberton School, what is your name?')

child.stdout.on('data', (data) => {
    process.stdout.write(`Your name is: ${data}`);
});

child.on('exit', () => {
 console.log('This important software is now closing');
})
