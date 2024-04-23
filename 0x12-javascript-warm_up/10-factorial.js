#!/usr/bin/node
let x;
const Leng = process.argv;

if (Number(Leng[2])) {
  x = Number(Leng[2]);

  console.log(factorial(x));
} else {
  console.log(1);
}

function factorial (x) {
  if (x === 0) {
    return 1;
  } else {
    return x * factorial(x - 1);
  }
}
