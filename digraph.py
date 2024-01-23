import random

class Digraph:
    def __init__(self):
        self.root_courses = []
        self.all_courses = []  # could possibly remove?

    # adds a node with no outgoing prereqs
    def add_leaf_node(self, c):
        if c not in self.all_courses:
            self.all_courses.append(c)
        if c not in self.root_courses:
            self.root_courses.append(c)
            self.sort_root_courses_by_outgoing()

    # adds a directional edge from c1 to c2
    def add_edge(self, c1, c2):
        if c1 not in self.all_courses:
            self.all_courses.append(c1)
        if c2 not in self.all_courses:
            self.all_courses.append(c2)

        # adds c1 to root nodes
        if c1 not in self.root_courses and c1.incoming_prereqs == []:
            self.root_courses.append(c1)
            self.sort_root_courses_by_outgoing()

        # if c2 was in root_nodes remove it
        if c2 in self.root_courses:
            self.root_courses.remove(c2)
            self.sort_root_courses_by_outgoing()

        if c2 not in c1.outgoing_prereqs:
            c1.outgoing_prereqs.append(c2)
        if c1 not in c2.incoming_prereqs:
            c2.incoming_prereqs.append(c1)

    def del_edge(self, c1, c2):
        if c2 in c1.outgoing_prereqs:
            c1.outgoing_prereqs.remove(c2)
        if c1 in c2.incoming_prereqs:
            c2.incoming_prereqs.remove(c1)

    # only use for root nodes
    def del_course(self, c):
        while len(c.outgoing_prereqs) != 0:
            c_outgoing = c.outgoing_prereqs[0]
            self.del_edge(c, c_outgoing)
            if len(c_outgoing.incoming_prereqs) == 0:
                self.root_courses.append(c_outgoing)
                self.sort_root_courses_by_outgoing()
    
        if c in self.root_courses:
            self.root_courses.remove(c)
            self.sort_root_courses_by_outgoing()
        if c in self.all_courses:
            self.all_courses.remove(c)

    # chooses the classes for a given quarter
    # quarter: 0 -> Fall, 1 -> Winter, 2 -> Spring 
    def choose_quarter(self, num_courses, min_credits, max_credits, min_hours, max_hours, quarter):
        chosen_courses = []
        
        # NOTE: implementation for one random root course per quarter
        """if len(self.root_courses) == 0:
            return -1
        elif len(self.root_courses) == 1:
            curr_course = 0
        else:
            curr_course = random.randrange(0, len(self.root_courses)-1)
        """

        if len(self.root_courses) == 0:
            return -1
        else:
            curr_course = 0
        
        # randomly iterates through root courses until it finds one that works for the "quarter"
        while True:
            if quarter in self.root_courses[curr_course].quarters:
                chosen_courses.append(self.root_courses[curr_course])
                break
            else:
                curr_course = random.randrange(0, len(self.root_courses))
    
        # iterates once or twice depending on num_classes specified
        for c in self.root_courses:
            if c in chosen_courses: continue
            if self.check_class_compatibility(chosen_courses, c, min_credits, max_credits, min_hours, max_hours, quarter, num_courses):
                chosen_courses.append(c)
                if len(chosen_courses) == num_courses:
                    break

        # delete classes that were chosen
        for c in chosen_courses:
            self.del_course(c)
        self.sort_root_courses_by_outgoing()
        return chosen_courses


    # checks compatibility btwn two classes by checking if they fit into range of credits and hours   
    def check_class_compatibility(self, chosen_courses, new_course, min_credits, max_credits, min_hours, max_hours, quarter, num_courses):
        # adjusts when we are only looking at 2 courses but 3 course overall quarter
        adjusted_min_credits = (min_credits - 5) if len(chosen_courses) == 1 and num_courses == 3 else min_credits
        adjusted_max_credits = (max_credits - 5) if len(chosen_courses) == 1 and num_courses == 3 else max_credits
        
        if quarter not in new_course.quarters:
            return False
        
        total_class_credits = new_course.num_credits
        for c in chosen_courses:
            total_class_credits += c.num_credits

        if total_class_credits >= adjusted_min_credits and total_class_credits <= adjusted_max_credits:
            return True
        return False
    
    # sorts root_courses by outgoing_prereqs
    def sort_root_courses_by_outgoing(self):
        get_outgoing_prereqs = lambda course: course.priority_rating
        self.root_courses.sort(key=get_outgoing_prereqs, reverse=True)



            



