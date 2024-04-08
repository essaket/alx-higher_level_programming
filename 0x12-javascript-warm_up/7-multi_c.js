#!/usr/bin/node
const string = parseInt(process.argv[2]);
if (isNaN(string)) {
    console.log('Missing number of occurrences');
} else {
   for (let i = 0; i < string; i++) {
       console.log('C is fun');
    }
}
