"""
 edit_res.py
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

@view_config(route_name='editres_view')
class EditResView(ViewController):
    
    def __init__(self, request):
        super(EditResView, self).__init__(request)
    
        self.repository = Repository.Instance()
    
    def GET(self):
        reservation = self.repository.find_reservation_by_id(int(self.res_id))
        
        data = {
            'checkin': reservation.checkin,
            'checkout': reservation.checkout,
            'ID': reservation.ID,
            'nights': reservation.nights,
            'rates': reservation.nightly_rates,
            'total': reservation.ttlcost,
            'reservation': reservation,
        }
        
        return render_to_response('assets:views/editres.pt', data,
            request=self._request)

        
@subscriber(GracefulShutdown)
def shutdown(event):
    pass
