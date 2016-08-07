from pymongo import MongoClient
from flask import *
from bson import json_util, ObjectId
import json

# Create simple flask app
app = Flask(__name__)
# To make sure the session is secure
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
# connect to mongo db
connection = MongoClient()
# set the db and collection
db = connection.secfilter1
requests = db.requests
threats = db.threats

# Route for /api, that gives the first 20 requests on startup
@app.route('/api', methods=['GET'])
def get():
    idb = threats
    requests = list(idb.find())[-20::]
    requests_sanitized = json.loads(json_util.dumps(requests))
    return jsonify({"threats":requests_sanitized})

# route to get the new requests after a particular request
@app.route('/api/<last>', methods=['GET'])
def more(last):
    idb = threats
    requests = list(idb.find({"_id": {"$gt": ObjectId(last)}}))[:20]
    requests_sanitized = json.loads(json_util.dumps(requests))
    return jsonify({"threats":requests_sanitized})


# route to view the details of an request after clicking on it
@app.route('/threats/<id>', methods=['GET'])
def request(id):
    idb = threats
    requests = list(idb.find({"_id": ObjectId(id)}))
    request_sanitized = json.loads(json_util.dumps(requests[0]))
    return render_template("threat.html",threat=request_sanitized)

# route route, renders the index.html template
@app.route('/')
def root():
    return render_template("index.html")

# run the app on 0.0.0.0:5050
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5050,debug=True,threaded=True)
