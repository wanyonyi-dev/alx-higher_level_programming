#!/usr/bin/node

const Leng = process.argv;
if (Leng.length === 2) {
  console.log('No argument');
} else if (Leng.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
