from flask import Flask
from utils.building import divide_teams
from utils.db_get.get_info import get_available_players

app = Flask(__name__)

@app.route('/build-teams')
def build_teams():
    # Code

    players = get_available_players()

    

    # Return teams
    return 'Done'