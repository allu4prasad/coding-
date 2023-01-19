def strobogramm(number):
    rotated_digits = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
    left=0
    right=len(number)-1
    while left<=right:
        if  rotated_digits[number[left]]!=number[right]:
            return False
        left=left+1
        right=right-1
        
    return True
number='691'
strobogramm(number)
