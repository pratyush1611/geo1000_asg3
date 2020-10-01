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
    pass


def opposite_edge(p1, p2):
    """Compute edge parallel to the edge defined by the two given points 
    p1 and p2 (i.e. the opposite edge in the square).
    """
    pass


def split_point(p1, p2, alpha):
    """Returns the point above this top edge that defines 
    the two new boxes (together with points p1 and p2 of the top edge).
    """
    pass


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
