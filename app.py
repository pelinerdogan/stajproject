from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

# Set up the MongoDB client
client = MongoClient('mongodb://mongodb:27017/')
db = client['your_database']
collection = db['your_collection']
print("hi")
@app.route('/item/<item_id>', methods=['GET'])
def get_item(item_id):
    item = collection.find_one({'_id': item_id})
    if item:
        item['_id'] = str(item['_id'])  # Convert ObjectId to string
        return jsonify(item)
    else:
        return jsonify({'error': 'Item not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

