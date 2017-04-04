"""
 CostUnit.py
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

class CostBase(object):
    """
    Base class for Cost.
    """
    def __init__(self, reason):
        super(CostBase, self).__init__()
        self.reason = reason

class CostUnit(CostBase):
    """
    Basic unit for cost.
    """
    def __init__(self, amount, reason):
        super(CostUnit, self).__init__(reason)
        self.amount = amount

class CostMultiply(CostBase):
    """
    Cost multiplier for cost
    """
    def __init__(self, base, multiplier, reason):
        super(CostMultiply, self).__init__(reason)
        self.mult = multiplier
        self.base = base
    
class CostAdd(CostBase):
    """
    Cost adder for cost
    """
    def __init__(self, base, add, reason):
        super(CostAdd, self).__init__(reason)
        self.add = add
        self.base = base
        
class CostList(CostBase):
    """
    Cost list for cost
    """
    def __init__(self, cost_list, reason):
        super(CostList, self).__init__(reason)
        self.cost_list = cost_list

class CostTraverserBase(object):
    """
    Base Traverser object for cost calculation and description (strategy-like)
    """
    def __init__(self, cost):
        super(CostTraverserBase, self).__init__()
        self.cost = cost
    
    def walk_untyped(self, cost):
        raise NotImplementedError(f"Unhandled Cost object type {type(cost).__name__} for {cost!r}")
        
    def walk_CostUnit(self, cost):
        return NotImplementedError("Abstract method. No processing done")
        
    def walk_CostMultiply(self, cost):
        return NotImplementedError("Abstract method. No processing done")
        
    def walk_CostAdd(self, cost):
        return NotImplementedError("Abstract method. No processing done")
        
    def walk_CostList(self, cost):
        return NotImplementedError("Abstract method. No processing done")
        
    def getwalker(self, cost):
        try:
            return getattr(self, f"walk_{type(cost).__name__}")
        except:
            return self.walk_untyped
    
    def walk(self, cost):
        return self.getwalker(cost)(cost)
        
    def __call__(self):
        return self.walk(self.cost)
            
class TotalTraverser(CostTraverserBase):
    """
    Traverser object for cost calculation
    """
    def __init__(self, cost):
        super(TotalTraverser, self).__init__(cost)
        
    def walk_CostUnit(self, cost):
        return cost.amount
        
    def walk_CostMultiply(self, cost):
        return cost.mult * self.walk(cost.base)
        
    def walk_CostAdd(self, cost):
        return cost.add + self.walk(cost.base)
        
    def walk_CostList(self, cost):
        return sum([self.walk(c) for c in cost.cost_list])
        
