$(document).ready(function() {
	$('img').click(function() {
		var x = $(this).attr('src');
		var y = $(this).attr('altsrc');

		$(this).attr('src', y);
		$(this).attr('altsrc', x);
	});
});