$(document).ready(function(){
	$('.show-tile').click(function() {
		$(this).children().css('visibility', 'hidden');
		$(this).css('background-image', 'url("static/img/Parquet_Courts.jpg")');
	});
});