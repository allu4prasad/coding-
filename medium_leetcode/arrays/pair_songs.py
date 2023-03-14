class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        c=[0]*60
        results=0
        for i in range(len(time)):
            y= time[i]%60
            if y>0:
                results=results+c[60-y]
            else:
                results=results+c[0]
            c[y]=c[y]+1
        return results 
