from flask import Flask, jsonify
import json
import os

app = Flask(__name__)

# Define the path to the backend file
DATA_FILE = os.path.join(os.path.dirname(__file__), "data.json")

@app.route('/api', methods=['GET'])
def get_data():
    try:
        # Read data from the file
        with open(DATA_FILE, 'r') as file:
            data = json.load(file)
        return jsonify(data), 200
    except FileNotFoundError:
        return jsonify({"error": "Data file not found"}), 404
    except json.JSONDecodeError:
        return jsonify({"error": "Error decoding JSON"}), 500


if __name__ == '__main__':
    app.run(debug=True)
