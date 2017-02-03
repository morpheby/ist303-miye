#!/usr/bin/env python

"""
 main.py
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


import config
import client
from waitress import serve
from pyramid.config import Configurator
import threading as t
from support.events import GracefulShutdown

def create_app_config():
    """
    Creates Pyramid config
    """
    config = Configurator()
    config.add_route('home', '/')
    config.scan('views')
    
    return config

def create_wsgi_app(config = create_app_config()):
    """
    Creates WSGI application. Necessary to run in debug mode, i.e. by 
    waitress-serve --listen=*:8041 main:create_wsgi_app
    """
    
    app = config.make_wsgi_app()
    return app

class Server(object):
    def __init__(self, host='127.0.0.1', port=8080):
        """
        Initializes the server and required multi-threading vars
        """
        
        self._host = host
        self._port = port
        
        self._config = None
        self._app = None
        
        # Create condition to see if the server is ready
        self._ready_cv = t.Condition()
        self._ready = False
        
        # Create server thread
        self._thread = t.Thread(target=self.server_worker, daemon=True)
        
    def start_server(self):
        """
        Starts the server thread
        """
        
        self._thread.start()
        
    def wait_for_server(self):
        """
        Waits till the server is completely ready to serve data
        """
        
        with self._ready_cv:
            while not self._ready:
                self._ready_cv.wait()
        
    def server_worker(self):
        """
        Initializes the server, notifies waiter that it is ready and continues to work
        """
        
        self._config = create_app_config()
        self._app = create_wsgi_app(self._config)
        
        with self._ready_cv:
            self._ready = True
            self._ready_cv.notify_all()
        
        serve(self._app, host=self._host, port=self._port)
        
    def stop_server(self):
        """
        Stops the server
        """
        
        # Send GracefulShutdown event
        gs = GracefulShutdown()
        self._config.registry.notify(gs)


def start_client(host, port):
    client.webview_start("http://%s:%d/" % (host, port))


if __name__ == '__main__':
    
    server_host = '127.0.0.1'
    port_number = 48552
    
    # Start the server
    srv = Server(server_host, port_number)
    srv.start_server()
    
    # Wait for the server startup
    srv.wait_for_server()
    
    # Now we can start the client
    
    # This one usually requires main thread, since it works with GUI
    start_client(server_host, port_number)
    
    # When start_client() returns, it means it was closed. Stop the server.
    srv.stop_server()
    


