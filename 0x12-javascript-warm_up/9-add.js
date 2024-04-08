#!/usr/bin/node
function add (a, b) {
    if (isNaN(a) || isNaN(b)) {
	return NaN;
    }
    return a + b;
}

add(parseInt(process.argv[2]), Number(process.argv[3]));
