from flask import Flask, render_template
from json import loads as json_loads

app = Flask(__name__)


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html',
    					title='ChiBarCrawler | Find Music in Chicago Bars'
                  		)


json_file = open("json_file.json", 'r')
show_data = json_loads(json_file.read())
json_file.close()
@app.route("/shows")
def shows():
	return render_template('shows.html',
						title='Shows | ChiBarCrawler',
						show_data=show_data
						)


@app.route("/spotify-play")
def spotify_play(song_id):
	return render_template('spotify_play_button.html',
						title='Spotify Play',
						song_id=song_id
						)


if __name__ == "__main__":
    app.run(debug=True)
