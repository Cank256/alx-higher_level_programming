#!/usr/bin/node

const x = process.argv[1];

if (x === undefined) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
