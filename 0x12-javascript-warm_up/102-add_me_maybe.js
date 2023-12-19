#!/usr/bin/node

module.exports.addMeMaybe = function addMeMaybe (x, theFunction) {
  x += 1;
  theFunction(x);
};
