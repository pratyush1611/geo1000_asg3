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
    theta = absolute_angle(p1, p2) #angle b/w edge and x axis 
    # theta=0
    dist = math.cos(alpha) * distance(p1, p2) #dist of p3 fom p1
    p3 = point_angle_distance(p1, alpha+theta , dist)
    return( p3 )


def as_wkt(p1, p2, p3, p4):
    """Returns Well Known Text string (POLYGON) for 4 points 
    defining the square
    """
    fin=str()
    for i in enumerate( (p1,p2,p3,p4) ):
        if i[0]==0 : #first iteration
            fin = (" ".join([str(_) for _ in  list(i[1])])).rstrip()
        else:
            fin = fin +','+(" ".join([str(_) for _ in  list(i[1])])).rstrip()
    return("POLYGON " + "(("+fin + "))")


def draw_pythagoras_tree(p1, p2, alpha, currentorder, totalorder, filename):
    currentorder=0
    while currentorder<=totalorder:
        p3,p4 = opposite_edge(p1, p2) # square complete
        p5 = split_point(p3,p4,alpha) 
        wkt_to_file = as_wkt(p1,p2,p3,p4) + ';' + str(currentorder) + ';' + str((distance(p1,p2)**2))
        with open(filename,'a') as fh:
            fh.write( '\n'+wkt_to_file)
        #recursion to come here
        currentorder +=1
        draw_pythagoras_tree(p3, p5, alpha, currentorder, totalorder, filename)
        draw_pythagoras_tree(p4, p5, alpha, currentorder, totalorder, filename)
    


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

# %%
