#!/usr/bin/node

// empty class
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      [this.width, this.height] = [w, h];
    }
  }

  print() {
    if (this.width > 0 && this.height > 0) {
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          process.stdout.write('X');
        }
      console.log();
      }
    }
  }
};
