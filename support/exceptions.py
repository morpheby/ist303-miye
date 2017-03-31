"""
 exceptions.py
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

import traceback
import sys
import config

class DateParserError(Exception):
    """Represents error while parsing date"""
    def __init__(self, dateStr, underlying):
        super(DateParserException, self).__init__()
        self.dateStr = dateStr
        self.underlying = underlying
        
    def __str__(self):
        return "Error parsing date {!r}. Exception: {}".format(self.dateStr, self.underlying)
        

