from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, resources={r"/*":{'origins' : '*'}})
# CORS(app, resources={r"/*":{'origins' : 'http://localhost:8080', "allow_headers"  : "Access-Control-Allow-Origin" }})


@app.route('/', methods=['GET'])
def greetings():
    return("Hello, world !")

@app.route('/shark', methods=['GET'])
def shark():
    return("Hello this wendi")

GAMES = [
    {
        'title' : '2k21',
        'genre' : 'sports',
        'played' : True
    },
    {
        'title' : 'Evil within',
        'genre' : 'horror',
        'played' : True
    },
    {
        'title' : 'The Last of us',
        'genre' : 'survival',
        'played' : False
    },
    {
        'title' : 'days gone',
        'genre' : 'horror',
        'played' : True
    },
    {
        'title' : 'Mario',
        'genre' : 'Retro',
        'played' : False
    },
]

# The GET route handler
@app.route('/games', methods=['GET'])
def all_games():
    return jsonify({
        'games' : GAMES,
        'status' : 'success'
    })


if __name__ == '__main__':
    app.run(debug=True)