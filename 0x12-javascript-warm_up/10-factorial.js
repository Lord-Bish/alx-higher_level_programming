#!/usr/bin/node
// script that prints the addition of 2 integers

const args = process.argv.slice(2);

const firstArgValue = parseInt(args[0]);

if (Number.isNaN(firstArgValue)) {
  console.log(1);
} else {
  console.log(factorial(firstArgValue));
}

function factorial (n) {
  if (n === 0 || n === 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}
