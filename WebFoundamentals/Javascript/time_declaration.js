var timeTeller = function(hour, minute, period) {
	var text = function(num) {
		if (num < 30) {
			return("just after");
		} else {
			return("almost");
		}
	};

	var timeOfDay = function(time) {
		if (time === "AM") {
			return("in the morning");
		} else {
			return("in the evening");
		}
	};

	return("It's " + text(minute) + " " + hour + " " + timeOfDay(period));
}

timeTeller(7, 15, "AM");