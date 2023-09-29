

class Point:

  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  # Sobrecarga do operador de subtração
  def __sub__(self, other):
    return Point(self.x - other.x, self.y - other.y)


class Segment:

  def __init__(self, _origin, _destination):
      self.origin = _origin
      self.destination = _destination

  # Positivo -> self está no sentido horário em relação a point
  # Negativo -> self está no sentido anti-horário em relação a point
  # Zero -> Colineares
  def direction(self, point):
    
    # Define os pontos e toma p0 como origem do plano cartesiano
    p0 = self.origin
    p1 = self.destination - p0
    p2 = point - p0
    
    return p1.x * p2.y - p1.y * p2.x

  def pointOnSegment(self, point):

    pointInXInterval = (point.x >= min(self.origin.x, self.destination.x) and point.x <= max(self.origin.x, self.destination.x))
    pointInYInterval = (point.y >= min(self.origin.y, self.destination.y) and point.y <= max(self.origin.y, self.destination.y))

    if pointInXInterval and pointInYInterval:
      return True
    return False

  def segmentIntersect(self, segmentB):

    d1 = segmentB.direction(self.origin)
    d2 = segmentB.direction(self.destination)
    d3 = self.direction(segmentB.origin)
    d4 = self.direction(segmentB.destination)

    if ((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and ((d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0)):
      return True
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
