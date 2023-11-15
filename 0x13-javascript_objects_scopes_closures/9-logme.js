#!/usr/bin/node
let argumentNum = 0;

exports.logMe = function (item) {
  console.log(`${argumentNum}: ${item}`);
  argumentNum++;
};
