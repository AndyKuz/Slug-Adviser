class Digraph:
    def __init__(self):
        self.root_courses = []
        self.all_courses = []  # could possibly remove?

    # adds a directional edge from c1 to c2
    def add_edge(self, c1, c2):
        if c1 not in self.all_courses:
            self.all_courses.append(c1)
        if c2 not in self.all_courses:
            self.all_courses.append(c2)

        # adds c1 to root nodes
        if c1 not in self.root_courses and c1.incoming_prereqs == []:
            self.root_courses.append(c1)

        # if c2 was in root_nodes remove it
        if c2 in self.root_courses:
            self.root_courses.remove(c2)

        if c2 not in c1.outgoing_prereqs:
            c1.outgoing_prereqs.append(c2)
        if c1 not in c2.incoming_prereqs:
            c2.incoming_prereqs.append(c1)
    
    def del_edge(self, c1, c2):
        pass

    def bfs(self, c):
        pass
