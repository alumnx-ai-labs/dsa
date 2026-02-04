# ==================== BRUTE FORCE SOLUTION ====================
# Time Complexity: O(n²) - creating new array and copying elements
# Space Complexity: O(n) - for the temporary result array
def remove_elements_brute(nums, val):
    """
    Brute Force Approach:
    - Create a new temporary array
    - Iterate through original array and copy elements >= val
    - Copy back to original array
    """
    # Create temporary array to store valid elements
    temp = []
    
    # Iterate through all elements
    for i in range(len(nums)):
        # If element is >= val, add to temp array
        if nums[i] >= val:
            temp.append(nums[i])
    
    # Copy elements back to original array
    for i in range(len(temp)):
        nums[i] = temp[i]
    
    # Return count of valid elements
    return len(temp)


# ==================== OPTIMAL SOLUTION (Two Pointers) ====================
# Time Complexity: O(n) - single pass through array
# Space Complexity: O(1) - only using two pointers, in-place modification
def remove_elements_optimal(nums, val):
    """
    Two Pointer Approach:
    - Use 'k' as slow pointer to track position for valid elements
    - Use 'i' as fast pointer to scan through array
    - When we find element >= val, place it at position k and increment k
    
    Visualization for [0,1,2,2,3,0,4,2], val=2:
    
    i=0: nums[0]=0 < 2, skip (k=0)
    i=1: nums[1]=1 < 2, skip (k=0)
    i=2: nums[2]=2 >= 2, nums[0]=2, k=1 → [2,1,2,2,3,0,4,2]
    i=3: nums[3]=2 >= 2, nums[1]=2, k=2 → [2,2,2,2,3,0,4,2]
    i=4: nums[4]=3 >= 2, nums[2]=3, k=3 → [2,2,3,2,3,0,4,2]
    i=5: nums[5]=0 < 2, skip (k=3)
    i=6: nums[6]=4 >= 2, nums[3]=4, k=4 → [2,2,3,4,3,0,4,2]
    i=7: nums[7]=2 >= 2, nums[4]=2, k=5 → [2,2,3,4,2,0,4,2]
    
    Result: k=5, first 5 elements are [2,2,3,4,2]
    """
    # Initialize pointer k to track position for next valid element
    k = 0
    
    # Iterate through array with fast pointer i
    for i in range(len(nums)):
        # If current element is >= val, it should be kept
        if nums[i] >= val:
            # Place element at position k
            nums[k] = nums[i]
            # Move k pointer forward
            k += 1
    
    # Return count of valid elements
    return k


# ==================== ALTERNATIVE OPTIMAL SOLUTION ====================
# Time Complexity: O(n) - single pass through array
# Space Complexity: O(1) - in-place modification
def remove_elements_swap(nums, val):
    """
    Swap Approach (Alternative):
    - When we find element < val, swap with element from end
    - Decrease array size consideration
    - Continue until we've checked all relevant positions
    """
    # Start from the end of array
    n = len(nums)
    i = 0
    
    while i < n:
        # If current element is < val, swap with last element
        if nums[i] < val:
            nums[i] = nums[n - 1]
            n -= 1  # Reduce the size we're considering
        else:
            i += 1  # Move to next element only if current is valid
    
    return n


# ==================== TEST CASES ====================
print("=== BRUTE FORCE SOLUTION ===")
nums1 = [3, 2, 2, 3]
k1 = remove_elements_brute(nums1, 3)
print(f"Input: [3,2,2,3], val=3 → k={k1}, nums={nums1[:k1]}")  # k=2, nums=[3,3]

nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
k2 = remove_elements_brute(nums2, 2)
print(f"Input: [0,1,2,2,3,0,4,2], val=2 → k={k2}, nums={nums2[:k2]}")  # k=5

nums3 = [1, 2, 3, 4, 5]
k3 = remove_elements_brute(nums3, 3)
print(f"Input: [1,2,3,4,5], val=3 → k={k3}, nums={nums3[:k3]}")  # k=3, nums=[3,4,5]

nums4 = [5, 5, 5, 5]
k4 = remove_elements_brute(nums4, 10)
print(f"Input: [5,5,5,5], val=10 → k={k4}, nums={nums4[:k4]}")  # k=0


print("\n=== OPTIMAL SOLUTION (Two Pointers) ===")
nums5 = [3, 2, 2, 3]
k5 = remove_elements_optimal(nums5, 3)
print(f"Input: [3,2,2,3], val=3 → k={k5}, nums={nums5[:k5]}")  # k=2, nums=[3,3]

nums6 = [0, 1, 2, 2, 3, 0, 4, 2]
k6 = remove_elements_optimal(nums6, 2)
print(f"Input: [0,1,2,2,3,0,4,2], val=2 → k={k6}, nums={nums6[:k6]}")  # k=5

nums7 = [1, 2, 3, 4, 5]
k7 = remove_elements_optimal(nums7, 3)
print(f"Input: [1,2,3,4,5], val=3 → k={k7}, nums={nums7[:k7]}")  # k=3, nums=[3,4,5]

nums8 = [5, 5, 5, 5]
k8 = remove_elements_optimal(nums8, 10)
print(f"Input: [5,5,5,5], val=10 → k={k8}, nums={nums8[:k8]}")  # k=0


print("\n=== SWAP APPROACH (Alternative) ===")
nums9 = [3, 2, 2, 3]
k9 = remove_elements_swap(nums9, 3)
print(f"Input: [3,2,2,3], val=3 → k={k9}, nums={nums9[:k9]}")  # k=2

nums10 = [0, 1, 2, 2, 3, 0, 4, 2]
k10 = remove_elements_swap(nums10, 2)
print(f"Input: [0,1,2,2,3,0,4,2], val=2 → k={k10}, nums={nums10[:k10]}")  # k=5


# ==================== COMPLEXITY COMPARISON ====================
print("\n=== COMPLEXITY ANALYSIS ===")
print("""
┌─────────────────────┬──────────────────┬──────────────────┐
│     Approach        │ Time Complexity  │ Space Complexity │
├─────────────────────┼──────────────────┼──────────────────┤
│ Brute Force         │ O(n²)            │ O(n)             │
│ Two Pointers        │ O(n)             │ O(1)             │
│ Swap Approach       │ O(n)             │ O(1)             │
└─────────────────────┴──────────────────┴──────────────────┘

Best Approach: Two Pointers (Optimal)
- Single pass through array
- In-place modification (no extra space)
- Maintains relative order of elements
""")