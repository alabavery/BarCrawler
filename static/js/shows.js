$(document).ready(function(){
	$('#show-container').on('click', ".show-tile", function() {
		$(this).children().toggle();

		var that = this;
		$.getJSON($SCRIPT_ROOT + '/_expand_show', {
			event_id: $(that).attr('event_id')
		}, function(expanded_show) {
			var spotify_play_uri = expanded_show['spotify']
			// ignore the spotify_play_url var for now...
			// here, we want to insert/inject into the div named 'spotify-play' the html for the iframe 
			// for a spotify play button...
			// <iframe src="https://open.spotify.com/embed?uri=spotify:track:5EyR6C5JvXzPlOMzU9A2GS" width="300" height="380" frameborder="0" allowtransparency="true"></iframe>
			// change wifth and height as necessary
			// eventually, the code after 'spotify:track:' will be replaced with the ajax call...
			// for now, let's just try getting the play button in there without complicating it with ajax call
			// in any case, the infrastructure is there now.
		});
		return false;
	});
});