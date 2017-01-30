var reward = function (num) {
	var sum = 0;
	var reward = 0.01;
	// var count = 0
	//count is for days to make x amount of money
	for (var i = 1; i <= num; i++) {
		// count += 1;
		sum += reward;
		reward = reward * 2;
		// if(sum >= 10000) {
		// 	return count;
		// } 
	}
	return "$" + sum;
};

reward(30);