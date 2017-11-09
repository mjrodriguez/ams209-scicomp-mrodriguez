"""
Problem 5 = Need to implement a function that capitalizes the first letter in our name. 
Additionally we also need to overload the function so that it takes two arguments and reverses
our name order.
"""
def print_yourName(*args):
    
    # Single argument implementation
    if len(args) == 1:
        
        nameAsList = args[0]
        
        lengthOfFirstName = len(nameAsList[0])
        lengthOfLastName = len(nameAsList[1])
        print(nameAsList[0][0].upper()+nameAsList[0][1:lengthOfFirstName]+' '+nameAsList[1][0].upper()+nameAsList[1][1:lengthOfLastName])
    
    # Double arugment implementation
    elif len(args) == 2:
        
        nameAsList = args[0]
        flip = args[1]
        
        lengthOfFirstName = len(nameAsList[0])
        lengthOfLastName = len(nameAsList[1])
        if flip:
            print(nameAsList[0][0].upper()+nameAsList[0][1:lengthOfFirstName]+' '+nameAsList[1][0].upper()+nameAsList[1][1:lengthOfLastName])
        else:
            print(nameAsList[1][0].upper()+nameAsList[1][1:lengthOfLastName] + ', ' + nameAsList[0][0].upper()+nameAsList[0][1:lengthOfFirstName] )
        

# ^ Function definition above
#####################################################################################

# Single argument function
print('This Prints from a Single Argument Function: ')
print_yourName(['martin','rodriguez'])
print ' '
# Two argument function
print('This Prints from a Double Argument Function: ')
print_yourName(['martin','rodriguez'], False)