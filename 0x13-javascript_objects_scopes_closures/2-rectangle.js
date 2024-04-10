#!/usr/bin/node

// empty class
module.exports = class Rectangle {
  width;
  height;

  constructor (w, h) {
    if (w === 0 || h === 0) return {};
    this.width = w;
    this.height = h;
  }
};
