
from flask import Flask, jsonify, request
import logging
import json 
import time
import mymodule
import phototagModel

try:
    from flask_cors import CORS  # The typical way to import flask-cors
except ImportError:
    # Path hack allows examples to be run without installation.
    import os
    parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.sys.path.insert(0, parentdir)

    from flask_cors import CORS


app = Flask('FlaskCorsAppBasedExample')
app.config['CORS_HEADERS'] = 'Content-Type'

logging.basicConfig(level=logging.INFO)

CORS(app, resources=r'/api/*', allow_headers='*')



@app.route("/")
def helloML():
    
    return '''<h1>Machine Learning Server</h1>
    <p>the server is under /flaskMLserver/FlaskPhotoTag '''


@app.route("/api/ML/photoTag/create", methods=['POST'])
def phototag():

    print (request.data)

    dataIn = request.get_json()
    data = dataIn[u'id']

    print (dataIn)
    print (data)

    
    predicted = phototagModel.doPrediction(data)

    print "coming back from the phototagModel", predicted
    
    return jsonify({ 'predicted':predicted })


if __name__ == "__main__":
    app.run()
    # app.run(debug=True)
