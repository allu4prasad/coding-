def removeVowels( s):
    """
    :type s: str
    :rtype: str
    """
    results=''
    vowels='aeiou'
    for i in s:
        if  not i in list(vowels):
            results=results+i

    return results
