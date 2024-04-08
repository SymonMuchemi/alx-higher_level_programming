#!/usr/bin/node

// function that execute a function passed as a parameter
exports.addMeMaybe = function (x, theFunction) {
  x = x + 1;
  theFunction(x);
};
