#!/usr/bin/node
// print 'count' times a statment

const statement = 'C is fun';

let count = 0;

const args = process.argv.slice(2);

if (Number.isNaN(parseInt(args[0]))) {
  console.log('Missing number of occurrences');
} else {
  while (count < parseInt(args[0])) {
    console.log(statement);
    count += 1;
  }
}
