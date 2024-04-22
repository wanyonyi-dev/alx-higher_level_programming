
#!/usr/bin/node

const Leng = process.argv;
if (Number(Leng[2])) {
  const num = Number(Leng[2]);
  for (let row = 0; row < num; row++) {
    // defining a row
    let sqr = '';
    for (let col = 0; col < num; col++) {
      // defining a column
      sqr += 'X';
    }
    // printing square
    console.log(sqr);
  }
} else {
  console.log('Missing number of occurences');
}

