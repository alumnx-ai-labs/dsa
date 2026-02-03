# ==================== BRUTE FORCE SOLUTION ====================
# Time Complexity: O(n²) - nested loops comparing each element
# Space Complexity: O(1) - only storing the max value
def find_largest_brute(nums):
    # Assume first element is the largest
    max_element = nums[0]
    
    # Outer loop: iterate through each element
    for i in range(len(nums)):
        is_largest = True
        
        # Inner loop: compare current element with all others
        for j in range(len(nums)):
            # If we find any element larger, current is not the largest
            if nums[j] > nums[i]:
                is_largest = False
                break
        
        # If current element is larger than all others, update max
        if is_largest:
            max_element = nums[i]
    
    return max_element


# ==================== SORTING SOLUTION ====================
# Time Complexity: O(n log n) - sorting the array
# Space Complexity: O(n) - creating sorted copy
def find_largest_sorting(nums):
    # Sort the array in ascending order
    sorted_nums = sorted(nums)
    
    # Return the last element (largest)
    return sorted_nums[-1]


# ==================== SORTING SOLUTION (IN-PLACE) ====================
# Time Complexity: O(n log n) - sorting the array
# Space Complexity: O(1) - sorting in-place (modifies original array)
def find_largest_sorting_inplace(nums):
    # Sort the array in-place
    nums.sort()
    
    # Return the last element (largest)
    return nums[-1]


# ==================== OPTIMAL SOLUTION ====================
# Time Complexity: O(n) - single pass through array
# Space Complexity: O(1) - only storing the max value
def find_largest_optimal(nums):
    # Initialize max with first element
    max_element = nums[0]
    
    # Iterate through array once
    for i in range(1, len(nums)):
        # Update max if current element is larger
        if nums[i] > max_element:
            max_element = nums[i]
    
    return max_element


# ==================== ALTERNATIVE OPTIMAL (PYTHONIC) ====================
# Time Complexity: O(n) - built-in max function
# Space Complexity: O(1)
def find_largest_pythonic(nums):
    return max(nums)


# ==================== TEST CASES ====================
print("=== BRUTE FORCE SOLUTION ===")
print(find_largest_brute([2, 5, 1, 3, 0]))      # 5
print(find_largest_brute([8, 10, 5, 7, 9]))     # 10
print(find_largest_brute([-5, -2, -8, -1]))     # -1
print(find_largest_brute([100]))                # 100

print("\n=== SORTING SOLUTION ===")
print(find_largest_sorting([2, 5, 1, 3, 0]))    # 5
print(find_largest_sorting([8, 10, 5, 7, 9]))   # 10
print(find_largest_sorting([-5, -2, -8, -1]))   # -1
print(find_largest_sorting([100]))              # 100

print("\n=== OPTIMAL SOLUTION ===")
print(find_largest_optimal([2, 5, 1, 3, 0]))    # 5
print(find_largest_optimal([8, 10, 5, 7, 9]))   # 10
print(find_largest_optimal([-5, -2, -8, -1]))   # -1
print(find_largest_optimal([100]))              # 100

print("\n=== PYTHONIC SOLUTION ===")
print(find_largest_pythonic([2, 5, 1, 3, 0]))   # 5
print(find_largest_pythonic([8, 10, 5, 7, 9]))  # 10
print(find_largest_pythonic([-5, -2, -8, -1]))  # -1
print(find_largest_pythonic([100]))             # 100