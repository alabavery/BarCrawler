from flask import Flask, render_template, request, jsonify
from json import loads as json_loads
import config

app = Flask(__name__)


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html',
    					title='ChiBarCrawler | Find Music in Chicago Bars'
                  		)


json_file = open(config.SONGKICK_FILE_PATH, 'r')
show_data = json_loads(json_file.read())
json_file.close()
@app.route("/shows")
def shows():
	return render_template('shows.html',
						title='Shows | ChiBarCrawler',
						show_data=show_data
						)

json_file = open(config.ARTIST_FILE_PATH, 'r')
artist_data = json_loads(json_file.read())
json_file.close()
@app.route('/_expand_show')
def expand_show():
	artist_id = str(request.args.get('artist_id', '0', type=str))
	artist_info = [artist_dict for artist_dict in artist_data if str(artist_dict['songkick_id']) == artist_id][0]
	return jsonify(artist_info)


@app.route("/spotify-play")
def spotify_play(song_id):
	return render_template('spotify_play_button.html',
						title='Spotify Play',
						song_id=song_id
						)

