#!/usr/bin/node

// prints a string variable times
const x = process.argv[2];

if (isNaN(x) === true) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < x; i++) console.log('C is fun');
}
