"""
 view_controller.py
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
from pyramid.httpexceptions import HTTPNotFound
from pyramid.view import view_config
from pyramid.events import subscriber
from support.events import GracefulShutdown
from models.Room import Room


class ViewController(object):
    
    def __init__(self, request):
        self._request = request
        self._method = request.method
        
    def __getattr__(self, attr):
        try:
            return self._request.matchdict[attr]
        except KeyError as e:
            raise AttributeError(attr)
    
    def POST(self):
        raise HTTPNotFound()
    
    def GET(self):
        raise HTTPNotFound()
    
    def __call__(self):
        if self._method == 'GET':
            return self.GET()
        elif self._method == 'POST':
            return self.POST()
        
@subscriber(GracefulShutdown)
def shutdown(event):
    pass
