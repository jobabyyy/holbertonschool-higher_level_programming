#!/usr/bin/node
const nbOccurrences = require('./7-occurrences').nbOccurences;

console.log(nbOccurrences([1, 2, 3, 4, 5, 6], 3));
console.log(nbOccurrences([3, 2, 3, 4, 5, 3, 3], 3));
console.log(nbOccurrences(["S", 12, "c", "S", "School", 8], "S"));
