

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Segment:

    def __init__(self, orig, dest):
        self.orig = orig
        self.dest = dest


"""
calculates the orientation
(clockwise/counter-clockwise)
of a vector A in relation to a vector B
"""
def vectProd(vectA, vectB):
  return vectA.x * vectB.y - vectA.y * vectB.x

"""
calculates the orientation
(clockwise/counter-clockwise)
of a segment A in relation to a
segment B that has the same
origin as segment A, but ends at a point B
"""
def orientation(segmentA, pointB):

  vectA = Point(segmentA.dest.x - segmentA.orig.x, segmentA.dest.y - segmentA.orig.y)
  vectB = Point(pointB.x - segmentA.orig.x, pointB.y - segmentA.orig.y)

  return vectProd(vectA, vectB)

def pointOnSegment(segment, point):

  pointInXInterval = point.x >= min(segment.orig.x, segment.dest.x) and point.x <= max(segment.orig.x, segment.dest.x)
  pointInYInterval = point.y >= min(segment.orig.y, segment.dest.y) and point.y <= max(segment.orig.y, segment.dest.y)

  if pointInXInterval and pointInYInterval:
    return True

  return False

def segmentIntersect(segmentA, segmentB):

  d1 = orientation(segmentB, segmentA.orig)
  d2 = orientation(segmentB, segmentA.dest)
  d3 = orientation(segmentA, segmentB.orig)
  d4 = orientation(segmentA, segmentB.dest)

  print(d1, d2, d3, d4)

  if ((d1 > 0 and d2 < 0) or (d1 < 0 and d2 > 0)) and ((d3 > 0 and d4 < 0) or (d3 < 0 and d4 > 0)):
    return True
  elif d1 == 0 and pointOnSegment(segmentB, segmentA.orig):
    return True
  elif d2 == 0 and pointOnSegment(segmentB, segmentA.dest):
    return True
  elif d3 == 0 and pointOnSegment(segmentA, segmentB.orig):
    return True
  elif d4 == 0 and pointOnSegment(segmentA, segmentB.dest):
    return True
  else:
    return False
