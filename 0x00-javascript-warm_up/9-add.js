#!/usr/bin/node
function add(a, b) {
    return a + b;
  }
  
  const arg0 = process.argv[2];
  const arg1 = process.argv[3];
  
  if (!arg0 || isNaN(arg0) || !arg1 || isNaN(arg1)) {
    console.log('Missing or invalid arguments');
  } else {
    const num1 = parseInt(arg0);
    const num2 = parseInt(arg1);
    const sum = add(num1, num2);
    console.log(sum);
  }
  