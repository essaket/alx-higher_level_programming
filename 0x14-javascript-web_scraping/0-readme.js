#!/usr/bin/node
//Script that reads and prints the content of a file

const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function (error, content) {
	if (err) {
		console.log(err);
	} else {
		console.log(data);
	}
});
