from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/saveData', methods=['POST'])
def save_data():
    try:
        data = request.get_json()
        # Process and handle the data received from the frontend
        print('Received data from frontend:', data)
        return jsonify({'message': 'Data received successfully'}), 200
    except Exception as e:
        print('Error processing data:', str(e))
        return jsonify({'error': 'Failed to process data'}), 500

if __name__ == '__main__':
    app.run(debug=True)
