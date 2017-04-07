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
from pyramid.renderers import render
from pyramid.view import view_config
from pyramid.events import subscriber
from support.events import GracefulShutdown
from models import Room, Repository, Client, Reservation
from .view_controller import ViewController
from support import parse_date_or_not

@view_config(route_name='reservation')
class ReservationView(ViewController):
    
    def __init__(self, request):
        super(ReservationView, self).__init__(request)
    
        self.repository = Repository.Instance()
        self.rooms = self.repository.rooms
        self.data = {
            'rooms': self.rooms,
            'date_from_check': '',
            'date_to_check': '',
        }
    
    def GET(self):
        return render_to_response('assets:views/reservation.pt', self.data,
            request=self._request)
    
    def POST(self):  
        if all( x in self._request.params for x in ['client_name', 'credit_card_number',
            'number_of_guests', 'date_from', 'date_to'] ) :
            
            if all( x != '' for x in [self._request.params['client_name'], 
                self._request.params['credit_card_number'], 
                self._request.params['number_of_guests'],
                self._request.params['date_from'],
                self._request.params['date_to'] ] ) :
                
                reservation = self.make_res(*self._request.params['client_name'].split(' '),
                    self._request.params['credit_card_number'],
                    int(self._request.params['number_of_guests']),
                    self._request.params['date_from'],
                    self._request.params['date_to'])
            
                self.data.update({
                    'new_reservation': reservation,
                })
            
                return render_to_response('assets:views/reservation.pt', self.data,
                    request=self._request)
                
            else:
                self.data.update({
                })

                return render_to_response('assets:views/reservation.pt', self.data,
                    request=self._request)
                

        if all( x in self._request.params for x in ['date_from_check', 'date_to_check'] ) :                
                
            if all( x != '' for x in [self._request.params['date_from_check'], 
                self._request.params['date_to_check'] ] ) :
                
                dates, rooms = self.check_availability(self._request.params['date_from_check'],
                                                     self._request.params['date_to_check'])

                self.data.update({
                    'check_dates': dates,
                    'date_from_check': self._request.params['date_from_check'],
                    'date_to_check': self._request.params['date_to_check'],
                    'rooms': rooms
                })

                return render_to_response('assets:views/reservation.pt', self.data,
                    request=self._request)
                
            else:
                self.data.update({
                })

                return render_to_response('assets:views/reservation.pt', self.data,
                    request=self._request)
                
                
        else:
            self.data.update({
            })

            return render_to_response('assets:views/reservation.pt', self.data,
                    request=self._request)
 
        
    
    def make_res(self, fname, lname, creditcard, num_guests, date_in, date_out):
        client = Client(*self._request.params['client_name'].split(' '),
                self._request.params['credit_card_number'])

        self.repository.add_client(client)
        
        reservation = Reservation(client.ID, date_in, date_out, num_guests)

        self.repository.add_reservation(reservation)

        return reservation
        
    
    def check_availability(self, date_in_s, date_out_s):
        date_in = parse_date_or_not(date_in_s)
        date_out = parse_date_or_not(date_out_s)
        
        rooms = Repository.Instance().find_free_rooms_in_dates(date_in, date_out)
        
        return ([date_in, date_out], rooms)

        
@subscriber(GracefulShutdown)
def shutdown(event):
    pass
