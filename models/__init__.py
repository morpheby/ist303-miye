"""
 __init__.py
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

from .Client import Client
from .Reservation import Reservation
from .Room import Room
from .SpaRes import SpaRes
from .Repository import Repository

def init_helpers():
    Reservation.client = property(lambda self: Repository.Instance().find_client_by_id(self.clientID))
    Reservation.room = property(lambda self: Repository.Instance().find_room_by_id(self.roomID))
    Reservation.guest_list = property(lambda self: [Repository.Instance().find_client_by_id(c) for c in self.guest_ids])

init_helpers()
