import flask, json
from app import app

@app.route("/greet/<string:name>", methods=["GET"])
def greet(name):
    if name in ['Gemma']:
        output = "Hello %s, you're looking good!" % name
    else:
        output = "Hello %s, nice to meet you!" % name
    return json.dumps({'response': output})

@app.route("/greet/", methods=["GET"])
def greet_who():
    return json.dumps({'response': "You need to tell me your name"})

@app.route("/count/<string:word>", methods=["GET"])
def count(word):
    return json.dumps({'count': len(word)})

@app.route("/count/")
def count_what():
    return json.dumps({'response': 'No string provided'})

@app.route("/quote/", methods=["GET"])
def quote():
    request = json.loads(flask.request.data.decode())
    comment = request['who'] + ' said ' + '"' + request['quote'] + '"'
    return json.dumps({'comment': comment})
    
@app.route("/madlib/", methods=["GET"])
def madlib():
    request = json.loads(flask.request.data.decode())
    return json.dumps({'madlib': "Do you %s your %s %s %s? That's a bit mad" %
                      (request['verb'], request['adjective'], request['noun'],
                       request['adverb'])})
