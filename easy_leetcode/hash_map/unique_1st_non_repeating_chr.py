class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        res={}
        for i in s:
            if i in res:
                res[i]=res[i]+1
            else:
                res[i]=1
        for j in s:
            if res[j]==1:
                return s.index(j)
                break
        else:
            return -1
