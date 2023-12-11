#!/usr/bin/node
const x = process.argv[2];
let S = 1;
if (!isNaN(x)) {
  for (let i = 1; i <= x; i++) {
    S = S * i;
  }
}
console.log(S);
