class Person:

	ID = 100000  #ID increments on instantiation of any person

class Client(Person):

	def __init__(self, fname, lname ):
		Person.ID += 1
    	self.fname = fname
    	self.lname = lname
    	self.ID = Person.ID
    	self.type = 'client'
    
  	def addcard(self, cardnum):
    	self.creditcard = cardnum


class Guest(Person):

	def __init__(self):
		Person.ID += 1
		self.ID = Person.ID
		self.type = 'guest'

