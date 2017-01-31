var arr = [1,2,3,4,5];

$(document).ready(function(){
	$('#button1').click(function() {
		alert("this is working");
	});

	for (var i = 0; i < arr.length; i++) {
		$('.decklists2').append(arr[i] + " ");
	}

	$('.decklists1').html("Now it became this");

	$('div').after("<p>Room for me?</p>");
});

.click
.hide
.show
.toggle
.slideDown
.slideUp
.slideToggle
.fadeIn
.fadeOut
.addClass
.before
.after
.append
.html
.attr
.val
.text
.data