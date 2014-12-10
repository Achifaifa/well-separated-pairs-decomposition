import numpy as np
import copy

class Rectangle(object):
    def __init__(self, d, intervals, widths = None):
        self._d = d
        self._intervals = intervals
        self._widths = self._intervals[:,1] - self._intervals[:,0] 
    
    def __repr__(self):
        return "Rectangle %s" %("x".join([str(x) for x in self._intervals]))

    def times(self, other):
        return Rectangle(self._d + other._d, self._intervals + other._intervals, self._widths + other._widths)

    def halve(self, l):
        intervals1 = np.copy(self._intervals)
        intervals2 = np.copy(self._intervals)
        widths = self._widths
        widths[l] /= 2.
        intervals1[l][1] = (self._intervals[l,1] + self._intervals[l,0])/2.
        intervals2[l][0] = intervals1[l][1]
        #[......] -> [[...],[...]]
        return [Rectangle(self._d, intervals1,widths), Rectangle(self._d, intervals2, widths)]
 
"""Axis-Aligned Bounding Box for a matrix, with rows being points"""
def AABB(P):
    maxs = P.max(0)
    mins = P.min(0)
    ints = [[mins[i],maxs[i]] for i in range(P.shape[1])]
    ints = np.array(ints)
    return Rectangle(P.shape[1],ints)
