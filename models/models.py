

class Point:

  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  # Overload of the subtraction operator
  def __sub__(self, other):
    return Point(self.x - other.x, self.y - other.y)
  
  # Overload of the less than operator
  def __lt__(self, other):
    if self.x < other.x:
      return True
    elif self.x == other.x:
      return self.y < other.y
    return False

  # Overload of the equal to operator
  def __eq__(self, other):
    return self.x == other.x and self.y == other.y


class Segment:

  def __init__(self, _origin, _destination):
      self.origin = _origin
      self.destination = _destination


  # Positive -> self is clockwise in relation to point
  # Negative -> self is counter-clockwise in relation to point
  # Zero -> Colinear
  def direction(self, point):
    
    # Defines the points and takes p0 as the 
    # origin of the cartesian plane
    p0 = self.origin
    p1 = self.destination - p0
    p2 = point - p0
    
    return p1.x * p2.y - p1.y * p2.x


  # Returns true if the point is on the segment
  def pointOnSegment(self, point):

    pointInXInterval = (point.x >= min(self.origin.x, self.destination.x) and point.x <= max(self.origin.x, self.destination.x))
    pointInYInterval = (point.y >= min(self.origin.y, self.destination.y) and point.y <= max(self.origin.y, self.destination.y))

    if pointInXInterval and pointInYInterval:
      return True
    return False


  # Returns true if the segments intersect
  def segmentIntersect(self, segmentB):

    d1 = segmentB.direction(self.origin)
    d2 = segmentB.direction(self.destination)
    d3 = self.direction(segmentB.origin)
    d4 = self.direction(segmentB.destination)

    # General cases
    if ((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and ((d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0)):
      return True
    
    # Colinear cases
    elif d1 == 0 and segmentB.pointOnSegment(self.origin):
      return True
    elif d2 == 0 and segmentB.pointOnSegment(self.destination):
      return True
    elif d3 == 0 and self.pointOnSegment(segmentB.origin):
      return True
    elif d4 == 0 and self.pointOnSegment(segmentB.destination):
      return True
    else:
      return False
    

  # Returns the leftmost point of the segment
  def leftmostPoint(self):
    
    originIsLeftmost = self.origin.x < self.destination.x
    pointsHaveSameX = self.origin.x == self.destination.x
    originIsLowest = self.origin.y < self.destination.y

    if originIsLeftmost or (pointsHaveSameX and originIsLowest):
        return self.origin
    else:
        return self.destination


  # Returns if a segment is less than another segment
  def __lt__(self, other):
      
      selfLeftmost = self.leftmostPoint()
      otherLeftmost = other.leftmostPoint()
      
      # A segment A is less than another segment B 
      # if the leftmost point of A is to the left of 
      # the leftmost point of B.
      if selfLeftmost.x < otherLeftmost.x:
        return True
      
      # If both segments have the same leftmost x 
      # coordinates, the segment with the lowest y 
      # coordinate is less than the other.
      elif selfLeftmost.x == otherLeftmost.x:
        return selfLeftmost.y < otherLeftmost.y
      
      return False


  # Two points are equal if they have the same 
  # leftmost point
  def __eq__(self, other):
    
    selfLeftmost = self.leftmostPoint()
    otherLeftmost = other.leftmostPoint()

    segmentsLeftmostXCoordSame = selfLeftmost.x == otherLeftmost.x
    segmentsLeftmostYCoordSame = selfLeftmost.y == otherLeftmost.y

    segmentsHaveSameLeftmostPoint = segmentsLeftmostXCoordSame and segmentsLeftmostYCoordSame
    
    return segmentsHaveSameLeftmostPoint
