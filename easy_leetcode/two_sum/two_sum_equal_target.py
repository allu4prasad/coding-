

from typing import List
def all_two_sum_combinations(nums:List[int],target:int)->List[int]:
    combinations=[]
    seen=set()
    for i in nums:
        if target-i in seen:
            combinations.append((i,target-i))
        seen.add(i)
    return combinations

# nums=list(x)
# target=40
# all_two_sum_combinations(nums,target)   
# [(21, 19),
#  (22, 18),
#  (23, 17),
#  (24, 16),
#  (25, 15),
#  (26, 14),
#  (27, 13),
#  (28, 12),
#  (29, 11),
#  (30, 10),
#  (31, 9),
#  (32, 8),
#  (33, 7),
#  (34, 6),
#  (35, 5),
#  (36, 4),
#  (37, 3),
#  (38, 2),
#  (39, 1),
#  (40, 0)]
