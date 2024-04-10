#!/usr/bin/node
// concates the content in two files
const fs = require('fs');

if (process.argv.length < 5) {
  console.log('Usage: ./102-concat.js <file1> <file2> <destination_file>');
  process.exit(1);
}

let txtA = '';
let txtB = '';
let txtC = '';

fs.readFile(process.argv[2], 'utf8', (err, data) => {
  if (err) {
    console.log(`Could not read file ${process.argv[2]}`);
    return;
  }
  txtA = data;

  fs.readFile(process.argv[3], 'utf8', (err, data) => {
    if (err) {
      console.log(`Could not read file ${process.argv[3]}`);
      return;
    }
    txtB = data;

    txtC = txtA + txtB;

    fs.writeFile(process.argv[4], txtC, (err) => {
      if (err) {
        console.log(`Could not write to file ${process.argv[4]}`);
      }
    });
  });
});
