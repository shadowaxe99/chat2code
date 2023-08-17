import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/api/data')
def get_data():
    data = {'name': 'John', 'age': 30}
    return flask.jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)