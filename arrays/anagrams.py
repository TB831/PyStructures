def anagram(s1, s2):
    '''
    Given two strings, check to see if they are anagrams.
    An anagram is when the two strings can be written using the
    exact same letters (so you can just rearrange the letters to
    get a different phrase or word).
    '''
    return sorted(s1) == sorted(s2)

def cleanString(str):
    '''
    Function to clean a string
    '''
    clean = sorted(str.lower().replace(" ", ""))
    return ''.join(clean)


# Test Cases
anagram('dog','god')
anagram('clint eastwood','old west action')
anagram('aa','bb')
