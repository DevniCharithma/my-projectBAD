class Student:
    def __init__(self, index, name, attendance):
        self.index = index
        self.name = name
        self.attendance = attendance

    def __str__(self):
        return self.index + ' ' + self.name + ' ' + self.attendance
