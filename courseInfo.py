import course
import schedule_maker

math_19a = course.Course(dptmnt='MATH', dptmnt_num='19A', course_title='Calculus for Science, Engineering, and Mathematics', num_credits=5, incoming_prereqs=[], quarters=[], profs=[])
math_19b = course.Course(dptmnt='MATH', dptmnt_num='19B', course_title='Calculus for Science, Engineering, and Mathematics', num_credits=5, incoming_prereqs=[math_19a], quarters=[], profs=[])
am_10 = course.Course(dptmnt='AM', dptmnt_num='10', course_title='Mathematical Methods for Engineers I', num_credits=5, incoming_prereqs=[], quarters=[], profs=[])
am_20 = course.Course(dptmnt='AM', dptmnt_num='20', course_title='Mathematical Methods for Engineers II', num_credits=5, incoming_prereqs=[math_19b, am_10], quarters=[], profs=[])
am_30 = course.Course(dptmnt='AM', dptmnt_num='30', course_title='Multivariate Calculus for Engineers', num_credits=5, incoming_prereqs=[am_10, math_19b], quarters=[], profs=[])
cse_20 = course.Course(dptmnt='CSE', dptmnt_num='20', course_title='Beginning Programming in Python', num_credits=5, incoming_prereqs=[], quarters=[], profs=[])
cse_30 = course.Course(dptmnt='CSE', dptmnt_num='30', course_title='Programming Abstractions: Python', num_credits=7, incoming_prereqs=[cse_20, math_19a], quarters=[], profs=[])
cse_12 = course.Course(dptmnt='CSE', dptmnt_num='12', course_title='Computer Systems and Assembly Language and Lab', num_credits=7, incoming_prereqs=[cse_20], quarters=[], profs=[])
cse_13s = course.Course(dptmnt='CSE', dptmnt_num='13S', course_title='Computer Systems and C Programming', num_credits=7, incoming_prereqs=[cse_12], quarters=[], profs=[])
cse_16 = course.Course(dptmnt='CSE', dptmnt_num='16', course_title='Applied Discrete Mathematics', num_credits=5, incoming_prereqs=[math_19a], quarters=[], profs=[])
phys_5a = course.Course(dptmnt='PHYS', dptmnt_num='5A/L', course_title='Introduction to Physics I', num_credits=6, incoming_prereqs=[math_19b], quarters=[], profs=[])
phys_5c = course.Course(dptmnt='PHYS', dptmnt_num='5C/N', course_title='Introduction to Physics III', num_credits=6, incoming_prereqs=[phys_5a], quarters=[], profs=[])
phys_5b = course.Course(dptmnt='PHYS', dptmnt_num='5B/M', course_title='Introduction to Physics II', num_credits=6, incoming_prereqs=[phys_5a,], quarters=[], profs=[])
cse_100 = course.Course(dptmnt='CSE', dptmnt_num='100/L', course_title='Logic Design', num_credits=7, incoming_prereqs=[cse_12], quarters=[], profs=[])
cse_101 = course.Course(dptmnt='CSE', dptmnt_num='101', course_title='Introduction to Data Structures and Algorithms', num_credits=5, incoming_prereqs=[cse_12, cse_13s, cse_16, math_19b], quarters=[], profs=[])
cse_107 = course.Course(dptmnt='CSE', dptmnt_num='107', course_title='Probability and Statistics for Engineers', num_credits=5, incoming_prereqs=[cse_16, am_30], quarters=[], profs=[])
cse_120 = course.Course(dptmnt='CSE', dptmnt_num='120', course_title='Computer Architecture', num_credits=5, incoming_prereqs=[cse_12, cse_13s], quarters=[], profs=[])
cse_185e = course.Course(dptmnt='CSE', dptmnt_num='185E', course_title='Technical Writing for Computer Science and Engineering', num_credits=5, incoming_prereqs=[cse_12], quarters=[], profs=[])
ece_101 = course.Course(dptmnt='ECE', dptmnt_num='101/L', course_title='Introduction to Electronic Circuits', num_credits=7, incoming_prereqs=[phys_5c, am_20], quarters=[], profs=[])
cse_121 = course.Course(dptmnt='CSE', dptmnt_num='121', course_title='Embedded System Design', num_credits=7, incoming_prereqs=[cse_12, cse_100, cse_13s, ece_101, phys_5c], quarters=[], profs=[])
ece_103 = course.Course(dptmnt='ECE', dptmnt_num='103/L', course_title='Signals and Systems', num_credits=7, incoming_prereqs=[ece_101, am_20], quarters=[], profs=[])

CE = [math_19a, math_19b, am_10, am_20, am_30, cse_20, cse_30, cse_12, cse_13s, cse_16,phys_5a, 
      phys_5c, phys_5b, cse_100, cse_101, cse_107, cse_120, cse_185e, ece_101, cse_121, ece_103]

CS = []

schedule_maker.create_schedule(CE, [cse_20, cse_30, math_19a, math_19b, am_10, am_20, am_30, cse_12, cse_13s, cse_16, phys_5a, phys_5b, phys_5c, cse_100, cse_107, cse_101, cse_120, ece_101], 3)