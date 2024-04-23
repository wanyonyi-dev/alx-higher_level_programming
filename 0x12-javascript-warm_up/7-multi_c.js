#!/usr/bin/node

const Leng = process.argv;
if (Number(Leng[2])) {
  const num = Number(Leng[2]);
  for (let index = 0; index < num; index++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurences');
}
