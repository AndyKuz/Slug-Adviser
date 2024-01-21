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
from course import Course
from courseInfo import get_courseInfo

app = Flask(__name__)
CORS(app)
CORS(app, resources={r"/api/*": {"origins": "*"}})
FRONT_END_DATA = None #for now
json_file_path = "./output.json"

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
        FRONT_END_DATA = request.get_json()
        
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


class AlgoInfo:
    def __init__(self, userPref):
        self.courses_passed = list(set(ApIbConverter(userPref) + userPref.coursesTaken))
        self.min_hours = userPref.minHoursWork
        self.max_hours = userPref.maxHoursWork
        self.min_credits = userPref.minCreditsQuarter
        self.max_credits = userPref.maxCreditsQuarter

    def get_courses_passed(self):
        return self._courses_passed

    def get_min_hours(self):
        return self._min_hours

    def get_max_hours(self):
        return self._max_hours

    def get_min_credits(self):
        return self._min_credits

    def get_max_credits(self):
        return self._max_credits

def ApIbConverter(userPref):
    # print("ENTERED AP IB CONVERTER METHOD")
    
    userPreferences = parse_json(FRONT_END_DATA)
    
    APScore3 = userPref.APScore3
    APScore4 = userPref.APScore4
    APScore5 = userPref.APScore5


    apCourses = APScore3 + APScore4 + APScore5
    # print("AP COURSES: ", apCourses)
    coursesEligible = []
    courseInfoDict = get_courseInfo()

    for courseIter in apCourses:
        # print("COURSEITER: ", courseIter)
        if courseIter ==  'AP Art History': 
            pass
        elif courseIter ==  'AP Biology':
            # coursesEligible.append()
            # coursesEligible.append(bioTwentyB)
            pass #till bio classes are released
        elif courseIter ==  'AP Calculus AB':
            if courseIter in APScore3:
                coursesEligible.append(courseInfoDict['math_3'])
                # coursesEligible.append(amThree)
            else:
                coursesEligible.append(courseInfoDict['math_3'])
                # coursesEligible.append(amThree)
                # coursesEligible.append(mathElevenA)
                coursesEligible.append(courseInfoDict['math_19a'])
        elif courseIter == 'AP Calculus BC':
            if courseIter in APScore3:
                coursesEligible.append(courseInfoDict['math_3'])
                # coursesEligible.append(amThree)
                # coursesEligible.append(mathElevenA)
                coursesEligible.append(courseInfoDict['math_19a'])
            else:
                coursesEligible.append(courseInfoDict['math_3'])
                # coursesEligible.append(amThree)
                # coursesEligible.append(mathElevenA)
                # coursesEligible.append(mathElevenB)
                coursesEligible.append(courseInfoDict['math_19a'])
                coursesEligible.append(courseInfoDict['math_19b'])
        elif courseIter ==  'AP Computer Science A':
            # coursesEligible.append(cseTen)
            # coursesEligible.append(cseFiveJ)
            pass
        elif courseIter ==  'AP Computer Science Principles':
            # coursesEligible.append(cseTen)
            pass
        elif courseIter ==  'AP Macroeconomics':
            # coursesEligible.append(econTwo)
            pass
        elif courseIter ==  'AP Microeconomics':
            # coursesEligible.append(econOne)
            pass
        elif courseIter ==  'AP Physics C: Electricity and Magnetism':
            # coursesEligible.append(courseInfoDict['phys_6a']) #'phys_6a'
            # coursesEligible.append(courseInfoDict['phys_6c']) #'phys_6c'
            coursesEligible.append(courseInfoDict['phys_5a']) #'phys_5a'
            coursesEligible.append(courseInfoDict['phys_5c']) #'phys_5c'
        elif courseIter ==  'AP Physics C: Mechanics':
            # coursesEligible.append(courseInfoDict['phys_6a']) #'phys_6a'
            # coursesEligible.append(courseInfoDict['phys_6c']) #'phys_6c'
            coursesEligible.append(courseInfoDict['phys_5a']) #'phys_5a'
            coursesEligible.append(courseInfoDict['phys_5c']) #'phys_5c'
        elif courseIter ==  'AP Psychology':
            # coursesEligible.append(psychOne)
            pass
        elif courseIter ==  'AP Statistics':
            # coursesEligible.append(statFive)
            # coursesEligible.append(psychTwo)
            # coursesEligible.append(socThreeB)
            pass
    return list(set(coursesEligible))

if __name__ == '__main__':
    app.run(debug=True)

