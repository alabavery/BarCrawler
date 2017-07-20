from flask import Flask, render_template, request, jsonify
from json import loads as json_loads
from datetime import datetime

import config

app = Flask(__name__)


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html',
    					title='ChiBarCrawler | Find Music in Chicago Bars'
                  		)

json_file = open(config.ARTIST_FILE_PATH, 'r')
artist_data = json_loads(json_file.read())
json_file.close()

def military_to_pretty_time(military_time):
	if int(military_time[3:5]) > 0:
		minute = ":" + military_time[3:5]
	else:
		minute = ""

	if int(military_time[:2]) > 12:
		suffix = 'pm'
		hour = int(military_time[:2]) - 12
	else:
		suffix = 'am'
		hour = int(military_time[:2])
	return str(hour) + minute + suffix


def prettify_dates_and_times(show_data):
	for day in show_data:
		dt = datetime.strptime(day[0], "%Y-%m-%d")
		day[0] = dt.strftime("%A %B %d")

		for show in day[1]:
			if show['time']:
				show['time'] = military_to_pretty_time(show['time'])
			else:
				show['time'] = "--"


VENUE_WEBSITES = {
	'Empty Bottle':'http://emptybottle.com/',
	'Schubas':'http://www.lh-st.com/',
	'Lincoln Hall':'http://www.lh-st.com/',
	'Beat Kitchen':'http://www.beatkitchen.com/',
	'Subterranean':'http://www.subt.net/',
	'Quenchers':'http://www.quenchers.com/',
	'The Burlington':'https://www.facebook.com/TheBurlington/',
	'Bottom Lounge':'https://bottomlounge.com/',
	'Coles':'https://www.facebook.com/coleschicago/',
	'The Hideout':'http://www.hideoutchicago.com/',
	'Thalia Hall':'http://thaliahallchicago.com/#!/'
}


@app.route("/shows")
def shows():

	json_file = open(config.SONGKICK_FILE_PATH, 'r')
	show_data = json_loads(json_file.read())
	json_file.close()

	prettify_dates_and_times(show_data)
	return render_template('shows.html',
						title='Shows | ChiBarCrawler',
						show_data=show_data,
						venue_websites=VENUE_WEBSITES
						)


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
