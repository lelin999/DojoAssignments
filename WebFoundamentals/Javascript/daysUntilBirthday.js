var daysUntilBirthday = function(days) {
	while (days > 0) {
		if (days > 30) {
			console.log(days + " days until my birthday. Unlucky :(");
		} else if (days > 5) {
			console.log(days + " until my birthday. Almost there!!!!");
		} else {
			console.log(days + " DAYS UNTIL MY BIRTHDAY!!?!?!??!?!?");
		}
		days--;
	}
	if (days === 0) {
		console.log("dank memes can't break playoff dreams.");
	}
};

daysUntilBirthday(10);