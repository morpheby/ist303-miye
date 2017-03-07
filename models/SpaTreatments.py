class Treatment:
    
    types = []  #stores all instances
    treatment_categories = []
    
    def __init__(self, durations, cost_per_min, rooms, time_between, subtype):
        self.durations = durations
        self.cost_per_min = cost_per_min
        self.rooms = rooms
        self.time_between = time_between
        if subtype != None:
            self.subtype = subtype
        else:
            self.subtype = ''
        Treatment.types.append(self)
        self.types.append(self)
        
    def __str__(self):
        return "%s (%s)\nlengths:  %d minute, %d minute\n$%d per minute\n%d rooms" % (self.subtype,self.type,self.durations[0],self.durations[1],self.cost_per_min,self.rooms)
        
class Mineral_Bath(Treatment):
    
    num_types = 0
    types = []
    
    def __init__(self, durations, cost_per_min, rooms, time_between, subtype = None):
        self.type = 'mineral bath'
        super().__init__(durations, cost_per_min, rooms, time_between, subtype)
        Mineral_Bath.num_types += 1
        
class Massage(Treatment):
    
    num_types = 0
    types = []
    
    def __init__(self, durations, cost_per_min, rooms, time_between, subtype = None):
        self.type = 'massage'
        super().__init__(durations, cost_per_min, rooms, time_between, subtype)
        Massage.num_types += 1

class Facial(Treatment):
    
    num_types = 0
    types = []
    
    def __init__(self, durations, cost_per_min, rooms, time_between, subtype = None):
        self.type = 'facial'
        super().__init__(durations, cost_per_min, rooms, time_between, subtype)
        Facial.num_types += 1

class Specialty(Treatment):
    
    num_types = 0
    types = []
    
    def __init__(self, durations, cost_per_min, rooms, time_between, subtype = None):
        self.type = 'specialty'
        super().__init__(durations, cost_per_min, rooms, time_between, subtype)
        Specialty.num_types += 1

massage_swedish = Massage([30,60], 3, 12, None, 'swedish')
massage_shiatsu = Massage([30,60], 3, 12, None, 'shiatsu')
massage_deeptissue = Massage([30,60], 3, 12, None, 'deep tissue')
mineral_bath = Mineral_Bath([60,90], 2.5, 12, 2)
facial_normal = Facial([30,60], 2, 3, None, 'normal')
facial_collagen = Facial([30,60], 2, 3, None, 'collagen')
specialty_hotstone = Specialty([60,90], 3.5, 2, None, 'hot stone')
specialty_sugarscrub = Specialty([60,90], 3.5, 2, None, 'sugar scrub')
specialty_herbalwrap = Specialty([60,90], 3.5, 2, None, 'herbal body wrap')
specialty_mudwrap = Specialty([60,90], 3.5, 2, None, 'botanical mud wrap')
