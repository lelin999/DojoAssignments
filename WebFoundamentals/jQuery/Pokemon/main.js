$(document).ready(function() {
	for (var i = 1; i <= 151; i++) {
		$('.pokemon').append('<img id=' + i + ' src="http://pokeapi.co/media/img/' + i + '.png">');
		$('img').css({"width": "23%", "height": "150px"});
		$('img').css("border", "3px solid blue");
	};


	$('img').on('click', function() {
		var x = ($(this).attr('id'));
		$.get("http://pokeapi.co/api/v1/pokemon/" + x, function(res) {
			var html_type = "";
			var html_height = "";
			var html_weight = "";

			html_type += "<h4>Type</h4>";
			html_type += "<ul>";
			for (var i = 0; i < res.types.length; i++) {
				html_type += "<li>" + res.types[i].name + "</li>"
			}
			html_type += "</ul>";

			html_height += "<h3>Height<p>";
			html_height += res.height;
			html_height += "</p></h3>";

			html_weight += "<h3>Weight<p>";
			html_weight += res.weight;
			html_weight += "</p></h3>";

			$('.name').html("<h2>" + res.name + "</h2>");
			$('.pic').html('<img id=' + i + ' src="http://pokeapi.co/media/img/' + x + '.png">')
			$('.type').html(html_type);
			$('.height').html(html_height);
			$('.weight').html(html_weight);
		}, "json");
	})
});