from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
#127.0.0.1:port/
#static Pages
def hello_world():
    return "Hello World"
#Dynamic Pages
@app.route("/<name>")
def hello_name(name):
    return " Welcome " + name

@app.route("/html")
def html_rendering():
    return render_template ("ui_designing.html")

if __name__ == "__main__" :
    app.run(port=8080,debug=True,host = "127.0.7.8")
