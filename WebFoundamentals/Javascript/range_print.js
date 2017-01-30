var print_range = function (start, end, skip) {
	if (!skip) {
		skip = 1;
	}

	if (!end) {
		end = start;
		start = 0;
	}

	for (var i = start; i < end; i+=skip) {
		console.log(i);
	}
}

print_range(2, 10, 2);
print_range(4, 8);
print_range(4);