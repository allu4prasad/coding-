# You are given a string number representing a positive integer and a character digit.

# Return the resulting string after removing exactly one occurrence of digit from number such that the value of the resulting string in decimal form is maximized. The test cases are generated such that digit occurs at least once in number.


class Solution(object):
    def removeDigit(self, number, digit):
        max_val = 0
        count=0
        new=list(number)
        if new.count(str(digit))==1:
            new.remove(str(digit))
            return ''.join(new)
        else:
            for i in range(len(number)):
                if number[i]==digit:
                    temp=number[:i]+number[i+1:]
                    max_val=max(max_val,temp)
                    count=+1
   
        return max_val
