# Fredo is assigned a new task today. He is given an array A containing N integers. His task is to update all elements of array to some minimum value x , that is,  ;  such that sum of this new array is strictly greater than the sum of the initial array. Note that x should be as minimum as possible such that sum of the new array is greater than the sum of the initial array.
def min_sum(numbers):
    n_sum=sum(numbers)
    x=min(numbers)-1
    new_sum=0
    while new_sum<=n_sum:
        x=x+1
        new_sum=x*len(numbers)
    for i in range(len(numbers)):
        numbers[i]=x
    return numbers
numbers=[1,2,3,4,5]
min_sum(numbers)       
