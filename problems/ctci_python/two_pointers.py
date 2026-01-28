def palindrome(s):
    l, r = 0, len(s) - 1

    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


"""
Given Two Sorted Lists, Find elements appearing in both arrays. 

27.3 - Array Intersection

arr1 = [1, 3, 5]
           p1

arr2 = [1, 2, 3]
              p2


- Have 2 pointers set at the start of the arrays
- Compare the elements of both the pointers. 
    - If arr1[p1] < arr2[p2]: Increment the p1 in arr1. Until the p1 < len(arr1). In this case, return.
    - If arr1[p1] > arr2[p2]: Increment the p2 in arr2. Until the p2 < len(arr2). In this case, return.
    - If arr1[p1] == arr2[p2]: Add the elem to result array. Increment both p1, p2 in arr1 and arr2 corr

"""

def array_intersection(arr1, arr2):
    p1, p2 = 0, 0

    res = []

    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] < arr2[p2]:
            p1 += 1
        elif arr1[p1] > arr2[p2]:
            p2 += 1
        elif arr1[p1] == arr2[p2]:
            res.append(arr1[p1])
            p1 += 1
            p2 += 1
    return res


"""
Palindromic Sentence

Check if the string is a palindrome, by ignoring punctuation.

s = "Bob wondered, 'Now, Bob?'"
     i                      j

- To work with palindromes, initialize two pointers.
- Iterate through the given input string inwards ignoring any punctuation using isalpha check.
    - If isalpha check fails, increment the i pointer or decrement the j pointer accordingly 
    - If isalpha check succeeds, check if the lower case of element matches. else return False
    - Continue until, i and j meet if odd or i and j coinside if even. return

"""

def palindromic_sentence(s):
    i, j = 0, len(s) - 1

    while i < j:
        if not s[i].isalpha():
            i += 1
        elif not s[j].isalpha():
            j -= 1
        else:
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
    return True


"""
Merge Two Sorted Arrays

Input:

arr1 = [1, 3, 4, 5]
        p1

arr2 = [2, 4, 4]
        p2
        
Output: [1, 2, 3, 4, 4, 4, 5]

- Initialize two pointers p1 and p2 in corr arr1 and arr2 and result array
- Compare both the elements. 
    - If arr1[p1] < arr2[p2], then append arr1[p1] to result array. Then Increment the p1.
    - If arr1[p1] > arr2[p2], then append arr2[p2] to result array. Then Increment the p2.
    - If arr1[p1] == arr2[p2], then append arr1[p1], arr2[p2] to result array. Then Increment both p1 and p2.
- If any of the arrays is exhausted, Then append the rest of the array to the result directly.

Test cases:
- Simple 
- Single/ 2 elements or none
- Duplicates

"""


def merge_two_sorted_arrays(arr1, arr2):
    p1, p2 = 0, 0
    res = []

    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] < arr2[p2]:
            res.append(arr1[p1])
            p1 += 1
        elif arr1[p1] > arr2[p2]:
            res.append(arr2[p2])
            p2 += 1
        else:
            res.append(arr1[p1])
            res.append(arr2[p2])
            p1 += 1
            p2 += 1
    
    while p1 < len(arr1):
        res.append(arr1[p1])
        p1 += 1

    while p2 < len(arr2):
        res.append(arr2[p2])   
        p2 += 1     

    return res


"""
In-Place Duplicate Removal

Remove duplicates from the array while preserving the order

arr = [1, 2, 2, 3, 3, 3, 5]

- As mentioned we can use the Fast Slow pointers pattern
- Initialize two pointers i, j adjacent to each other
    - If arr[i] < arr[j], increment both i and j and swap if j != i + 1
    - If arr[i] == arr[j], increment j until arr[i] == arr[j] condition fails

"""


def remove_duplicates_sorted(nums):
    if not nums:
        return 0

    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write += 1
    return write


"""

      |
  |   |       |
  | | | |   | |
  | | | | | | | |
  | | | | | | | | |
-------------------------
    i         j
  0 1 2 3 4 5 6 7 8

- If h[i] > h[j] -> decrement j
- else, increment i
- elif If equal?

"""

def max_container_area(heights):
    l, r = 0, len(heights) - 1
    
    max_area = 0

    while l < r:
        curr_area = (r - l) * min(heights[l], heights[r])
        max_area = max(max_area, curr_area)

        if heights[l] > heights[r]:            
            r -= 1
        elif heights[l] < heights[r]:
            l += 1
        else:
            r -= 1
        
    return max_area
        


