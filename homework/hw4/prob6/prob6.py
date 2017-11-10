def palindrome(word):
    
    if word[0] == word[(len(word)-1)]:
        palindrome(word[1:(len(word)-2)])
    else:
        return False
    
    return True
            
#####################################################################################      
# ^ Function definition above
#####################################################################################

isIt = palindrome('not')
print isIt