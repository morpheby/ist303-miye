"""
 ReservationSearcher.py
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

from support import SegmentTree
import datetime

SAFETY_DATE_GAP = 365

class ReservationSearcher(object):
    """Facilitates segment tree for looking for free rooms"""
    def __init__(self, reservations):
        super(ReservationTree, self).__init__()
        
        min_date = min([r.checkin for r in reservations] + [datetime.datetime.now()])
        max_date = max([r.checkout for r in reservations] + [datetime.datetime.now()])

        self.build_tree_for_dates(min_date, max_date)
        
    def add_reservation(self, res):
        def add(rooms):
            return rooms + [res.roomID]
        try:
            self.tree.act_segment(res.checkin, res.checkout, add)
        except IndexError:
            self.extend(res.checkin, res.checkout)
            self.tree.act_segment(res.checkin, res.checkout, add)
        
    def remove_reservation(self, res):
        def remove(rooms):
            return [r for r in rooms if r != res.roomID]
        try:
            self.tree.act_segment(res.checkin, res.checkout, remove)
        except IndexError:
            self.extend(res.checkin, res.checkout)
            self.tree.act_segment(res.checkin, res.checkout, remove)
        
    def get_occupied_rooms(self, res):
        oc_rooms = {}
        def rooms_acc(rooms):
            nonlocal oc_rooms
            oc_rooms = oc_rooms.union(rooms)
            return rooms # do not modify tree
        try:
            self.tree.act_segment(res.checkin, res.checkout, rooms_acc)
        except IndexError:
            self.extend(res.checkin, res.checkout)
            self.tree.act_segment(res.checkin, res.checkout, rooms_acc)
            
    def build_tree_for_dates(self, start, end):
        diff = (end - start).days + SAFETY_DATE_GAP
        all_days = [start + datetime.timedelta(days=i) for i in range(diff)]
        
        self.tree = SegmentTree(all_days, f_diff = lambda a,b: (a-b).days)
        
        
    def extend(self, start, end):
        # Rebuild tree
        min_date = min(self.tree.start, start)
        max_date = max(self.tree.end, end)
        self.build_tree_for_dates(min_date, max_date)
        
