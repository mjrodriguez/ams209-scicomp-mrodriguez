"""
Homework 5:
- Prob1.py --> Need to read in file words.txt and print the first N lines
"""

def readNLinesToList(N):
    fn = open('words.txt')
    nWords = []
    counter = 0
    for line in fn:
        word = line.strip()
        nWords.append(word)
        counter += 1
        
        if counter == N:
            return nWords
            break
            
def readLinesToList():
    fn = open('words.txt')
    nWords = []
    for line in fn:
        word = line.strip()
        nWords.append(word) 
                
    return nWords 


def readNLinesToDict(N):
    fn = open('words.txt')
    wordDict = {}
    counter = 0
    for line in fn:
        word = line.strip()
        wordDict[word] = counter 
        counter += 1
        if counter == N:
            return wordDict
            break     
    
def readLinesToDict():
    fn = open('words.txt')
    wordDict = {}
    counter = 0
    for line in fn:
        word = line.strip()
        wordDict[word] = counter 
        counter += 1
                
    return wordDict 
       
        
if __name__ == "__main__":
    #wordList = readNLinesToList(50)
    #wordList = readLinesToList()
    wordList = readLinesToDict()
    #wordList = readNLinesToDict(5)
    print 'is aa in dicitonary?'
    print 'aa' in wordList
    print len(wordList)
    #print wordList
    #print wordList.keys()
    
 