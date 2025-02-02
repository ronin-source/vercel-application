import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load data
with open('students-marks-api\marks.json') as f:
    data = json.load(f)

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')
    result = {"marks": []}
    
    # Create a dictionary for faster lookup
    name_to_marks = {entry['name']: entry['marks'] for entry in data}
    
    for name in names:
        result['marks'].append(name_to_marks.get(name, None))  # Return None if name not found

    return jsonify(result)

if __name__ == '__main__':
    app.run()
