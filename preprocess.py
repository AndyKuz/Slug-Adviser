# from flask import Flask, request, jsonify
# from flask_cors import CORS

from flask import Flask, request, jsonify
from flask_cors import CORS
from studentpreferences import StudentPreferences
import json
import courseInfo
import schedule_maker
import py2jsonconvert

app = Flask(__name__)
CORS(app)

# json_file_path = "./output.json"

# with open(json_file_path, 'r') as json_file:
#     data = json.load(json_file)
    
# def get_plan_data():
#     return(data.get('planData'))

# @app.route('/api/plan-data', methods=['GET'])
# def plan_data():
#     try:
#         data = get_plan_data()
#         return jsonify(data)
#     except Exception as e:
#         return jsonify({'error': 'Failed to fetch plan data'}), 500

@app.route('/saveData', methods=['POST'])
def save_data():
    # try:
        user_data = request.get_json()
        print(user_data)
        user_pref = parse_user_pref(user_data)
        print(user_pref)
        
        print("computing...")
        
        major_courses = []
        placeholder_courses = []
        if user_pref.major == "Computer Science":
            major_courses = courseInfo.get_cs_courses()
            placeholder_courses = courseInfo.get_cs_placeholders()
        elif user_pref.major == "Computer Engineering":
            major_courses = courseInfo.get_ce_courses()
            placeholder_courses = courseInfo.get_ce_placeholder()
        else:
            print("Error major not recognized")
            
        print("?")
        college_year = 0
        if user_pref.currentYear == "Freshman":
            college_year = 0
        elif user_pref.currentYear == "Sophomore":
            college_year = 1
        elif user_pref.currentYear == "Junior":
            college_year = 2
        elif user_pref.currentYear == "Senior":
            college_year = 3
        
        print("??")
        print("major courses: ", major_courses)
        print("user")
        quarters = schedule_maker.create_schedule(major_courses, user_pref.get_courses_taken(), college_year, placeholder_courses)
        print(quarters)
        plan_data = py2jsonconvert.convert(quarters)
        
        print("finished preprocess:")
        print("college year: ", college_year)
        print("min hours: ", user_pref.get_min_hours_work(), " max hours: ", user_pref.get_max_hours_work)
        print("major courses: ", major_courses)
        print("courses_taken: ", user_pref.get_courses_taken())

        
        # Process and handle the data received from the frontend
        print('Received data from frontend:', user_data)
        print("\n")
        print("Print Plan Out")
        print(plan_data)
        return jsonify(plan_data), 200
    # except Exception as e:
    #     print('Error processing data:', str(e))
    #     return jsonify({'error': f'Failed to process data {str(e)}'}), 500

def parse_user_pref(data):
    # Parse the JSON data
    # data = json.loads(json_data)

    # Extracting information and assigning to variables
    major = data.get("Major", "")
    courses_taken = data.get("CoursesTaken", []) #fix course issue
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
                                  major=major, coursesTaken=courses_taken, currentYear=current_year, 
                                  APScore3=ap_scores_3, APScore4=ap_scores_4, APScore5=ap_scores_5)
    
    return userPref


# class AlgoInfo:
#     def __init__(self, userPref):
#         self.courses_passed = list(set(ApIbConverter(userPref) + userPref.coursesTaken))
#         self.min_hours = userPref.minHoursWork
#         self.max_hours = userPref.maxHoursWork
#         self.min_credits = userPref.minCreditsQuarter
#         self.max_credits = userPref.maxCreditsQuarter

#     def get_courses_passed(self):
#         return self._courses_passed

#     def get_min_hours(self):
#         return self._min_hours

#     def get_max_hours(self):
#         return self._max_hours

#     def get_min_credits(self):
#         return self._min_credits

#     def get_max_credits(self):
#         return self._max_credits
def main():
    app.run(debug=True)

main()