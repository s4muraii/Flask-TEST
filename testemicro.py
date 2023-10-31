from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return "<h1>Ola Senai</h1>"

@app.route("/teste")
def teste():
    return "<h1>Teste</h1>"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")