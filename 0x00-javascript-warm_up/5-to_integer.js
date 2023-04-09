#!/usr/bin/node
const args = process.argv[2];
const MyNum = Number(args); // assigning num func to convert

if (Number.isNaN(MyNum)) { // Opening brace moved to same line
  console.log('Not a number');
} else {
  console.log(`My number: ${MyNum}`); // prints value of mynum
}
