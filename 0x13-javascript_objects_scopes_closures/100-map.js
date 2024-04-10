#!/usr/bin/node
// create a new list with each value equal to the value of the
// initial list, multiplied by the index in the list
const list = require('./100-data.js').list;
let i = 0;

const newList = list.map(element => {
  element = element * i;
  i = i + 1;
  return (element);
});

console.log(list);
console.log(newList);
