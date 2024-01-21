from digraph import Digraph
from course import Course
from course import Quarter

from datetime import date

def create_digraph(courses_list):
    dg = Digraph() 
    for c in courses_list:
        if not c.incoming_prereqs:
            dg.add_leaf_node(c)
        for prereq in c.incoming_prereqs:
            dg.add_edge(prereq, c)
    return dg

""" gets current school quarter
    returns:
        1 -> fall
        2 -> winter
        3 -> spring
"""
def get_current_quarter():
    today = date.today()
    
    month = today.strftime("%m")

    if int(month) >= 9 and int(month) <= 11:
        return 1
    elif int(month) == 12 or (int(month) >= 1 and int(month) <= 3):
        return 2
    elif int(month) >= 4 and int(month) <= 6:
        return 3
    
# removes already taken classes from digraph
def remove_taken_classes(dg, l):
    while l:
        for c in l:
            if c in dg.root_courses:
                dg.del_course(c)
                l.remove(c)

""" 
    creates a base 4 year academic plan
    bases it off of inputed college year and pre_taken classes
    calculates current quarter by datetime
"""
def create_schedule(course_list, taken_courses, current_year):
    dg = create_digraph(course_list)
    quarters_list = []  # list of quarter class instances representing each quarter

    remove_taken_classes(dg, taken_courses) # removes all classes already taken from digraph

    current_quarter = get_current_quarter()
    current_quarter_string = ""
    current_year_string = ""

    for i in range(1, 13):
        # TODO:...
        # quarters_list.append(Quarter())

        # stores current quarter
        if i in [1, 4, 7, 10]:
            current_quarter_string = "Fall"
        if i in [2, 5, 8, 11]:
            current_quarter_string = "Winter"
        if i in [3, 6, 9, 12]:
            current_quarter_string = "Spring"

        # stores current college year
        if i >= 1 and i <= 3:
            current_year_string = "Freshman"
        elif i >= 4 and i <= 6:
            current_year_string = "Sophomore"
        elif i >= 7 and i <= 9:
            current_year_string = "Junior"
        elif i >= 10 and i <= 12:
            current_year_string = "Senior"

        # prints out header above classes
        print(current_year_string, current_quarter_string)
        chosen_classes = []

        # only chooses classes if the iterated year/quarter is past the actual current year/quarter
        if current_year == 1:
            if i > current_quarter + 0:
                chosen_classes = dg.choose_quarter(2, 10, 12, 0, 100)
        elif current_year == 2:
            if i > current_quarter + 3:
                chosen_classes = dg.choose_quarter(2, 10, 12, 0, 100)
        elif current_year == 3:
            if i > current_quarter + 6:
                chosen_classes = dg.choose_quarter(2, 10, 12, 0, 100)
        elif current_year == 4:
            if i > current_quarter + 9:
                chosen_classes = dg.choose_quarter(2, 10, 12, 0, 100)
        
        if not chosen_classes or chosen_classes == -1:   # prints placeholders if classes not chose
            print("x\nx")
        else:
            for c in chosen_classes:
                print("     ", c.dptmnt, c.dptmnt_num)
        print()

# CS MAJOR LOWER DIV TEST
"""
cse_20 = Course("cse", "20", "",  5, [])
math_19A = Course("math", "19A", "",  5, [])
math_19B = Course("math", "19B", "",  5, [math_19A])
cse_12 = Course("cse", "12", "",  5, [cse_20])
cse_16 = Course("cse", "16", "",  5, [math_19A, math_19B])
cse_30 = Course("cse", "30", "",  5, [cse_20, math_19A])
cse_13s = Course("cse", "13s", "",  7, [cse_12])
am_10 = Course("am", "10", "",  5, [])
am_30 = Course("am", "30", "",  5, [am_10])
ece_30 = Course("ece", "30", "",  5, [])
cse_101 = Course("cse", "101", "",  5, [cse_12, cse_13s, cse_16, cse_30, math_19B])

course_list = [cse_20, math_19A, math_19B, cse_12, cse_16, cse_30, cse_13s, am_10, am_30, ece_30, cse_101]
"""