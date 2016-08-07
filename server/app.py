from flask import Flask, request
import logging, time
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/android", methods=['POST'])
def connect():
    logger = logging.getLogger('tcpserver')
    error = None
    # execute this only if the android has done a POST method
    if request.method == 'POST':
        # get json passed from android
        content = request.get_json(silent=True)
        app.logger.info("JSON Received. " + time.strftime("%Y-%m-%d %H:%M"))
        # print json passed from android
        ## either this
        print content
        ## or this
        app.logger.info(content)
        # returns the response status code
        # if all is good this is 200, else can vary - 404, 500, etc.
        return "Received data from Android to server"
    else:
        error = 'JSON not received..' + time.strftime("%Y-%m-%d %H:%M")
        app.logger.error(error)
        return error

if __name__ == "__main__":
    # start Flask app on localhsot with port 5000
    app.run(host="127.0.0.1", port=5000)