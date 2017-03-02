#creating a new instance with y = Room(405,4) will automatically add the room to the master list of rooms (Room.list_all)

class Room:

	#create the master list of all rooms; list of lists: [room #, max occ.]
	single = [ [100 + x, 1] for x in range(16) ]
	double = [ [200 + x, 2] for x in range(16) ]
	quad = [ [300 + x, 4] for x in range(4) ]
	list_all = single + double + quad

	def __init__(self, numbr, max_guests):
		self.numbr = numbr
		self.max_guests = max_guests
		Room.list_all.append([self.numbr,self.max_guests])

	def remove(self, numbr):
		pass