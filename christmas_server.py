from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


# Assignments
@app.route("/assignments/assign1.html")
def assign1():
    return render_template('assign1.html')


@app.route("/assignments/assign2.html")
def assign2():
    return render_template('assign2.html')


@app.route("/assignments/assign3.html")
def assign3():
    return render_template('assign3.html')


@app.route("/assignments/assign4.html")
def assign4():
    return render_template('assign4.html')


@app.route("/assignments/assign5.html")
def assign5():
    return render_template('assign5.html')


@app.route("/assignments/assign6.html")
def assign6():
    return render_template('assign6.html')


@app.route("/assignments/assign7.html")
def assign7():
    return render_template('assign7.html')


if __name__ == "__main__":
    app.run()
