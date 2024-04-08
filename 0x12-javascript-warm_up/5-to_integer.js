#!/usr/bin/node

// prints a message if the first arg can be converted to a number
const fArg = process.argv[2];

if (isNaN(fArg) === false) {
  console.log('My number: ' + fArg);
} else {
  console.log('Not a number');
}
