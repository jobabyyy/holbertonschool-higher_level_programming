#!/usr/bin/node
function add(a, b) {
    return a + b;
  }
  
  const arg1 = process.argv[2];
  const arg2 = process.argv[3];
  
  if (!arg1 || isNaN(arg1) || !arg2 || isNaN(arg2)) {
    console.log('Missing or invalid arguments');
  } else {
    const num1 = parseInt(arg1);
    const num2 = parseInt(arg2);
    const sum = add(num1, num2);
    console.log(sum);
  }
  