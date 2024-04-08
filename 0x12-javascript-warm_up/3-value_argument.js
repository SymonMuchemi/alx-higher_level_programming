#!/usr/bin/node

// prints the first argument if any

const fArg = process.argv[2];

if (fArg !== undefined) {
  console.log(fArg);
} else {
  console.log('No argument');
}
