#!/usr/bin/node

const Leng = process.argv;
if (Number(Leng[2])) {
  console.log('My number: ' + Number(Leng[2]));
} else {
  console.log('Not a number');
}
