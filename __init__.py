from flask import Flask, render_template

app = Flask(__name__)


@app.route("/index")
@app.route("/")
def hello():
    return render_template('base.html',
                  title='BarCrawler | Find Music in Chicago Bars',
                  )




if __name__ == "__main__":
    app.run()
