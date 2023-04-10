#!/usr/bin/node
const arg = process.argv[2];

if (!arg || isNaN(arg)) {
  console.log('Missing size');
} else {
  const size = parseInt(arg);

  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
