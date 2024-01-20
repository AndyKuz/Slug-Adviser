from digraph import Digraph
from course import Course

def create_digraph(courses_list):
    dg = Digraph() 
    for c in courses_list:
        if not c.incoming_prereqs:
            dg.add_leaf_node(c)
        for prereq in c.incoming_prereqs:
            dg.add_edge(prereq, c)
    return dg


# CS MAJOR LOWER DIV TEST
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

dg = create_digraph(course_list)
for i in range(1, 10):
    chosen_classes = dg.choose_quarter(2, 10, 12, 0, 100)
    if chosen_classes == -1:
        exit()
    print("Quarter Schedule:")
    for c in chosen_classes:
        print("     ", c.dptmnt, c.dptmnt_num)