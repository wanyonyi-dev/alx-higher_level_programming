#!/usr/bin/node
const Num = process.argv;
const array = [0];

for (let i = 2; i < Num.length; i++) {
  if (!Number(Num[i])) {
    array.push(0);
  } else {
    array.push(Number(Num[i]));
  }
}
array.sort((a, b) => a - b);
if (array.length > 1) {
  console.log(array[array.length - 2]);
} else {
  console.log(0);
}
