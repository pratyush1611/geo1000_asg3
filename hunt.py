# GEO1000 - Assignment 3
# Authors:
# Studentnumbers:

def read_grid(filenm):
    f = open(filenm, "r")
    data = [f.read()]   
    coord = []

    for i in data:
        for x in i:
            if str.isdigit(x):
                coord.append(x)
    tuple_coord = [(int(coord[i]), int(coord[i+1])) for i in range(0,len(coord),2)]   
    datastr = [[tuple_coord[i],tuple_coord[i+1],tuple_coord[i+2],tuple_coord[i+3],tuple_coord[i+4]] for i in range(0,len(tuple_coord),5)]
    
    return datastr

def visit(table, steps_allowed, path):
    treasure = (4,1)
    start = (0,0)
    path.append(start)
    steps_allowed -= 1 
           
    while steps_allowed > 0:
        for i in path:
            print(i)
            print("sa",steps_allowed)
            if i == path[-1]:
                print("i",i)
                row = i[0]
                col = i[1]
                print(row,col)
                x,z = tuple(x for x in (table[row])[col])
                path.append((x,z))
                print((x,z))
                print("2",steps_allowed)
                steps_allowed -= 1 
            
            if (x,z) == treasure:
                print("finalstep", steps_allowed)
                return True
            if steps_allowed == 0:
                print("breakstep", steps_allowed)
                return False

def hunt(filenm, max_steps):
    table = read_grid(filenm)
    print(table)
    steps_allowed = max_steps
    path = []
    
    result  = visit(table, steps_allowed, path)
    print(path)
    N = len(path)
    X,Y = (path[-1])

    if result == True:
        return f"The treasure was found at row: {X}, column: {Y}; it took {N} steps to find the treasure."
    if result == False:
        return f"Could not find a treasure (in {N} steps)."
    

if __name__ == "__main__":
    print(hunt('finite.txt', 20))
