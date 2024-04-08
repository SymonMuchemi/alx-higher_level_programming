#!/usr/bin/node

// function to add two numbers
function add (a, b) {
  const x = a + b;

  console.log(x);
}

add(Number(process.argv[2]), Number(process.argv[3]));
