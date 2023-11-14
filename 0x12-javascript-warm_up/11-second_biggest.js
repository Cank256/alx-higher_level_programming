#!/usr/bin/node

const args = process.argv.slice(2).map(Number);
const secondBiggest = args.length < 2 ? 0 : Math.max(...args.filter(num => num !== Math.max(...args)));

console.log(secondBiggest);
