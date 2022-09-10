class Subject:
    def __init__(self, module, grade):
        self.module = module
        self.grade = grade

    def __str__(self):
        return self.module + ' ' + self.grade
