def toTriangleOrNot(x,y,z):
    if x < y+z and y < x+z and z < x+y:
        return True
    else:
        return False
        
        
#####################################################################################      
# ^ Function definition above
#####################################################################################

isIt = toTriangleOrNot(5,4,10)
print isIt