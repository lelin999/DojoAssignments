var numbers_only = function (arr) {
	var newArr = [];
	for (var i = 0; i < arr.length; i++) {
		if (typeof arr[i] === 'number') {
			newArr.push(arr[i]);
		}
	}
	return newArr;
}

numbers_only(arr);
var arr = [1, "apple", -3, "orange", 'truck', 0.5, 234, 234234,3423];

var not_numbers = function (arr) {
	for (var i = arr.length - 1; i >= 0; i--) {
		if (typeof arr[i] === 'number') {
			arr.splice(i, 1);
		}
	}

	return arr;
};

not_numbers(arr);