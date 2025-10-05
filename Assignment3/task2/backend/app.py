from flask import Flask, jsonify
from flask import request
from dotenv import load_dotenv
import os
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

from pymongo.mongo_client import MongoClient


# Create a new client and connect to the server
client = MongoClient(MONGO_URI)

db = client["test"]

collection = db['flask-tutorial']
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    # form_data = dict(request.json)
    # collection.insert_one(form_data)
    # return "data submited successfully"
    try:
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400

        # Required fields
        required_fields = ["name", "email", "password", "confirm_password"]

        # Check for missing fields
        missing_fields = [field for field in required_fields if not data.get(field)]
        if missing_fields:
            return jsonify({"error": f"Missing fields: {', '.join(missing_fields)}"}), 400

        collection.insert_one(data)
        return jsonify({"message": "Data submitted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/view')
def view():
    data = collection.find()
    data = list(data)
    for i in data:
        print(i)
        i.pop('_id')
    data = { "data" : data }
    return data
if __name__ == '__main__':
    app.run( host='0.0.0.0', port=9000, debug=True)
