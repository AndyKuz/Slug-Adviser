# from flask import Flask, request, jsonify
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# @app.route('/saveData', methods=['POST'])
# def save_data():
#     try:
#         data = request.get_json()
#         # Process and handle the data received from the frontend
#         print('Received data from frontend:', data)
#         print("\n")
#         return jsonify({'message': 'Data received successfully'}), 200
#     except Exception as e:
#         print('Error processing data:', str(e))
#         return jsonify({'error': 'Failed to process data'}), 500

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, request, jsonify
from flask_cors import CORS
from studentpreferences import StudentPreferences
import json

app = Flask(__name__)
CORS(app)

json_file_path = "./SampleClasses.json"

with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)
    
def get_plan_data():
    return(data.get('planData'))

@app.route('/api/plan-data', methods=['GET'])
def plan_data():
    try:
        data = get_plan_data()
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': 'Failed to fetch plan data'}), 500

@app.route('/saveData', methods=['POST'])
def save_data():
    try:
        data = request.get_json()
        
        # Process and handle the data received from the frontend
        print('Received data from frontend:', data)
        print("\n")
        output = get_plan_data()
        return jsonify(output), 200
    except Exception as e:
        print('Error processing data:', str(e))
        return jsonify({'error': 'Failed to process data'}), 500

def parse_json(json_data):
    # Parse the JSON data
    data = json.loads(json_data)

    # Extracting information and assigning to variables
    major = data.get("Major", "")
    courses_taken = data.get("CoursesTaken", [])
    ap_scores_3 = data.get("APScores3", [])
    ap_scores_4 = data.get("APScores4", [])
    ap_scores_5 = data.get("APScores5", [])
    min_hours = int(data.get("MinHoursPerWeek", 0))
    max_hours = int(data.get("MaxHoursPerWeek", 0))
    min_credits = int(data.get("MinCredits", 0))
    max_credits = int(data.get("MaxCredits", 0))
    current_year = data.get("CurrentYear", "")


    userPref = StudentPreferences(minHoursWork=min_hours, maxHoursWork=max_hours, 
                                  minCreditsQuarter=min_credits, maxCreditsQuarter=max_credits, 
                                  APScore3=ap_scores_3, APScore4=ap_scores_4, APScore5=ap_scores_5)
    
    return userPref
    

if __name__ == '__main__':
    app.run(debug=True)

