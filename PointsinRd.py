import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches
import pylab

class Rectangle(object):
  
  def __init__(self, d, intervals, widths = None):
    
    self.d = d
    self.intervals = intervals
    self.widths = self.intervals[:,1]-self.intervals[:,0] 
  
  def __repr__(self):
    
    return "Rectangle %s" %("x".join([str(x) for x in self.intervals]))

  def times(self, other):
    
    return Rectangle(self.d+other.d, self.intervals+other.intervals, self.widths+other.widths)

  def halve(self, l):
    
    intervals1 = np.copy(self.intervals)
    intervals2 = np.copy(self.intervals)
    widths = self._widths
    widths[l] /= 2.
    intervals1[l,1] = (self.intervals[l,1] + self.intervals[l,0])/2.
    intervals2[l,0] = intervals1[l,1]
    #[......] -> [[...],[...]]
    return [Rectangle(self.d, intervals1,widths), Rectangle(self.d, intervals2, widths)]
 
class DLNode(object):
  
  def __init__(self, point, prev, next):
    
    self.point = point
    self.prev = prev
    self.next = next

  def setprev(self, point):
    
    self.prev = point

  def setnext(self, point):
    
    self.next = point

class DoubleList(object):

  head = None
  tail = None

  def append(self, data):
    
    new_node = DLNode(data, None, None)
    if self.head is None:
      self.head = self.tail = new_node
    else:
      new_node.setprev(self.tail)
      new_node.setnext(self.tail)
      self.tail.setnext(new_node)
      self.tail = new_node

  def remove(self, node_value):
    
    current_node = self.head
    while current_node is not None:
      if current_node.point == node_value:
        #if it is not the first element
        if current_node.prev is not None:
          current_node.prev.setnext(current_node.next)
          current_node.next.setprev(current_node.prev)
        else:
          self.head = current_node.next
          current_node.next.setprev(None)
      current_node = current_node.next

class Points(object):
  
  def __init__(self, P):
    
    self.P = P

def AABB(P):
  """
  Axis-Aligned Bounding Box for a matrix, with rows being points
  """

  maxs = P.max(0)
  mins = P.min(0)
  ints = [[mins[i],maxs[i]] for i in range(P.shape[1])]
  ints = np.array(ints)
  return Rectangle(P.shape[1],ints)

def OuterRectangle(P):

  maxs = P.max(0)
  mins = P.min(0)
  center = (maxs + mins)/2.
  widths = maxs - mins
  width = widths.max()
  ints = [[center[i] - width/2., center[i] + width/2.] for i in range(P.shape[1])]
  ints = np.array(ints)
  return Rectangle(P.shape[1],ints)

def showPointsandRectangle(P,Rect):

  ints = Rect.intervals()
  fig = plt.figure()
  ax = fig.add_subplot(111)
  verts = [
    (ints[0,0], ints[1,0]),
    (ints[0,0], ints[1,1]),
    (ints[0,1], ints[1,1]),
    (ints[0,1], ints[1,0]),
    (ints[0,0], ints[1,0]),]
  codes = [
    Path.MOVETO,
    Path.LINETO,
    Path.LINETO,
    Path.LINETO,
    Path.CLOSEPOLY,]

  path = Path(verts, codes)
  patch = patches.PathPatch(path, facecolor='none', lw=2)
  ax.add_patch(patch)
  ax.set_xlim(-2,2)
  ax.set_ylim(-2,2)
  plt.plot(P[:,0],P[:,1],'ro')
  plt.show()