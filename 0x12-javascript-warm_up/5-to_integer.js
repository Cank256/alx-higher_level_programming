#!/usr/bin/node

const getNum = process.argv[2];
const myNum = parseInt(getNum);

if (!isNaN(myNum)) {
  console.log(`My number: ${myNum}`);
} else {
  console.log('Not a number');
}
