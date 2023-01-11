def largestSubarray(nums,k):
    mIndex = 0
    maxx = 0
    for i in range(len(nums)-k+1):
        if nums[i]>maxx:
            maxx = nums[i]
            mIndex = i
    return nums[mIndex:mIndex+k]
