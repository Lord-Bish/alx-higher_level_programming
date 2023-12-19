#!/usr/bin/node

// Script that prints two arguments passed to it
// concatenated with "is" string

const args = process.argv.slice(2);

console.log(args[0] + ' is ' + args[1]);
