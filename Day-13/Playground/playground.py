from flask import Flask , render_template
app = Flask(__name__)


@app.route("/")
def hello():
    return "hello world"

@app.route('/play')
def threeboxes():
    return render_template("play.html",repeat = 3)


@app.route("/play/<int:repeat>")
def pushBoxes(repeat):
    return render_template("play.html",repeat = repeat)

@app.route("/play/<int:repeat>/<string:color>")
def pushBoxesAndColors(repeat,color):
    return render_template("play.html",repeat = repeat, color = color)


if __name__ == "__main__":
    app.run(debug=True)
