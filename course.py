class Course:
    def __init__(self, dptmnt, dptmnt_num, course_title, num_credits, incoming_prereqs, score=2.5, outgoing_prereqs=None, quarters=None, profs=None):
        self.dptmnt = dptmnt
        self.dptmnt_num = dptmnt_num
        self.course_title = course_title
        self.num_credits = num_credits
        self.score = score
        self.incoming_prereqs = incoming_prereqs
        self.outgoing_prereqs = outgoing_prereqs if outgoing_prereqs is not None else []
        self.quarters = quarters if quarters is not None else []
        self.profs = profs if profs is not None else []
        