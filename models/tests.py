from models import Point
from models import Segment

def testPointLessThan():
  # Test for x values
  p1 = Point(1, 5)
  p2 = Point(2, 5)
  assert p1 < p2, "Test failed: Expected p1 to be less than p2 based on x values"

  # Test for same x values, different y values
  p3 = Point(2, 3)
  p4 = Point(2, 4)
  assert p3 < p4, "Test failed: Expected p3 to be less than p4 based on y values"

  # Test for neither being less than the other
  p5 = Point(3, 3)
  p6 = Point(2, 2)
  assert not (p5 < p6), "Test failed: Expected p5 not to be less than p6"

  print("All point less than tests passed!")


def testPointEqualTo():
  # Test for equal points
  p1 = Point(1, 5)
  p2 = Point(1, 5)
  assert p1 == p2, "Test failed: Expected p1 to be equal to p2"

  # Test for different x values
  p3 = Point(1, 4)
  p4 = Point(2, 4)
  assert not (p3 == p4), "Test failed: Expected p3 not to be equal to p4"

  # Test for different y values
  p5 = Point(3, 5)
  p6 = Point(3, 6)
  assert not (p5 == p6), "Test failed: Expected p5 not to be equal to p6"

  print("All point equal to tests passed!")

def test_distance():
    p0 = Point(0,0)
    p1 = Point(2,0)
    assert p0.distance(p1) == 2, "Test 1 failed"

    p2 = Point(2,5)
    assert p2.distance(p2) == 0, "Test 2 failed"

    p3 = Point(-10, 0)
    assert p0.distance(p3) == 10, "Test 3 failed"
    
    p4 = Point(3,4)
    p5 = Point(-3, -4)
    assert p4.distance(p5) == 10, "Test 4 failed"

    print("Distance function has been calculated correctly")

# Run the tests
testPointLessThan()
testPointEqualTo()


def test_orientation():

    # Test 1: If p0p1 is oriented clockwise in relation to p0p2
    p0 = Point(0, 0)
    p1 = Point(1, 1)
    p2 = Point(1, 2)
    seg1 = Segment(p0, p1)
    assert seg1.direction(p2) > 0, "Test 1 Failed"

    # Test 2: If p0p1 is oriented counter-clockwise in relation to p0p3
    p3 = Point(2, 0)
    assert seg1.direction(p3) < 0, "Test 2 Failed"

    # Test 3: If p0p1 is colinear to p0p4
    p4 = Point(2, 2)
    assert seg1.direction(p4) == 0, "Test 3 Failed"

    # Test 4: If p5p6 is colinear to p5p7 (all points y axis)
    p5 = Point(0, 0)
    p6 = Point(0, 1)
    seg2 = Segment(p5, p6)
    p7 = Point(0, 2)
    assert seg2.direction(p7) == 0, "Test 4 Failed"

    # Test 5: If p8p9 is colinear to p8p10 (all points x axis)
    p8 = Point(0, 0)
    p9 = Point(1, 0)
    seg3 = Segment(p8, p9)
    p10 = Point(2, 0)
    assert seg3.direction(p10) == 0, "Test 5 Failed"

    # Test 6: If p11p12 is oriented counter-clockwise in relation to p11p13 (all negative coordinates)
    p11 = Point(-2, -2)
    p12 = Point(-3, -3)
    seg4 = Segment(p11, p12)
    p13 = Point(-4, -2)
    assert seg4.direction(p13) < 0, "Test 6 Failed"

    print("All direction tests passed!")



def testPointOnSegment():

    # Test 1: Point on the segment
    p0 = Point(1, 1)
    p1 = Point(2, 2)
    seg1 = Segment(p0, p1)
    assert seg1.pointOnSegment(p1) == True, "Test 1 Failed"

    # Test 2: Point off the segment but on the line extended from the segment
    p2 = Point(3, 3)
    assert seg1.pointOnSegment(p2) == False, "Test 2 Failed"

    # Test 3: Point outside the line formed by the segment
    p3 = Point(2, 3)
    assert seg1.pointOnSegment(p3) == False, "Test 3 Failed"

    # Test 4: Point exactly at the start of the segment
    assert seg1.pointOnSegment(p0) == True, "Test 4 Failed"

    # Test 5: Point inside the segment, but not at start or end
    p4 = Point(1.5, 1.5)
    assert seg1.pointOnSegment(p4) == True, "Test 5 Failed"

    # Test 6: Point lying on the vertical segment
    p5 = Point(2, 0)
    p6 = Point(2, 3)
    p7 = Point(2, 1.5)
    seg2 = Segment(p5, p6)
    assert seg2.pointOnSegment(p7) == True, "Test 6 Failed"

    print("All points on segment tests passed!")

def testSegmentIntersect():
    # Test 1: Segments that intersect
    p0 = Point(1, 1)
    p1 = Point(2, 2)
    p2 = Point(3, 2.5)
    seg1 = Segment(p0, p1)
    seg2 = Segment(p1, p2)
    assert seg1.segmentIntersect(seg2) == True, "Test 1 Failed"

    # Test 2: Segments that intersect
    p1 = Point(1, 1.5)
    p2 = Point(3, 1.5)
    p3 = Point(2, 2)
    p4 = Point(2, 1)
    seg1 = Segment(p1, p2)
    seg2 = Segment(p2, p3)
    assert seg1.segmentIntersect(seg2) == True, "Test 2 Failed"

    # Test 3: Segments that don't intersect (colinear)
    p1 = Point(1, 1.5)
    p2 = Point(3, 1.5)
    p3 = Point(4, 1.5)
    p4 = Point(5, 1.5)
    seg1 = Segment(p1, p2)
    seg2 = Segment(p3, p4)
    assert seg1.segmentIntersect(seg2) == False, "Test 3 Failed"

    # Test 4: Segments that intersect (colinear)
    p1 = Point(1, 1.5)
    p2 = Point(3, 1.5)
    p3 = Point(2, 1.5)
    p4 = Point(5, 1.5)
    seg1 = Segment(p1, p2)
    seg2 = Segment(p3, p4)
    assert seg1.segmentIntersect(seg2) == True, "Test 4 Failed"

    # Test 5: Segments that intersect on one point, perpendicular to each other (forming a right angle)
    p1 = Point(1, 1.5)
    p2 = Point(3, 1.5)
    p3 = Point(2, 2)
    p4 = Point(2, 1.5)
    seg1 = Segment(p1, p2)
    seg2 = Segment(p3, p4)
    assert seg1.segmentIntersect(seg2) == True, "Test 5 Failed"

    # Test 6: Segments that don't intersect, parallel to each other
    p1 = Point(1, 1)
    p2 = Point(3, 1)
    p3 = Point(1, 2)
    p4 = Point(3, 2)
    seg1 = Segment(p1, p2)
    seg2 = Segment(p3, p4)
    assert seg1.segmentIntersect(seg2) == False, "Test 6 Failed"

    # Test 7: Segments that intersect at one end
    p1 = Point(1, 1)
    p2 = Point(3, 1)
    p3 = Point(3, 1)
    p4 = Point(3, 2)
    seg1 = Segment(p1, p2)
    seg2 = Segment(p3, p4)
    assert seg1.segmentIntersect(seg2) == True, "Test 7 Failed"

    print("All segment intersect tests passed!")

def testLeftmostPointAndOrdering():
    # Creating points
    point1 = Point(2, 2)
    point2 = Point(1, 1)
    point3 = Point(1.5, 1.5)
    point4 = Point(4, 5)
    point5 = Point(1, 0.5)

    # Creating segments
    segmentA = Segment(point1, point2)  # Leftmost point is (1, 1)
    segmentB = Segment(point3, point4)  # Leftmost point is (1.5, 1.5)
    segmentC = Segment(point5, point4)  # Leftmost point is (1, 0.5)

    # Test leftmostPoint
    assert segmentA.leftmostPoint() == point2, "Test 1 Failed"
    assert segmentB.leftmostPoint() == point3, "Test 2 Failed"
    assert segmentC.leftmostPoint() == point5, "Test 3 Failed"

    # Test ordering (__lt__)
    assert segmentA < segmentB, "Test 4 Failed"  # Because (1, 1) is to the left of (1.5, 1.5)
    assert not segmentB < segmentA, "Test 5 Failed"  # Opposite of Test 4
    assert segmentC < segmentB, "Test 6 Failed"  # Both have x=1, but y=0.5 < y=1.5

    # Test equality (__eq__)
    segmentD = Segment(Point(3, 3), point2)  # Leftmost point is still (1, 1)
    assert segmentA == segmentD, "Test 7 Failed"
    assert not segmentA == segmentB, "Test 8 Failed"
    assert not segmentA == segmentC, "Test 9 Failed"

    print("All leftmost point and ordering tests passed passed!")

test_orientation()
testPointOnSegment()
testSegmentIntersect()
testLeftmostPointAndOrdering()