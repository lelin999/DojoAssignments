var fancy_array = function (arr, symb, reversed) {
	if (reversed === true) {
		for (var i = arr.length - 1; i >= 0; i--) {
			if (symb) {
				console.log(i + symb + arr[i]);	
			} else {
				console.log(i + "->" + arr[i]);
			}
		}
	} else {
		for (var i = 0; i < arr.length; i++) {
			if (symb) {
				console.log(i + symb + arr[i]);	
			} else {
				console.log(i + "->" + arr[i]);
			}
		}
	}	
};

var arr = ['James', 'Jack', 'Jill', 'Jane'];
fancy_array(arr, "----", true);