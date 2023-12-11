#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const numArray = process.argv.slice(2).map(Number);
  numArray.sort(function (a, b) {
    return a - b;
  });
  console.log(numArray[numArray.length - 2]);
}
