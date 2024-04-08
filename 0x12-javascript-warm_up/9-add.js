#!/usr/bin/node

// adds two integer arguments
const num1 = process.argv[2];
const num2 = process.argv[3];

// function to add the two numbers
function add (a, b) { return (a + b); }

if (isNaN(num1) === false && isNaN(num2) === false) {
  const a = parseInt(num1);
  const b = parseInt(num2);

  console.log(add(a, b));
}



