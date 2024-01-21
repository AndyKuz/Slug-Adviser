from course import Course
import schedule_maker

math_3 = Course(dptmnt='MATH', dptmnt_num='3', course_title='Precalculus', num_credits=5, incoming_prereqs=[], quarters=[0, 1, 2], profs=[]) #in development
math_19a = Course(dptmnt='MATH', dptmnt_num='19A', course_title='Calculus for Science, Engineering, and Mathematics', num_credits=5, incoming_prereqs=[math_3], quarters=[0, 1, 2], profs=[])
math_19b = Course(dptmnt='MATH', dptmnt_num='19B', course_title='Calculus for Science, Engineering, and Mathematics', num_credits=5, incoming_prereqs=[math_19a], quarters=[0, 1, 2], profs=[])
am_10 = Course(dptmnt='AM', dptmnt_num='10', course_title='Mathematical Methods for Engineers I', num_credits=5, incoming_prereqs=[], quarters=[0, 1, 2], profs=[])
am_20 = Course(dptmnt='AM', dptmnt_num='20', course_title='Mathematical Methods for Engineers II', num_credits=5, incoming_prereqs=[math_19b, am_10], quarters=[1, 2], profs=[])
am_30 = Course(dptmnt='AM', dptmnt_num='30', course_title='Multivariate Calculus for Engineers', num_credits=5, incoming_prereqs=[am_10, math_19b], quarters=[0, 1, 2], profs=[])
cse_20 = Course(dptmnt='CSE', dptmnt_num='20', course_title='Beginning Programming in Python', num_credits=5, incoming_prereqs=[], quarters=[0, 1, 2], profs=[])
cse_30 = Course(dptmnt='CSE', dptmnt_num='30', course_title='Programming Abstractions: Python', num_credits=7, incoming_prereqs=[cse_20, math_19a], quarters=[0, 1, 2], profs=[])
cse_12 = Course(dptmnt='CSE', dptmnt_num='12', course_title='Computer Systems and Assembly Language and Lab', num_credits=7, incoming_prereqs=[cse_20], quarters=[0, 1, 2], profs=[])
cse_13s = Course(dptmnt='CSE', dptmnt_num='13S', course_title='Computer Systems and C Programming', num_credits=7, incoming_prereqs=[cse_12], quarters=[0, 1, 2], profs=[])
cse_16 = Course(dptmnt='CSE', dptmnt_num='16', course_title='Applied Discrete Mathematics', num_credits=5, incoming_prereqs=[math_19a], quarters=[0, 1, 2], profs=[])
phys_5a = Course(dptmnt='PHYS', dptmnt_num='5A/L', course_title='Introduction to Physics I', num_credits=6, incoming_prereqs=[math_19b], quarters=[0], profs=[])
phys_5c = Course(dptmnt='PHYS', dptmnt_num='5C/N', course_title='Introduction to Physics III', num_credits=6, incoming_prereqs=[phys_5a], quarters=[1], profs=[])
phys_5b = Course(dptmnt='PHYS', dptmnt_num='5B/M', course_title='Introduction to Physics II', num_credits=6, incoming_prereqs=[phys_5a,], quarters=[2], profs=[])
cse_100 = Course(dptmnt='CSE', dptmnt_num='100/L', course_title='Logic Design', num_credits=7, incoming_prereqs=[cse_12], quarters=[0, 1, 2], profs=[])
cse_101 = Course(dptmnt='CSE', dptmnt_num='101', course_title='Introduction to Data Structures and Algorithms', num_credits=5, incoming_prereqs=[cse_12, cse_13s, cse_16, math_19b], quarters=[0, 1, 2], profs=[])
cse_102 = Course(dptmnt='CSE', dptmnt_num='102', course_title='Introduction to Analysis of Algorithms', num_credits=5, incoming_prereqs=[cse_101], quarters=[0, 1, 2], profs=[])
cse_103 = Course(dptmnt='CSE', dptmnt_num='103', course_title='Computational Models', num_credits=5, incoming_prereqs=[cse_101], quarters=[0, 1, 2], profs=[])
cse_107 = Course(dptmnt='CSE', dptmnt_num='107', course_title='Probability and Statistics for Engineers', num_credits=5, incoming_prereqs=[cse_16, am_30], quarters=[0, 1, 2], profs=[])
cse_120 = Course(dptmnt='CSE', dptmnt_num='120', course_title='Computer Architecture', num_credits=5, incoming_prereqs=[cse_12, cse_13s], quarters=[0, 1, 2], profs=[])
cse_125 = Course(dptmnt='CSE', dptmnt_num='125', course_title='Logic Design with Verilog', num_credits=7, incoming_prereqs=[cse_100, cse_120], quarters=[2], profs=[])
cse_130 = Course(dptmnt='CSE', dptmnt_num='130', course_title='Principles of Computer Systems Design', num_credits=5, incoming_prereqs=[cse_12, cse_101], quarters=[0, 1, 2], profs=[])
cse_150 = Course(dptmnt='CSE', dptmnt_num='150', course_title='Introduction to Computer Networks', num_credits=7, incoming_prereqs=[cse_12, cse_16, cse_30], quarters=[0, 1, 2], profs=[])
cse_185e = Course(dptmnt='CSE', dptmnt_num='185E', course_title='Technical Writing for Computer Science and Engineering', num_credits=5, incoming_prereqs=[cse_12], quarters=[0, 1, 2], profs=[])
ece_30 = Course(dptmnt='ECE', dptmnt_num='30', course_title='Engineering Principles of Electronics', num_credits=5, incoming_prereqs=[math_19b], quarters=[1, 2], profs=[])
ece_101 = Course(dptmnt='ECE', dptmnt_num='101/L', course_title='Introduction to Electronic Circuits', num_credits=7, incoming_prereqs=[phys_5c, am_20], quarters=[0, 1], profs=[])
cse_111 = Course(dptmnt='CSE', dptmnt_num='111', course_title='Advanced Programming', num_credits=5, incoming_prereqs=[cse_13s], quarters=[2], profs=[])
cse_121 = Course(dptmnt='CSE', dptmnt_num='121', course_title='Embedded System Design', num_credits=7, incoming_prereqs=[cse_12, cse_100, cse_13s, ece_101, phys_5c], quarters=[0, 2], profs=[])
cse_122 = Course(dptmnt='CSE', dptmnt_num='122', course_title='Introduction to VLSI Digital System Design', num_credits=5, incoming_prereqs=[cse_100, ece_101], quarters=[1], profs=[])
cse_220 = Course(dptmnt='CSE', dptmnt_num='220', course_title='Computer Architecture', num_credits=5, incoming_prereqs=[cse_120], quarters=[0, 2], profs=[])
ece_103 = Course(dptmnt='ECE', dptmnt_num='103/L', course_title='Signals and Systems', num_credits=7, incoming_prereqs=[ece_101, am_20], quarters=[0, 2], profs=[])
cse_112orcse_114a = Course(dptmnt='CSE', dptmnt_num='112 or 114A', course_title='Comparative Programming Languages', num_credits=5, incoming_prereqs=[cse_101], quarters=[0, 1, 2], profs=[])
stat_131orcse_107 = Course(dptmnt='STAT or CSE', dptmnt_num='131 or 107', course_title='Introduction to Probability Theory', num_credits=5, incoming_prereqs=[math_19b], quarters=[0, 1, 2], profs=[])

CE = [math_3, math_19a, math_19b, am_10, am_20, am_30, cse_20, cse_30, cse_12, cse_13s, cse_16,phys_5a, 
      phys_5c, phys_5b, cse_100, cse_101, cse_107, cse_120, cse_185e, ece_101, cse_121, ece_103]

CS = [cse_12, cse_16, cse_20, cse_30, cse_13s, math_3, math_19a, math_19b, am_10, am_30, ece_30, cse_101, 
      cse_102, cse_103, cse_120, cse_130, cse_112orcse_114a, stat_131orcse_107]

# Digital_Hardware = [cse_125, cse_122, cse_220]
# Systems_Programming = [cse_130, cse_150, cse_11]

# schedule_maker.py


course_dict = {
    'math_3': math_3,
    'math_19a': math_19a,
    'math_19b': math_19b,
    'am_10': am_10,
    'am_20': am_20,
    'am_30': am_30,
    'cse_20': cse_20,
    'cse_30': cse_30,
    'cse_12': cse_12,
    'cse_13s': cse_13s,
    'cse_16': cse_16,
    'phys_5a': phys_5a,
    'phys_5c': phys_5c,
    'phys_5b': phys_5b,
    'cse_100': cse_100,
    'cse_101': cse_101,
    'cse_102': cse_102,
    'cse_103': cse_103,
    'cse_107': cse_107,
    'cse_120': cse_120,
    'cse_125': cse_125,
    'cse_130': cse_130,
    'cse_150': cse_150,
    'cse_185e': cse_185e,
    'ece_30': ece_30,
    'ece_101': ece_101,
    'cse_111': cse_111,
    'cse_121': cse_121,
    'cse_122': cse_122,
    'cse_220': cse_220,
    'ece_103': ece_103,
    'cse_112orcse_114a': cse_112orcse_114a,
    'stat_131orcse_107': stat_131orcse_107,
}



def get_ce_courses():
    return CE

def get_cs_courses():
    return CS

def get_courseInfo():
    return course_dict

# You can define similar getters for other course categories if needed




# CE.extend(Digital_Hardware)