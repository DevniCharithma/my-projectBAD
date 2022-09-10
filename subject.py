class Subject:
    def __init__(self, module, marks):
        self.module = module
        self.marks = marks

    def __str__(self):
        return self.module + ' ' + self.marks
