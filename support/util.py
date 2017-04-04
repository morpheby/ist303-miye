"""
 events.py
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

from dateutil import parser

def parse_date_or_not(date):
    if type(date) == str:
        try:
            return parser.parse(date)
        except ValueError as e:
            raise exc.DateParserError(date, e)
    elif type(date) == datetime.datetime:
        return date
    else:
        raise ValueError(f"Invalid date object: {date!r}")

class SegmentTree(object):
    """Segment Tree"""
    
    class TreeNode(object):
        """SegmentTree Node"""
        def __init__(self, start, end):
            super(SegmentTree.TreeNode, self).__init__()
            self.start = start
            self.end = end
            self.value = None
            self.left = None
            self.right = None
    
    def __init__(self, values_ordered, f_diff = (lambda a,b: a - b)):
        super(SegmentTree, self).__init__()
        
        def build_tree(values):
            node = SegmentTree.TreeNode(values[0], values[-1])
            node.left = build_tree(values[:len(values)//2])
            node.right = build_tree(values[len(values)//2:])
            return node
        
        self.f_diff = f_diff
        self.root = build_tree(values_ordered)
        
    @property
    def start(self):
        return self.root.start
        
    @property
    def end(self):
        return self.root.end
        
    def act_segment(start, end, f_act):
        def act(node, start, end):
            if self.f_diff(node.start - start) < 0 or self.f_diff(end, node.end) < 0:
                a = act(node.left)
                b = act(node.right)
                return a + b
            elif self.f_diff(start, node.start) <= 0 and self.f_diff(node.end, end) <= 0:
                node.value = f_act(node.value)
                return self.f_diff(node.end, node.start)
            else:
                return 0
        
        if (act(self.root, start, end)) != self.f_diff(end, start):
            raise IndexError("SegmentTree doesn't cover all values")
        
        
