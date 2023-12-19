#!/usr/bin/node
// script that prints the addition of 2 integers

const args = process.argv.slice(2);

const firstArgValue = parseInt(args[0]);
const secondArgValue = parseInt(args[1]);

if (Number.isNaN(firstArgValue) | Number.isNaN(secondArgValue)) {
  console.log('NaN');
} else {
  console.log(add(firstArgValue, secondArgValue));
}

function add (a, b) {
  return a + b;
}
