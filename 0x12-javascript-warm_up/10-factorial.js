#!/usr/bin/node
if (process.argv.length <= 2 || isNaN(process.argv[2])) {
  console.log('1');
} else {
  const x = process.argv[2];
  let S = 1;
  for (let i = 1; i <= x; i++) {
    S = S * i;
  }
  console.log(S);
}
