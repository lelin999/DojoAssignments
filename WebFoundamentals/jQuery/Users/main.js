$(document).ready(function() {
	$('form').submit(function () {
		var first_name_value = $("form input[name='firstname']").val();
		var last_name_value = $("form input[name='lastname']").val();
		var email_value = $("form input[name='email']").val();
		var contact_value = $("form input[name='contact']").val();

		$('.table1').append("<tr><td>" + "insert text here" + "</td><td>" + "other text" + "</td><td>" + "more text" + "</td><td>" + "last text" + "</td></tr>");
		
		return false;
	});
});
