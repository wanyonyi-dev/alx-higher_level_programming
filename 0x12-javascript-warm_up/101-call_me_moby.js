#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let index = x; index > 0; index--) {
    theFunction.call();
  }
};
