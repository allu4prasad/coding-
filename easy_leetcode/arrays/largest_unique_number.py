class Solution(object):
    def largestUniqueNumber(self, nums):

        curr_key = 0
        largest_key = -1
        nums_dict = {} 

        for i in nums:
            nums_dict[i] = nums_dict.get(i, 0) + 1
        
        for key, value in nums_dict.items():
            if value < 2:
                curr_key = key
                largest_key = max(curr_key, largest_key)

        return largest_key
