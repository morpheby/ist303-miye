"""
 reservation_view.py
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

import cgi

from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.renderers import render_to_response
from pyramid.view import view_config
from pyramid.events import subscriber
from support.events import GracefulShutdown
from models import Room, Repository, Client, Reservation
from .view_controller import ViewController

@view_config(route_name='reservation')
class ReservationView(ViewController):
    
    def __init__(self, request):
        super(ReservationView, self).__init__(request)
    
        self.repository = Repository.Instance()
        self.rooms = self.repository.rooms
    
    def GET(self):
        data = {
            'rooms': self.rooms,
        }
        
        return render_to_response('assets:views/reservation.pt', data,
            request=self._request)
    
    def POST(self):        
        reservation = self.make_res(*self._request.params['client_name'].split(' '),
                self._request.params['credit_card_number'],
                self._request.params['number_of_guests'],
                self._request.params['date_from'],
                self._request.params['date_to'])

        data = {
            'rooms': self.rooms,
            'new_reservation': reservation,
        }

        return render_to_response('assets:views/reservation.pt', data,
            request=self._request)
    
    def make_res(self, fname, lname, creditcard, num_guests, date_in, date_out):
        client = Client(*self._request.params['client_name'].split(' '),
                self._request.params['credit_card_number'])

        self.repository.add_client(client)
        
        reservation = Reservation(client.ID, date_in, date_out, num_guests)

        self.repository.add_reservation(reservation)

        return reservation

        
@subscriber(GracefulShutdown)
def shutdown(event):
    pass
