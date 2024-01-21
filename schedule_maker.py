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
    for c in courses_list:
        c.set_priority_rating()
    dg.sort_root_courses_by_outgoing()
    return dg

""" gets current school quarter
    returns:
        0 -> fall
        1 -> winter
        2 -> spring
"""
def get_current_quarter():
    today = date.today()
    
    month = today.strftime("%m")

    if int(month) >= 9 and int(month) <= 11:
        return 0
    elif int(month) == 12 or (int(month) >= 1 and int(month) <= 3):
        return 1
    elif int(month) >= 4 and int(month) <= 6:
        return 2
    
# removes already taken classes from digraph
def remove_taken_classes(dg, taken_classes):
    while taken_classes:
        for c in taken_classes:
            if c in dg.root_courses:
                dg.del_course(c)
                taken_classes.remove(c)

""" 
    creates a base 4 year academic plan
    bases it off of inputed college year and pre_taken classes
    calculates current quarter by datetime
"""
def create_schedule(course_list, taken_courses, current_year, placeholder_classes):
    dg = create_digraph(course_list)
    quarters_list = []  # list of quarter class instances representing each quarter

    remove_taken_classes(dg, taken_courses) # removes all classes already taken from digraph

    datetime_quarter = get_current_quarter()
    current_quarter_int = -1
    current_quarter_string = ""
    current_year_string = ""

    num_three_class_quarters = (len(course_list) - len(taken_courses)) + len(placeholder_classes) - 24
    quarter_three_class_start = 12 - num_three_class_quarters   # calculates when to start taking 3 classes
    for i in range(0, 12):
        # need to check up here for proper code flow, used below
        all_courses_empty = False if len(dg.all_courses) else True

        curr_num_courses = 3 if i >= quarter_three_class_start else 2

        # stores current quarter
        if i in [0, 3, 6, 9]:
            current_quarter_string = "Fall"
            current_quarter_int = 0
        if i in [1, 4, 7, 10]:
            current_quarter_string = "Winter"
            current_quarter_int = 1
        if i in [2, 5, 8, 11]:
            current_quarter_string = "Spring"
            current_quarter_int = 2
        
        # TODO:...
        # quarters_list.append(Quarter())

        # stores current college year
        if i >= 0 and i <= 2:
            current_year_string = "First year"
        elif i >= 3 and i <= 5:
            current_year_string = "Second year"
        elif i >= 6 and i <= 8:
            current_year_string = "Third year"
        elif i >= 9 and i <= 11:
            current_year_string = "Fourth year"

        # prints out header above classes
        print(current_year_string, current_quarter_string) 
        chosen_classes = -1

        # only chooses classes if the iterated year/quarter is past the actual current year/quarter
        print("current year: ", current_year)
        if current_year == 0:
            if i > datetime_quarter:
                chosen_classes = dg.choose_quarter(curr_num_courses, (5*curr_num_courses), (5*curr_num_courses)+5, 0, 100, current_quarter_int)
        elif current_year == 1:
            if i > datetime_quarter + 3:
                chosen_classes = dg.choose_quarter(curr_num_courses, (5*curr_num_courses), (5*curr_num_courses)+5, 0, 100, current_quarter_int)
        elif current_year == 2:
            if i > datetime_quarter + 6:
                chosen_classes = dg.choose_quarter(curr_num_courses, (5*curr_num_courses), (5*curr_num_courses)+5, 0, 100, current_quarter_int)
        elif current_year == 3:
            if i > datetime_quarter + 9:
                chosen_classes = dg.choose_quarter(curr_num_courses, (5*curr_num_courses), (5*curr_num_courses)+5, 0, 100, current_quarter_int)
        
        print("chosen classes: ", chosen_classes)

        course2json = []
        if all_courses_empty:    # for placeholder classes after #'d classes finish
            for i in range(0, curr_num_courses):
                if len(placeholder_classes) >= 1:
                    course2json.append(placeholder_classes[0]) # to json
                    print("     ", placeholder_classes.pop(0))  # to console
                else:
                    course2json.append(" ") # to json
                    print("     x") # to console
        elif not chosen_classes or chosen_classes == -1:
            for i in range(0, curr_num_courses):
                course2json.append(" ") # to json
                print("     x") # to console
        elif len(chosen_classes) == 1:
            course2json.append((chosen_classes[0].dptmnt + " " + chosen_classes[0].dptmnt_num)) # to json
            print("     ", chosen_classes[0].dptmnt, chosen_classes[0].dptmnt_num)  # to console
            if curr_num_courses == 2:
                if len(placeholder_classes) >= 1:
                    course2json.append(placeholder_classes[0])  # to json
                    print("     ", placeholder_classes.pop(0))  #  to console
            else:
                for i in range(0, 2):
                    if len(placeholder_classes) >= 1:
                        course2json.append(placeholder_classes[0])  # to json
                        print("     ", placeholder_classes.pop(0))  # to console
        elif len(chosen_classes) == 2 and curr_num_courses == 3:
            course2json.append((chosen_classes[0].dptmnt + " " + chosen_classes[0].dptmnt_num))   # to json
            print("     ", chosen_classes[0].dptmnt, chosen_classes[0].dptmnt_num)  # to console
            course2json.append((chosen_classes[1].dptmnt + " " + chosen_classes[1].dptmnt_num))   # to json
            print("     ", chosen_classes[1].dptmnt, chosen_classes[1].dptmnt_num)  # to console
            if len(placeholder_classes) >= 1:
                course2json.append(placeholder_classes[0])  # to json
                print("     ", placeholder_classes.pop(0))  # to console
        elif len(chosen_classes) > 1:
            for c in chosen_classes:
                course2json.append((c.dptmnt + " " + c.dptmnt_num)) # to json  
                print("     ", c.dptmnt, c.dptmnt_num)  # to console
        else:
            course2json.append(" ") # to json
            course2json.append(" ") # to json
            print("     x\n     x") # to console
        print()
        quarters_list.append(Quarter(current_year_string, current_quarter_string, course2json))
    return quarters_list
