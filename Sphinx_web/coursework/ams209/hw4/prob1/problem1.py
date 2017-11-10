"""
problem1.py: Writing a function such that the text is left justified
"""

def right_justify(name):
    lengthName = len(name)
    numberOfSpaces = 70 - lengthName
    space = ' '
    print( numberOfSpaces*space + name )
    


right_justify('Mike')
    