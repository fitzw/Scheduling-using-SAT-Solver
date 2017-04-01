class Course:
    def __init__(self, id, name, size):
        self.id = id
        self.name = name
        self.size = size
        
    def size(self):
        return self.size
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return '{"id":%d, "name":"%s"}'%(self.id, self.name)
