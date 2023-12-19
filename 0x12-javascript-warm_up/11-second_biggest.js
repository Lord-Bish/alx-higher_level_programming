#!/usr/bin/node
// script that prints the addition of 2 integers

const args = process.argv.slice(2);

const firstArgValue = parseInt(args[0]);

if (args.length === 1) {
  console.log(0);
} else if (Number.isNaN(firstArgValue)) {
  console.log(0);
} else {
  args.sort(function (a, b) {
    return a - b;
  });

  console.log(args[args.length - 2]);
}
