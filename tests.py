from models import *

def test_orientation():

    # Test 1: If p0p1 is oriented clockwise in relation to p0p2
    p0 = Point(0, 0)
    p1 = Point(1, 1)
    p2 = Point(1, 2)
    seg1 = Segment(p0, p1)
    assert orientation(seg1, p2) > 0, "Test 1 Failed"

    # Test 2: If p0p1 is oriented counter-clockwise in relation to p0p3
    p3 = Point(2, 0)
    assert orientation(seg1, p3) < 0, "Test 2 Failed"

    # Test 3: If p0p1 is colinear to p0p4
    p4 = Point(2, 2)
    assert orientation(seg1, p4) == 0, "Test 3 Failed"

    # Test 4: If p5p6 is colinear to p5p7 (all points y axis)
    p5 = Point(0, 0)
    p6 = Point(0, 1)
    seg2 = Segment(p5, p6)
    p7 = Point(0, 2)
    assert orientation(seg2, p7) == 0, "Test 4 Failed"

    # Test 5: If p8p9 is colinear to p8p10 (all points x axis)
    p8 = Point(0, 0)
    p9 = Point(1, 0)
    seg3 = Segment(p8, p9)
    p10 = Point(2, 0)
    assert orientation(seg3, p10) == 0, "Test 5 Failed"

    # Test 6: If p11p12 is oriented counter-clockwise in relation to p11p13 (all negative coordinates)
    p11 = Point(-2, -2)
    p12 = Point(-3, -3)
    seg4 = Segment(p11, p12)
    p13 = Point(-4, -2)
    assert orientation(seg4, p13) < 0, "Test 6 Failed"

    print("All orientation tests passed!")

def testPointOnSegment():

    # Test 1: Point on the segment
    p0 = Point(1, 1)
    p1 = Point(2, 2)
    seg1 = Segment(p0, p1)
    assert pointOnSegment(seg1, p1) == True, "Test 1 Failed"

    # Test 2: Point off the segment but on the line extended from the segment
    p2 = Point(3, 3)
    assert pointOnSegment(seg1, p2) == False, "Test 2 Failed"

    # Test 3: Point outside the line formed by the segment
    p3 = Point(2, 3)
    assert pointOnSegment(seg1, p3) == False, "Test 3 Failed"

    # Test 4: Point exactly at the start of the segment
    assert pointOnSegment(seg1, p0) == True, "Test 4 Failed"

    # Test 5: Point inside the segment, but not at start or end
    p4 = Point(1.5, 1.5)
    assert pointOnSegment(seg1, p4) == True, "Test 5 Failed"

    # Test 6: Point lying on the vertical segment
    p5 = Point(2, 0)
    p6 = Point(2, 3)
    p7 = Point(2, 1.5)
    seg2 = Segment(p5, p6)
    assert pointOnSegment(seg2, p7) == True, "Test 6 Failed"

    print("All points on segment tests passed!")

def testSegmentIntersect():
    # Test 1: Segments that intersect
    p0 = Point(1, 1)
    p1 = Point(2, 2)
    p2 = Point(3, 2.5)
    seg1 = Segment(p0, p1)
    seg2 = Segment(p1, p2)
    assert segmentIntersect(seg1, seg2) == True, "Test 1 Failed"

    # Test 2: Segments that intersect
    p1 = Point(1, 1.5)
    p2 = Point(3, 1.5)
    p3 = Point(2, 2)
    p4 = Point(2, 1)
    seg1 = Segment(p1, p2)
    seg2 = Segment(p2, p3)
    assert segmentIntersect(seg1, seg2) == True, "Test 2 Failed"

    # Test 3: Segments that don't intersect (colinear)
    p1 = Point(1, 1.5)
    p2 = Point(3, 1.5)
    p3 = Point(4, 1.5)
    p4 = Point(5, 1.5)
    seg1 = Segment(p1, p2)
    seg2 = Segment(p3, p4)
    assert segmentIntersect(seg1, seg2) == False, "Test 3 Failed"

    # Test 4: Segments that intersect (colinear)
    p1 = Point(1, 1.5)
    p2 = Point(3, 1.5)
    p3 = Point(2, 1.5)
    p4 = Point(5, 1.5)
    seg1 = Segment(p1, p2)
    seg2 = Segment(p3, p4)
    assert segmentIntersect(seg1, seg2) == True, "Test 4 Failed"

    # Test 5: Segments that intersect on one point, perpendicular to each other (forming a right angle)
    p1 = Point(1, 1.5)
    p2 = Point(3, 1.5)
    p3 = Point(2, 2)
    p4 = Point(2, 1.5)
    seg1 = Segment(p1, p2)
    seg2 = Segment(p3, p4)
    assert segmentIntersect(seg1, seg2) == True, "Test 5 Failed"

    # Test 6: Segments that don't intersect, parallel to each other
    p1 = Point(1, 1)
    p2 = Point(3, 1)
    p3 = Point(1, 2)
    p4 = Point(3, 2)
    seg1 = Segment(p1, p2)
    seg2 = Segment(p3, p4)
    assert segmentIntersect(seg1, seg2) == False, "Test 6 Failed"

    # Test 7: Segments that intersect at one end
    p1 = Point(1, 1)
    p2 = Point(3, 1)
    p3 = Point(3, 1)
    p4 = Point(3, 2)
    seg1 = Segment(p1, p2)
    seg2 = Segment(p3, p4)
    assert segmentIntersect(seg1, seg2) == True, "Test 7 Failed"

    print("All segment intersect tests passed!")

test_orientation()
testPointOnSegment()
testSegmentIntersect()
