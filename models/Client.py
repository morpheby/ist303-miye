class Person:

    ID = 100000  #ID increments on instantiation of any person

class Client(Person):

    def __init__(self, fname, lname, creditcard = None ):
        self.ID = Person.ID
        Person.ID += 1
        self.fname = fname
        self.lname = lname
        self.creditcard = creditcard
        self.type = 'client'
        
    def __str__(self):
        return "Client: %s %s, #%d (CC: %r)" % (self.fname, self.lname, self.ID, self.creditcard)
    


class Guest(Person):

    def __init__(self, clientID):
        self.ID = Person.ID
        Person.ID += 1
        self.type = 'guest'
        self.clientID = clientID

