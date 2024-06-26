#!/usr/bin/node
// imports a dictionary of occurrences by user id and computes a dict of
// user ids by occurrence
const dict = require('./101-data').dict;

const myDict = {};

for (const key in dict) {
  if (myDict[dict[key]] === undefined) {
    myDict[dict[key]] = [key];
  } else {
    myDict[dict[key]].push(key);
  }
}

console.log(myDict);
