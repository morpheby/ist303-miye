"""
 Room.py
 ist303-miye
 
Copyright (C) 2017 

This program is free software; you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation; either version 2 of the License, or (at your option) any later
version. 
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program; if not, write to the Free Software Foundation, Inc., 59 Temple
Place, Suite 330, Boston, MA 02111-1307 USA 
"""

from .CostUnit import CostUnit

# Baserice
HOTEL_BASEPRICE = {'Single': 140, 'Double': 260, 'Quad': 480}

class Room:

    ID = 30000
    PRICE_SINGLE = CostUnit(HOTEL_BASEPRICE['Single'], "Base price for Single room")
    PRICE_DOUBLE = CostUnit(HOTEL_BASEPRICE['Double'], "Base price for Double room")
    PRICE_QUAD = CostUnit(HOTEL_BASEPRICE['Quad'], "Base price for Quad room")

    def __init__(self, numbr, max_guests):
        self.ID = Room.ID
        Room.ID += 1
        self.numbr = numbr
        self.max_guests = max_guests

    def remove(self, numbr):
        pass
    
    @property
    def price(self):
        return {
            1: Room.PRICE_SINGLE,
            2: Room.PRICE_DOUBLE,
            4: Room.PRICE_QUAD,
        }[self.max_guests]
    
    @property
    def name(self):
        "The name property."
        return "Room #%d (max. guests: %d)" % (self.numbr, self.max_guests)
     