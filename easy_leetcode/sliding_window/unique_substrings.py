class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        x=0
        y=3
        results=[]
        for i in range(len(s)):
            sub_str=s[x:y]
            if len(sub_str)!=3:
                continue
            x=x+1
            y=y+1
            if len(set(sub_str))==3:
                results.append(sub_str)
        return len(results)
        
