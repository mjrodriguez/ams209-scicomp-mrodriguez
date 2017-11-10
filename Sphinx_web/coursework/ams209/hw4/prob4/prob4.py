def cumulativeSum(list):
    x = []
    sum = 0
    for i in range(0,len(list)):
        sum += list[i]
        x.append(sum)
        
    print x

#####################################################################################      
# ^ Function definition above
#####################################################################################      

cumulativeSum([1,2,3])