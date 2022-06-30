from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_word():
    return "Hello World!"

@app.route("/dojo")
def dojo():
    return "dojo"

@app.route("/say/<name>")
def say_name(name):
    return f"Hi {name}"

@app.route("/repeat/<int:repeat_times>/<msg>")
def repeat(repeat_times,msg):
    message = ""
    for i in range(repeat_times):
        message += msg + "<br>"
    return message

@app.errorhandler(404)
def message(e):
    return "Sorry! No response. Try again."

if __name__ == "__main__":
    app.run(debug=True)
