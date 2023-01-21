class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        x={}
        for i in range(len(arr)):
            if arr[i] not in x:
                x[arr[i]]=1
            else:
                x[arr[i]]=x[arr[i]]+1
        if len(x)==len(set(x.values())):
            return True
        else:
            return False

