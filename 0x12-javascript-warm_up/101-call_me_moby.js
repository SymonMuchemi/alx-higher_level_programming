#!/usr/bin/node

// function that execute a function passed as a parameter
exports.callMeMoby = function (x, theFunction) {
  for (let i = 0; i < x; i++) theFunction();
};
