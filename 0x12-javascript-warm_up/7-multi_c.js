#!/usr/bin/node
const x = parseInt(process.argv[2]);
if (isNaN(x)) {
	console.log('Missing number of occurrences');
} else {
	let y = 0;
	while (y < x) {
		console.log('C is fun');
		y++;
	}
}
