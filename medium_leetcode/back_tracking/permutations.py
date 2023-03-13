def permute(nums):
    def bck_track(first=0):
        if first==n:
            output.append(nums[:])
        for i in range(first,n):
            nums[first],nums[i]=nums[i],nums[first]
            bck_track(first+1)
            nums[first],nums[i]=nums[i],nums[first]
    n=len(nums)
    output=[]
    bck_track()
    return output
nums = [1, 2, 3]
result = permute(nums)
print(result)
    
        
