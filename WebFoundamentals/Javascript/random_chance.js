var random = function (num, desired) {
	var winnings;
	var howMuchDidIWin = function () {
		return Math.floor(Math.random() * 50) + 50;
	}
	num = num - 1;

	if (num > 0) {
		if ((Math.floor(Math.random() * 100)) === 0) {
			winnings = num + howMuchDidIWin();
			if (desired) {
				if (winnings < desired) {
					return random(winnings);
				}	
			}
			return winnings;
		} 
		else {
			return random(num);
		}
	}
	
	return 0;
};

random(20);