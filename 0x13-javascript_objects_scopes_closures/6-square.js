#!/usr/bin/node
// blueprint for square objects

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  // prints the rectangle
  charPrint (c) {
    if (this.width > 0 && this.height > 0) {
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          if (c !== undefined) {
            process.stdout.write(c);
          } else {
            process.stdout.write('X');
          }
        }
        console.log();
      }
    }
  }
};
