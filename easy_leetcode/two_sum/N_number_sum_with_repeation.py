def find_N_number_sum_combination(nums,target,partial=[]):
    if sum(partial)==target:
        combination.append(partial)
    for index,num in enumerate(nums):
        remaining=nums[index+1:]
        find_N_number_sum_combination(remaining,target,partial+[num])

combination = []
find_N_number_sum_combination([1, 2, 3, 4,6,5,7, 5], 10)
print(combination)
