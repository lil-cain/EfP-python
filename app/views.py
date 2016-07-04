import flask, json, functools, datetime
from app import app

def json_response(data_structure, headers=None):
    if headers is None:
        headers = dict()
    headers['Content-Type'] = 'application/json'
    return (json.dumps(data_structure), 200, headers)

@app.route("/greet/<string:name>", methods=["GET"])
def greet(name):
    if name in ['Gemma']:
        output = "Hello %s, you're looking good!" % name
    else:
        output = "Hello %s, nice to meet you!" % name
    return json_response({'response': output})

@app.route("/greet/", methods=["GET"])
def greet_who():
    return json_response({'response': "You need to tell me your name"})

@app.route("/count/<string:word>", methods=["GET"])
def count(word):
    return json_response({'count': len(word)})

@app.route("/count/")
def count_what():
    return json_response({'response': 'No string provided'})

@app.route("/quote/", methods=["GET"])
def quote():
    request = json.loads(flask.request.data.decode())
    comment = request['who'] + ' said ' + '"' + request['quote'] + '"'
    return json_response({'comment': comment})
    
@app.route("/madlib/", methods=["GET"])
def madlib():
    request = json.loads(flask.request.data.decode())
    return json_response({'madlib': "Do you %s your %s %s %s? That's a bit mad" %
                      (request['verb'], request['adjective'], request['noun'],
                       request['adverb'])})

@app.route("/math/", methods=["GET"])
def do_basic_math():
    numbers = json.loads(flask.request.data.decode())
    string_numbers = [str(num) for num in numbers]
    addition = "%s = %d" % (' + '.join(string_numbers), sum(numbers))
    subtraction = "%s = %d" % (' - '.join(string_numbers), functools.reduce(lambda x, y: x -y, numbers))
    multiplication = "%s = %d" % (' * '.join(string_numbers), functools.reduce(lambda x, y: x * y, numbers))
    division = "%s = %0.6f" % (' / '.join(string_numbers), functools.reduce(lambda x, y: float(x) / float(y), numbers))
    return json_response({'addition': addition, 'subtraction': subtraction, 'multiplication': multiplication, 'division': division})

@app.route("/retirement/",methods=["GET"])
def retirement_data():
    request_data = json.loads(flask.request.data.decode())
    current_year = datetime.datetime.now().year
    years_till_retirement = request_data['retirementAge'] - request_data['age']
    return json_response({'yearsTillRetirement': years_till_retirement,
                       'retirementYear': current_year + years_till_retirement})
