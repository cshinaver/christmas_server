from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/assignments/assign1.html")
def assign1():
    return render_template('assign1.html')

if __name__ == "__main__":
    app.run()
