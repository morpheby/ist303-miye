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
import config

SAFETY_DATE_GAP = 180

class ReservationSearcher(object):
    """Facilitates segment tree for looking for free rooms"""
    def __init__(self, reservations):
        super(ReservationSearcher, self).__init__()
        
        min_date = min([r.checkin for r in reservations] + [datetime.datetime.now()])
        max_date = max([r.checkout for r in reservations] + [datetime.datetime.now()])

        self.build_tree_for_dates(min_date, max_date)
        
        for r in reservations:
            self.add_reservation(r)
        
    def add_reservation(self, res):
        def add(node_value, sum_value):
            if config.RESFREE_DEBUG: print("Add", res, node_value, sum_value)
            return node_value + [res.roomID]
        try:
            self.tree.act_segment(res.checkin, res.checkout, add)
        except IndexError:
            self.extend(res.checkin, res.checkout)
            self.tree.act_segment(res.checkin, res.checkout, add)
        
    def remove_reservation(self, res):
        def remove(node_value, sum_value):
            return [r for r in node_value if r != res.roomID]
        try:
            self.tree.act_segment(res.checkin, res.checkout, remove)
        except IndexError:
            self.extend(res.checkin, res.checkout)
            self.tree.act_segment(res.checkin, res.checkout, remove)
        
    def get_occupied_rooms(self, checkin, checkout):
        oc_rooms = set()
        def rooms_acc(node_value, sum_value):
            nonlocal oc_rooms
            if config.RESFREE_DEBUG: print(sum_value)
            oc_rooms = oc_rooms.union(sum_value)
            return node_value # do not modify tree
        try:
            self.tree.act_segment(checkin, checkout, rooms_acc, traverse = True)
        except IndexError:
            self.extend(checkin, checkout)
            self.tree.act_segment(checkin, checkout, rooms_acc, traverse = True)
        return oc_rooms
            
    def build_tree_for_dates(self, start, end):
        diff = (end - start).days + SAFETY_DATE_GAP
        all_days = [start + datetime.timedelta(days=i) for i in range(diff)]
        
        self.tree = SegmentTree(all_days, initial = [], f_diff = lambda a,b: (a-b).days)
        
        
    def extend(self, start, end):
        # Rebuild tree
        min_date = min(self.tree.start, start)
        max_date = max(self.tree.end, end)
        self.build_tree_for_dates(min_date, max_date)
        
