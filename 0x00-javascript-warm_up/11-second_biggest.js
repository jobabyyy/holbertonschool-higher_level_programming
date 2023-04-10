#!/usr/bin/node
const args = process.argv.slice(2);

if (args.length === 0) {
  console.log(0);
} else if (args.length === 1) {
  console.log(0);
} else {
  const numbers = args.map(Number);
  const sorted = numbers.sort((a, b) => b - a);
  console.log(sorted[1]);
}
