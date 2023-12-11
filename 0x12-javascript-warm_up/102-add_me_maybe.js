#!/usr/bin/node
exports.addMeMaybe = function (number, fun) {
  fun(++number);
};
