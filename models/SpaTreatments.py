class Treatment:
    
    catalog = {}  #stores all instances
    
    def __init__(self, treatment_type, durations, cost_per_min, rooms, time_between, subtype = None):
        self.durations = durations
        self.cost_per_min = cost_per_min
        self.rooms = rooms
        self.treatment_type = treatment_type
        self.time_between = time_between
        if subtype != None:
            self.subtype = subtype
            
        if treatment_type in Treatment.catalog:
            Treatment.catalog[treatment_type].append(self)
        else:
            Treatment.catalog[treatment_type] = [self]

        
    def __str__(self):
        return "%s %s\nlengths:  %d minute, %d minute\n$%d per minute\n%d rooms\n" % (self.subtype,self.treatment_type,self.durations[0],self.durations[1],self.cost_per_min,self.rooms)

        
    def print_menu():
        if len(Treatment.catalog) > 0:
            for key in Treatment.catalog:
                for item in Treatment.catalog[key]:
                    print(item)
        else:
            print("No treatments have been added yet.  Use Treatment() class to add.")
        

massage_swedish = Treatment('massage',[30,60], 3, 12, 0, 'swedish')
massage_shiatsu = Treatment('massage',[30,60], 3, 12, 0, 'shiatsu')
massage_deeptissue = Treatment('massage',[30,60], 3, 12, 0, 'deep tissue')
mineral_bath = Treatment('mineral bath',[60,90], 2.5, 12, 2, 'standard')
facial_normal = Treatment('facial',[30,60], 2, 3, 0, 'normal')
facial_collagen = Treatment('facial',[30,60], 2, 3, 0, 'collagen')
specialty_hotstone = Treatment('specialty',[60,90], 3.5, 2, 0, 'hot stone')
specialty_sugarscrub = Treatment('specialty',[60,90], 3.5, 2, 0, 'sugar scrub')
specialty_herbalwrap = Treatment('specialty',[60,90], 3.5, 2, 0, 'herbal body wrap')
specialty_mudwrap = Treatment('specialty',[60,90], 3.5, 2, 0, 'botanical mud wrap')
