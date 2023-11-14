#!/usr/bin/node

const computeFactorial = (n) => {
  if (isNaN(n)) {
    console.log(1);
  } else {
    const factorial = (n) => (n <= 1 ? 1 : n * factorial(n - 1));
    console.log(factorial(n));
  }
};

const myNum = parseInt(process.argv[2]);
computeFactorial(myNum);
