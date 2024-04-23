#!/usr/bin/node
let x, y;
const Leng = process.argv;

if (Number(Leng[2]) && Number(Leng[3])) {
  x = Number(Leng[2]);
  y = Number(Leng[3]);

  add(x, y);
} else {
  console.log(NaN);
}

function add (x, y) {
  const sum = x + y;
  console.log(sum);
}
