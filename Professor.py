class Professor:
    def __init__(self, id, name, courses_ids,n,pref,office,unava):
        self.id = id
        self.name = name
        #courses_ids = [class1, class2,...]
        self.courses_ids = courses_ids
        # n of class teaching   MAX
        self.n = n
        # pref = [(date, hours)...]
        self.pref = pref
        # office => building id
        self.office = office
        # unava => days or hours unavailable [(date, hours)...]
        self.unava = unava
    def p_id(self):
        return self.id
        
    def teaching(self):
        return self.courses_ids
    
    def n_teaching(self):
        return self.n
    
    def pref(self):
        return self.pref
    
    def office(self):
        return self.office
    
    def unava(self):
        return self.unava
   
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return '{"id":%d, "name":"%s"}'%(self.id, self.name)
