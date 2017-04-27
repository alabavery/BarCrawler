from flask import Flask, render_template

app = Flask(__name__)


@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html',
    					title='ChiBarCrawler | Find Music in Chicago Bars'
                  		)


@app.route("/shows")
def shows():
	return render_template('shows.html',
						title='Shows | ChiBarCrawler'
				)


if __name__ == "__main__":
    app.run()
