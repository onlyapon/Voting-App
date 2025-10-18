from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Root route for testing
@app.route('/')
def home():
    return jsonify({'message': 'RMEDUSC Voting API Server is running'})

# Error handlers
@app.errorhandler(404)
def not_found(e):
    return jsonify({'error': 'Route not found'}), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({'error': 'Internal server error'}), 500

# File to store votes
VOTES_FILE = 'votes.json'

def load_votes():
    if os.path.exists(VOTES_FILE):
        with open(VOTES_FILE, 'r') as f:
            return json.load(f)
    return {'regular_votes': [], 'rme10_votes': []}

def save_votes(votes):
    with open(VOTES_FILE, 'w') as f:
        json.dump(votes, f, indent=2)

# API Routes
@app.route('/api/votes/regular', methods=['POST'])
def submit_regular_vote():
    vote = request.json
    vote['timestamp'] = datetime.now().isoformat()
    
    votes = load_votes()
    votes['regular_votes'].append(vote)
    save_votes(votes)
    
    return jsonify({'message': 'Vote recorded successfully'})

@app.route('/api/votes/regular', methods=['GET'])
def get_regular_votes():
    votes = load_votes()
    return jsonify(votes['regular_votes'])

@app.route('/api/votes/rme10', methods=['POST'])
def submit_rme10_vote():
    vote = request.json
    vote['timestamp'] = datetime.now().isoformat()
    
    votes = load_votes()
    votes['rme10_votes'].append(vote)
    save_votes(votes)
    
    return jsonify({'message': 'RME 10 vote recorded successfully'})

@app.route('/api/votes/rme10', methods=['GET'])
def get_rme10_votes():
    votes = load_votes()
    return jsonify(votes['rme10_votes'])

if __name__ == '__main__':
    # Create votes.json if it doesn't exist
    if not os.path.exists(VOTES_FILE):
        save_votes({'regular_votes': [], 'rme10_votes': []})
    
    print('Starting RMEDUSC Voting API Server...')
    print('Server will be available at http://localhost:5001')
    print('API Routes:')
    print('  GET  / - Test if server is running')
    print('  POST /api/votes/rme10 - Submit RME 10 vote')
    print('  GET  /api/votes/rme10 - Get all RME 10 votes')
    print('  POST /api/votes/regular - Submit regular vote')
    print('  GET  /api/votes/regular - Get all regular votes')
    
    app.run(debug=True, port=5001, host='0.0.0.0')