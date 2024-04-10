#!/usr/bin/node

// empty class
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      [this.width, this.height] = [w, h];
    }
  }

  // prints the rectangle
  print () {
    if (this.width > 0 && this.height > 0) {
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          process.stdout.write('X');
        }
        console.log();
      }
    }
  }

  // exchanges the values of width and height
  rotate () {
    if (this.width > 0 && this.height > 0) {
      [this.width, this.height] = [this.height, this.width];
    }
  }

  // double the size of width and height
  double () {
    [this.height, this.width] = [2 * this.height, 2 * this.width];
  }
};
