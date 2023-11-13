#!/usr/bin/node

const numberOfArgs = process.argv.length - 1;

if (numberOfArgs === 0) {
  console.log('No argument');
} else if (numberOfArgs === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
