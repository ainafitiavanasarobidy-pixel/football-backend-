from flask import Flask, jsonify
from flask_cors import CORS
import requests
import os
import random

app = Flask(__name__)
CORS(app)

API_KEY = "af3766a29e4f4243aed987b57bcac734"

@app.route('/predictions')
def get_data():
    headers = {'X-Auth-Token': API_KEY}
    url = "https://api.football-data.org/v4/matches"
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        output = []
        for match in data.get('matches', [])[:10]:
            h_prob = random.randint(55, 85)
            output.append({
                "home": match['homeTeam']['shortName'],
                "away": match['awayTeam']['shortName'],
                "prob": f"{h_prob}%"
            })
        return jsonify(output)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    
