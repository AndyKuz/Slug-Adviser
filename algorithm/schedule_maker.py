from digraph import Digraph

def create_digraph(courses_list):
    dg = Digraph() 
    for c in courses_list:
        for prereq in c.incoming_prereqs:
            dg.add_edge(prereq, c)


# CS MAJOR LOWER DIV TEST
"""
cse_20 = Course("cse", "20", [])
math_19A = Course("math", "19A", [])
math_19B = Course("math", "19B", [math_19A])
cse_12 = Course("cse", "12", [cse_20])
cse_16 = Course("cse", "16", [math_19A, math_19B])
cse_30 = Course("cse", "30", [cse_20, math_19A])
cse_13s = Course("cse", "13s", [cse_12])
am_10 = Course("am", "10", [])
am_30 = Course("am", "30", [am_10])
ece_30 = Course("ece", "30", [])
cse_101 = Course("cse", "101", [cse_12, cse_13s, cse_16, cse_30, math_19B])

course_list = [cse_20, math_19A, math_19B, cse_12, cse_16, cse_30, cse_13s, am_10, am_30, ece_30, cse_101]
create_digraph(course_list)
"""