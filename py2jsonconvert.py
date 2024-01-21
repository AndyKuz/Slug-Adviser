import json
from course import Quarter
from typing  import List

def convert(qlist: List[Quarter]):
    plan_data = []

    # Group quarters by year
    quarters_by_year = {}
    for quarter in qlist:
        if quarter.college_year not in quarters_by_year:
            quarters_by_year[quarter.college_year] = []
        quarters_by_year[quarter.college_year].append(quarter)

    # Create JSON format
    for year, quarters in quarters_by_year.items():
        year_data = {"year": year, "quarters": []}
        for quarter in quarters:
            quarter_data = {
                "quarter": quarter.quarter_type,
                "courses": quarter.course_list
            }
            year_data["quarters"].append(quarter_data)
        plan_data.append(year_data)

    return plan_data
    # with open('output.json', 'w') as json_file:
    #     json.dump({"planData": plan_data}, json_file, indent=4, sort_keys=False)

'''   
qtest1 = Quarter("First year", "Fall", [])
qtest2 = Quarter("First year", "Winter", ["cse 12", "cse 16"])
qtest3 = Quarter("First year", "Spring", ["cse 120", "cse 16"])
qtest4 = Quarter("Second year", "Fall", ["cse 12", "cse 16"])
qtest5 = Quarter("Second year", "Winter", ["cse 12", "cse 16"])
qtest6 = Quarter("Second year", "Spring", ["cse 12", "cse 16"])
qlist = [qtest1, qtest2, qtest3, qtest4, qtest5, qtest6]
convert(qlist)
'''