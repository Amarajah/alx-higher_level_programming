#!/usr/bin/node

let myArray;
if (process.argv.length === 2 || process.argv.length === 3) {
  console.log(0);
} else {
  myArray = process.argv.slice(2);
  myArray.sort(function (a, b) { return (a - b); });
  myArray.reverse();
  console.log(myArray[1]);
}
