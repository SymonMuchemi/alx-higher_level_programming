#!/usr/bin/node

// finds the factorial of a number
function fact (a) {
  if (a === 0 || a === 1) return 1;

  return (a * fact(a - 1));
}

console.log(fact(Number(process.argv[2])));
