$(document).ready(function() {
	$('form').submit(function () {
		return false;
	})
	$("form").submit(function (event) {
		$('table').append('cat');
	})
});





// $('form').submit(function() {
// 	$('table').addClass('table');
// });