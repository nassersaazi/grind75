def twoSum(nums, target):
    """
    Finds the indices of two numbers in a list that add up to a target value.

    Args:
        nums: A list of integers.
        target: The target integer.

    Returns:
        A list of two integers representing the indices of the two numbers
        that add up to the target. Returns an empty list if no solution is found.
    """
    num_map = {}  # Dictionary to store numbers and their indices
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []  # Return an empty list if no solution is found.

def main():
    """
    Main function to demonstrate the usage of twoSum function.
    """
    test_cases = [
        ([2, 7, 11, 15], 9),
        ([3, 2, 4], 6),
        ([3, 3], 6),
        ([-1, -2, -3, -4, -5], -8),
    ]
    for nums, target in test_cases:
        result = twoSum(nums, target)
        print(f"Input: nums = {nums}, target = {target}, Indices = {result}")

if __name__ == "__main__":
    main()
