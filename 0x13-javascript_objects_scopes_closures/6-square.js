#!/usr/bin/node
// blueprint for square objects

const Squared = require('./5-square');

module.exports = class Square extends Squared {
  // prints the square using a given character
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) console.log(c.repeat(this.width));
    }
  }
};
