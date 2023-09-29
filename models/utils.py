# Receives a list of segments and returns a 
# list of points from those segments
def extractPointsFromSegments(segments):
  
    points = []
  
    for segment in segments:
        points.append(segment.origin)
        points.append(segment.destination)
    
    return points
