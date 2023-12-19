#!/usr/bin/node
// print 3 lines by looping over an array containing strings

const myArray = ['C is fun', 'Python is cool', 'JavaScript is amazing'];

let count = 0;

while (count < 3) {
  console.log(myArray[count]);
  count += 1;
}
