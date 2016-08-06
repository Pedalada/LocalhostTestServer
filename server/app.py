from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/android")
def connect():
    
    return "Hello World!"

if __name__ == "__main__":
    # start Flask app on localhsot with port 5000
    app.run(host="127.0.0.1", port=5000)