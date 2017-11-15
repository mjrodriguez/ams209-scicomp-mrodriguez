"""
Homework 5: Problem 3
Unit Conversion - The dictionary is represented by units/meters. 
Therefore, the given units are converted to meters and then the dictionary is used
to display all the other converted units.
"""

def unitConversion(length,unitSystem):
    
    # Defining the dictionary
    unitDictionary = {'meters':1.0, 'miles':0.000621, 'inches':39.370079, 'feet':3.28084, 'yards':1.093613}
    siDictionary   = {'nm': 10**9, 'um': 10**6, 'mm': 10**3, 'cm': 10**2, 'km': 10**(-3)}
    
    # This loop picks out the right value to convert given units to meters
    for k, v in unitDictionary.items():
        if k == unitSystem:
            convertToMetersValue = v
    
    # Converting Units using unitDictionary     
    lengthConverted = dict()
    for d in unitDictionary:
        lengthConverted[d] = length/convertToMetersValue*unitDictionary[d]
    print lengthConverted 
    
    # Converting Units using siDictionary     
    lengthSi = dict()
    for d in siDictionary:
        lengthSi[d] = length/convertToMetersValue*siDictionary[d]
    print lengthSi 
        
        
if __name__ == "__main__":
    print('\n10 yards: ')
    unitConversion(10,'yards')
    print('\n159 yards:')
    unitConversion(159,'yards')