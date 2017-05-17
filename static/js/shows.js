$(document).ready(function(){
	$('#show-container').on('click', ".show-tile", function() {
		$(this).children().toggle();
		$(this).toggleClass('col-sm-3 col-sm-12');
   
		var that = this;
		$.getJSON($SCRIPT_ROOT + '/_expand_show', {
			artist_id: $(that).attr('artist-id')
		}, function(artist_info) {
			var spotify_play_uri = artist_info['spotify_track_id']
			var spotify_image = artist_info['image']

			if(spotify_play_uri) { // possible that we could not find the artist on spotify and will return null
				$(that).find('.spotify-play').append('<iframe src="https://open.spotify.com/embed?uri=spotify:\
					track:'+spotify_play_uri+'"</iframe>');
				$(that).find('.expanded-show-image').attr('src', spotify_image);
			} else {
				alert("Sorry we either couldn't find or couldn't verify that artist on Spotify.");
			}
		});
		return false;
	});
});