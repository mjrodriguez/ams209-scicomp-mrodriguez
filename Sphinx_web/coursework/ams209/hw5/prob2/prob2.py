# Takes the second element of the tuple which is the char frequency
def charFrequency(element):
    return element[1]
    
    
def characterCounter(fileName):
    # Converting fileName into giant string
    fstring = open(fileName).read()
    
    # Creating empty dictionary to store chars
    d = dict()
    
    # Cycling through chars in giant string
    for c in fstring:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    
    # displaying dictionary as tuples
    dTuple = d.items()  # converts dictionary to list of tuples
    dTuple.sort(key=charFrequency, reverse=True) # sorts tuples based on frequency
    
    # Prints tuples
    for i in range(0,len(dTuple)):
        print dTuple[i]
        
    
    


if __name__ == "__main__":
    characterCounter('words.txt')