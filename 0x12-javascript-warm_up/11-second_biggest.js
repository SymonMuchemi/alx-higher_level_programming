#!/usr/bin/node

// finds the second largest integer argument
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const intArr = [];

  for (let i = 3; i < process.argv.length; i++) {
    const num = process.argv[i];

    if (!isNaN(num)) intArr.push(num);
  }

  intArr.sort((a, b) => a - b);

  console.log(intArr[intArr.length - 2]);
}
