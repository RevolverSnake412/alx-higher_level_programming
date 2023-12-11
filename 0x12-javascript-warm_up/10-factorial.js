#!/usr/bin/node
if (process.argv.length <= 2 || isNaN(process.argv[2])) {
  console.log(1);
} else {
  function fact (x) {
    let S = 1;
    if (x > 1) {
      S = fact(x - 1);
    }
    return (S * x);
  }
  const Result = fact(Number(process.argv[2]));
  console.log(Result);
}
