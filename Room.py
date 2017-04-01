class Room:
    
    def __init__(self, id, name, size, b_id):
        #self.type = type
        self.id = id
        self.name = name
        self.size = size
        self.b_id = b_id
    
    def b_id(self):
        return self.b_id
    def size(self):
        return self.size
    def __str__(self):
        return self.name
    def __repr__(self):
        return '{"id":%d, "name":"%s"}'%(self.id, self.name)
