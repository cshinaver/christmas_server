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

if __name__ == "__main__":
    app.run()
