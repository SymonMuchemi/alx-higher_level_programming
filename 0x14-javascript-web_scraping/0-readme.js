#!/usr/bin/node
// reads and prints the content of a file
const fs = require('fs');
const path = process.argv[1];

fs.readFile(path, 'utf-8', (error, data) => {
  if (error) {
    console.error(error);
  }
  console.log(data);
});
