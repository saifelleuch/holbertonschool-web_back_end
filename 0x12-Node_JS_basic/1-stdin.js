process.stdout.write('Welcome to Holberton School, what is your name?\n');
process.stdin.setEncoding('utf8');
process.stdin.on('readable', () => {
  const inputName = process.stdin.read();
  if (inputName) process.stdout.write(`Your name is: ${inputName}`);
});
process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});
