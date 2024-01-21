class Course:
    def __init__(self, dptmnt, dptmnt_num, course_title, num_credits, incoming_prereqs,
                  hours=30, outgoing_prereqs=None, quarters=None, profs=None, best_prof="", 
                  best_prof_rating=2.5):
        self.dptmnt = dptmnt
        self.dptmnt_num = dptmnt_num
        self.course_title = course_title
        self.num_credits = num_credits
        self.hours = hours
        self.incoming_prereqs = incoming_prereqs
        self.outgoing_prereqs = outgoing_prereqs if outgoing_prereqs is not None else []
        self.quarters = quarters if quarters is not None else []
        self.profs = profs if profs is not None else []
        self.best_prof = best_prof
        self.best_prof_rating = best_prof_rating
        self.priority_rating = 0
    
    def set_priority_rating(self):
        self.priority_rating = (5 - len(self.quarters)) + len(self.outgoing_prereqs)

    def to_dict(self):
        incoming_prereqs_dict = (
            [prereq.to_dict() for prereq in self.incoming_prereqs]
            if isinstance(self.incoming_prereqs, list)
            else []
        )

        return {
            'dptmnt': self.dptmnt,
            'dptmnt_num': self.dptmnt_num,
            'course_title': self.course_title,
            'num_credits': self.num_credits,
            'incoming_prereqs': incoming_prereqs_dict,
            'quarters': self.quarters,
            'profs': self.profs
        }

class Quarter:
    def __init__(self, college_year, quarter_type, course_list):
        self.college_year = college_year
        self.quarter_type = quarter_type
        self.course_list = course_list
    
    def to_dict(self):
        return {
            'college_year': self.college_year,
            'quarter_type': self.quarter_type,
            'courses': [course.to_dict() for course in self.course_list]
        }