import collections
def intersection_array(num1,num2):
    c = collections.Counter(nums1) and  collections.Counter(nums2)
    ans = []
    for k, v in c.items():
        ans.append([k]* v)
    return ans
nums1 = [1,2,2,1]
nums2 = [2,2]
intersection_array(nums1,nums2)
