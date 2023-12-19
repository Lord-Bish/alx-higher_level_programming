#!/usr/bin/node
// script that prints a square using 'X'

const squareChar = 'X';

let count = 0;

let tmp = '';
const args = process.argv.slice(2);

const argValue = parseInt(args[0]);

if (Number.isNaN(argValue)) {
  console.log('Missing size');
} else {
  while (count < argValue) {
    tmp += squareChar;
    count += 1;
  }

  for (let i = 0; i < argValue; i++) {
    console.log(tmp);
  }
}
