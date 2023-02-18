from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid


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

# The GET and POST route handler
@app.route('/games', methods=['GET', 'POST'])
def all_games():
    response_object = {'status':'success'}
    if request.method == "POST":
        post_data = request.get_json()
        GAMES.append({
            'id' : uuid.uuid4().hex,
            'title': post_data.get('title'),
            'genre': post_data.get('genre'),
            'played': post_data.get('played')})
        response_object['message'] =  'Game Added!'
    else:
        response_object['games'] = GAMES
    return jsonify(response_object)


#The PUT and DELETE route handler
@app.route('/games/<game_id>', methods =['PUT', 'DELETE'])
def single_game(game_id):
    response_object = {'status':'success'}
    if request.method == "PUT":
        post_data = request.get_json()
        remove_game(game_id)
        GAMES.append({
            'id' : uuid.uuid4().hex,
            'title': post_data.get('title'),
            'genre': post_data.get('genre'),
            'played': post_data.get('played')
        })
        response_object['message'] =  'Game Updated!'

# Removing the game to update / delete
def remove_game(game_id):
    for game in GAMES:
        if game['id'] == game_id:
            GAMES.remove(game)
            return True
    return False


if __name__ == '__main__':
    app.run(debug=True)