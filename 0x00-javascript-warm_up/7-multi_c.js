#!/usr/bin/node
const arg = process.argv[2];

if (!arg || isNaN(arg)) { // checks if num is not null & can be converted
  console.log('Missing number of occurrences');
} else {
  const x = parseInt(arg); // converting to an integer
  let count = 0;

  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
