#!/usr/bin/node

// Script that prints two arguments passed to it
// concatenated with "is" string

const args = process.argv.slice(2);

if (Number.isNaN(parseInt(args[0]))) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(args[0]));
}
