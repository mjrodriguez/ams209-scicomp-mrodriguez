""""
Problem 3 = Need to check whether the list is sorted or not.
"""


def is_sorted(someList):
    someListCopy = []
    someListCopy.extend(someList)  # Create a copy of the list
    someListCopy.sort()            # sort the copy of the list

    sorted = 1 # sorted checker
    
    # here i am going to compare the elements from the sorted copy and original list
    for i in range(0,len(someList)):
        if someList[i] != someListCopy[i]:
            sorted = 0
            print 'False'
            break
            
    
    if sorted == 1:
        print 'True'
    
# ^ Function definition above
#####################################################################################

#x = [1,3,2]
x = [1,2,3]
is_sorted(x)