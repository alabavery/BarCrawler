$(document).ready(function(){
	$('.expand-spotify').click(function() {
		var that = this;
		$.getJSON($SCRIPT_ROOT + '/_expand_show', {
			artist_id: $(that).attr('artist-id')
		}, function(artist_info) {
			var spotify_play_uri = artist_info['spotify_track_id']
			if(spotify_play_uri) { // possible that we could not find the artist on spotify and will return null
				$(that).parent().append('<iframe src="https://open.spotify.com/embed?uri=spotify:\
					track:'+spotify_play_uri+'"</iframe>');
				$(that).remove();
			} else {
				$(that).text("sorry, we couldn't find this artist on spotify.");
			}
		});
		return false;
	});
});