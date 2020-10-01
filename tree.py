# GEO1000 - Assignment 3
# Authors: Simon Pena Pereira & Pratyush Kumar
# Studentnumbers: 5391210 & 5359252
#%%
import math
#%%
def distance(p1, p2):
    """Returns Cartesian distance (as float) between two 2D points"""
    return( math.sqrt( (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 ) )


def point_angle_distance(pt, beta, distance):
    """Compute new point that is distance away from pt in direction beta"""
    x2,y2 = (  pt[0] + (distance * math.cos(beta))  ), (  pt[1] + (distance * math.sin(beta))  )
    return( x2, y2 )


def absolute_angle(p1, p2):
    """Returns the angle (in radians) between the positive x-axis 
    and the line through two given points, p1 and p2"""
    return( math.atan2( p2[1] - p1[1] , p2[0] - p1[0]  ) )


def opposite_edge(p1, p2):
    """Compute edge parallel to the edge defined by the two given points 
    p1 and p2 (i.e. the opposite edge in the square).
    """
    
    theta_p3 = absolute_angle(p1, p2) + (math.pi/4)
    theta_p4 = absolute_angle(p1, p2) + (math.pi/2)

    dist_p3 = distance(p1, p2)/(math.cos(math.pi/4))
    dist_p4 = distance(p1, p2)
    

    p3 = point_angle_distance(p1, theta_p3, dist_p3)
    p4 = point_angle_distance(p1, theta_p4, dist_p4)
    return( p3, p4 )


def split_point(p1, p2, alpha):
    """Returns the point above this top edge that defines 
    the two new boxes (together with points p1 and p2 of the top edge).
    """
    # theta = absolute_angle(p1, p2)
    dist = math.cos(alpha) * distance(p1, p2)
    
    return(  )


def as_wkt(p1, p2, p3, p4):
    """Returns Well Known Text string (POLYGON) for 4 points 
    defining the square
    """
    pass


def draw_pythagoras_tree(p1, p2, alpha, currentorder, totalorder, filename):
    pass


if __name__ == "__main__":
    with open('out.wkt', 'w') as fh:  # 'with' statement closes 
                                      # file automatically
        fh.write("geometry;currentorder;area\n")

    draw_pythagoras_tree(p1=(5,0), 
        p2=(6,0), 
        alpha=math.radians(45),
        currentorder=0,
        totalorder=6,
        filename='out.wkt')
