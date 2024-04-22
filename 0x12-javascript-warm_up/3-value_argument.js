#!/usr/bin/node

const Leng = process.argv;
if (!Leng[2]) {
  console.log('No argument');
} else {
  console.log(Leng[2]);
}
