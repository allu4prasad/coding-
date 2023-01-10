#1
def create_target_array(nums, index):
    target = []
    for i in range(len(nums)):
        target.insert(index[i], nums[i])
    return target
#2
class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        results=[]
        for i,j in zip(index,nums):
            results[i:i]=[j]
        return results
