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
    
        if c in self.root_courses:
            self.root_courses.remove(c)
        if c in self.all_courses:
            self.all_courses.remove(c)

    # chooses the classes for a given quarter
    def choose_quarter(self, num_classes, min_credits, max_credits, min_hours, max_hours):
        chosen_classes = []
        
        if len(self.root_courses) == 0:
            return -1
        elif len(self.root_courses) == 1:
            curr_course = 0
        else:
            curr_course = random.randrange(0, len(self.root_courses)-1)
        
        chosen_classes.append(self.root_courses[curr_course])

        # iterates through all other root nodes first
        for c in self.root_courses:
            if c in chosen_classes: continue
            if self.check_class_compatibility(chosen_classes[-1], c, min_credits, max_credits, min_hours, max_hours):
                chosen_classes.append(c)
                if len(chosen_classes) == num_classes:
                    break
        
        # delete classes that were chosen
        for c in chosen_classes:
            self.del_course(c)
        self.sort_root_courses_by_outgoing()
        return chosen_classes


    # checks compatibility btwn two classes by checking if they fit into range of credits and hours   
    def check_class_compatibility(self, c1, c2,  min_credits, max_credits, min_hours, max_hours):
        total_class_credits = c1.num_credits + c2.num_credits

        if total_class_credits >= min_credits and total_class_credits <= max_credits:
            return True
        return False
    
    # sorts root_courses by outgoing_prereqs
    def sort_root_courses_by_outgoing(self):
        get_outgoing_prereqs = lambda course: len(course.outgoing_prereqs)
        self.root_courses.sort(key=get_outgoing_prereqs, reverse=True)



            



