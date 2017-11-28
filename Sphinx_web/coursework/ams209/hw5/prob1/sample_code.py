"""
An example file for hw5.
(1) It reads in lines from an ASCII file, 'words.txt', using open(); and saves it to fn
(2) Now fn is a "file object" (Try uncommenting linenumbers 10 and 11).
(3) Use strip(), a method defined in file object, to get rid of whitespace characters (e.g., a carraige return and a new line).
    To see how strip() makes a difference, try commenting linenumber 14 and uncomment linenumber 15. 
"""

fn = open('words.txt')
#print fn
#print type(fn)
for line in fn:
    word = line.strip()
    print word
    #print line