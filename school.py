class School:
    def __init__(self, name, roster={}):
        self.name = name
        self.roster = roster

    def add_student(self, student_name, grade):
        if grade not in self.roster.keys():
            self.roster[grade] = [student_name]
        else:
            self.roster[grade].append(student_name)
    
    def grade(self, grade):
        return self.roster[grade]

    def sort_roster(self):
        for grade in self.roster.keys():
            self.roster[grade].sort()
        return self.roster