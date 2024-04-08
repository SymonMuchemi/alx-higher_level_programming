#!/usr/bin/node

// adds two integer arguments
const num1 = process.argv[2];
const num2 = process.argv[3];

function add (a, b) {
  return (0 + a + b);
}

if (isNaN(num1) === false && isNaN(num2) === false) {
  const a = parseFloat(num1);
  const b = parseFloat(num2);

  console.log(add(a, b));
}
