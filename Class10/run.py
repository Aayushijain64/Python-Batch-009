from flask import Flask, render_template
from imdb import show_movie

app = Flask(__name__)

@app.route("/")
def func():
    list1 = show_movie()
    return render_template("index.html",data = list1)

if __name__ == "__main__" :
    app.run(debug =True, port=4545)