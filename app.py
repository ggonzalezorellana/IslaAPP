from flask import Flask, jsonify
from utils.building import divide_teams
from utils.db_get.get_info import get_available_players

app = Flask(__name__)

@app.route('/build-teams')
def build_teams():
    # Code

    players = get_available_players()
    
    player_list = []
    for player in players:
        player_dict = {
            'name': player[0],
            'gender': player[1],
            'quality': player[2],
            'will_play': bool(player[3])
        }
        player_list.append(player_dict)

    # return the list of players as JSON
    return jsonify(player_list)

if __name__ == '__main__':
    app.run(debug=True)