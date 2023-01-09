def find_combinations(target):
  # Create an empty list to store the combinations
  combinations = []

  # Iterate over the numbers from 1 to half of the target
  for num1 in range(1, target // 2 + 1):
    # Find the number that would make the sum equal to the target
    num2 = target - num1
    # Add the combination to the list
    combinations.append((num1, num2))
  
  return combinations

# Find all combinations that add up to 10
combinations = find_combinations(10)
print(combinations)
