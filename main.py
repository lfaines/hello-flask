from flask import Flask

app = Flask(__name__)
app.config['Debug'] = True

@app.route("/")
def index():
    return "Hello World"

app.run()