"""
The Task:
Given an array where each element represents the biomarker level on a given day, 
find the maximum difference between a later day's level and an earlier day's level. If no improvement is possible, return 0.

Example 1:
Input: levels = [7, 1, 5, 3, 6, 4]

num = 3
min = 1
res_max_diff = 4


condition: max(levels[r]) - min(levels[l]) for different values where r > l. This should return the maximum difference.

- So, the question is if i am the max today. what is the minimum until now. 

- I will initialize the minimum variable
- Update the minimum variable while going through the list by comparing the value
- So always compare curr_num vs last seen minimum and update the max_difference as necessary

"""

def best_time_to_buy_stock(nums):
    min = float("inf")
    res_max_diff = 0

    for num in nums:
        if num < min:
            min = num
        
        if num > min:
            res_max_diff = max(res_max_diff, num - min)
    
    return res_max_diff




"""
Given an array where each element represents the height of a barrier at that position, 
find two barriers that together with the track can hold the maximum amount of liquid.

- return the heights at positions such that we can hold maximum amount. 
- So, in order to hold Maximum amount, we need to have the area which is maximum. 
    - Area = width * height
    - Width - difference b/w the positions. Ideally, needs to be large to get maximum
    - Height - min(between the heights). Ideally, needs to be large to get maximum

- (r - l) > maximum
- min(heights[l], heights[r]) should be maximum

How to set up, l and r - l can be 0 and r can be len(nums) - 1 respectively

condition? Keep the max height 
- How to increment l 
    What happens if we increment l?
    - heights = [4, 3, 2, 1, 8]
                 l           r
    - 
- How to increment r

- INitialize l and r
- We know how to incremenet l and r
- calulcte the max

"""


def container_most_water(heights):
    l, r = 0, len(heights) - 1
    max_area = 0

    while l < r:        
        curr_area = (r - l) * min(heights[l], heights[r])
        max_area = max(max_area, curr_area)

        if heights[l] > heights[r]:
            r -= 1
        else:
            l += 1

    return max_area



"""
Given an array of strings (DNA sequences), group all sequences that are anagrams of each other together. Return the groups in any order.


- Return the groups of anagrams -> ["eat", "tea", "tan", "ate", "nat", "bat"] -> [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

Input: SDEN -> Duplicates? Empty strings?
Ouptut: SDEN -> Does the Order matter? Empty strings?

- Initializing a defaultdict(list)
- Calculating the counts of each word instead of sorting
- Convert the counts to a tuple and use this tuple as a key
- return the list of lists by reading from the dict


Examples:

Input: sequences = ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
"""



"""
Given a 2D grid of '1's (living cells) and '0's (dead cells), count the number of cell colonies. 
A colony consists of living cells that are connected horizontally or vertically.
Examples:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

- return the count of islands.

- So if we are at island r, c = 0, 0 we see a 1. We try to make sure all the 1's directly accessible need to be marked as visited. 

- DFS
- Iterate through the grid, r and c. If r and c is 1. 
    - Then update the count of islands and then do a DFS to find all the closer neighbors. 
        - If neighbor = grid[r][c] == 1, then mark the neighbor as visited using grid[r][c] == 0
        - We need to go 4 different directions

"""


def numIslands(grid):
    num_islands = 0
    directions = [[0,1], [1,0], [-1,0], [0,-1]]

    def dfs(grid, i , j):
        if (i < 0 or j < 0 or i >= len(grid) or j >= len(grid)):
            return
        if grid[i][j] == "0":
            return
        
        grid[i][j] = 0

        for r, c in directions:
            dfs(grid, i + r, j + c)

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == "1":
                num_islands += 1
                dfs(grid, r, c)

    return num_islands


"""
The Task:
Given an array of sample IDs (integers), return True if any ID appears at least twice, and return False if every ID is unique.

Examples:

Input: samples = [1, 2, 3, 1]
Output: True

- Check if we have a duplicate in the list
- We can use a set to store the unique elements
- Then iterate through the main array, if the value is already available return True. Rerturn False at the end

"""

def containsDuplicate(samples):
    s = set()
    for sample in samples:
        if sample in s:
            return True
        else:
            s.add(sample)
    return False
    
"""
Given a string s, determine if it is a palindrome. 
Only consider alphanumeric characters and ignore cases. Non-alphanumeric characters (spaces, punctuation) should be ignored.

Examples:

Input: s = "A man, a plan, a canal: Panama"
Output: True

- return True or False based on if the string is palindrome
- If yes, return True. We need to skip any Non alphanumeric characters

- Use two pointers to check if it is palindrome
- Have two pointers at both ends

l = 0, r = len(s) - 1

How to increment l and r?
- Ideally, If we encounter a non alphanumeric character, we need to continue
- Compare both l and r at each iteration. If it is false return false. else l += 1, r -= 1

"""

def validPalindrome(s):    
    l, r = 0, len(s) - 1

    while l < r:
        if not s[l].isalnum():
            l += 1
            continue

        if not s[r].isalnum():
            r -= 1
            continue
            
        if s[l].islower() != s[r].islower():
            return False
        
        l += 1
        r -= 1

    return True



"""
Given an array of molecular weights (integers) and a target weight, 
return the indices of the two compounds that add up to the target. 
You may assume that each input has exactly one solution, and you cannot use the same compound twice.

- return the indexes of two values where addition is equal to target
    nums[i] + nums[j] = target => nums[j] = target - nums[i]

- We can use a hash table in such as way that, we can always check if target - nums[i] is already present in the hash table. If already present, we can return the indices

Examples:
Input: weights = [2, 7, 11, 15], target = 9
Output: [0, 1]

"""


def twoSum(nums, target):
    d = {}

    for i, val in enumerate(nums):
        complement = target - val
        if complement in d:
            return [d[complement], i]
        d[val] = i
    return [-1, -1]


"""
Given a sorted array of integers and a target value, return the index of the target if it exists. If it doesn't exist, return -1.
You must write an algorithm with O(log n) runtime complexity.

Examples:

Input: concentrations = [-1, 0, 3, 5, 9, 12], target = 9

- return the index of the target if it exists

- we can use binary search

- Calculate the mid which is l + r // 2
- If arr[mid] > target then the value is in the left array
- If arr[mid] < target then the value is in the right array
- if arr[mid] == target return

"""


def binary_search(nums, target):
    l, r = 0, len(nums) - 1

    while l < r:
        mid = (l + r) // 2

        if nums[mid] == target:
            return mid
        
        elif nums[mid] > target:
            r = mid - 1
        
        else:
            l = mid + 1

    return -1

            
"""
Given a sorted array that has been rotated at some unknown pivot point, and a target value, return the index of the target if it exists, otherwise return -1.

You must write an algorithm with O(log n) runtime complexity.

- return index of a target if it exists

- In order to get O(log n) we need to use something like binary search which halves the input on each iteration using a condition
    - If left half is sorted (arr[l] <= arr[mid])
        -> check if target is in the range [arr[l], arr[mid]]

    - Else left half is sorted (arr[l] <= arr[mid])
        -> check if target is in the range [arr[l], arr[mid]]
    
- In this case, initialize l, r = 0, len(arr) - 1
    - How to increment the l and r to find the target because it is rotated

Examples:
Input: measurements = [4, 5, 6, 7, 0, 1, 2], target = 0
                       l        m        r

Output: 4

"""


"""
Given a sorted array that has been rotated at some unknown pivot point, find the minimum element.
You must write an algorithm with O(log n) runtime complexity.

-> compare mid to l and mid to r
-> If mid > r: This means the minimum element should be in the right side of the array
    l = mid + 1
-> else: 
    r = mid - 1
-> return

Examples:

Input: measurements = [3, 4, 5, 1, 2]
Output: 1

"""



"""
Given a string s consisting of only uppercase English letters and an integer k, 
you can replace at most k characters with any other character. 

Return the length of the longest substring containing the same letter you can get after performing the replacements.

- Return the longest sequence conatining the same letter after replacing k elements

- So over here i can replace B or A does not matter.

- return max(r - l + 1) where all the elements are same

- Invalid condition: If k = 0. Then, increment l

- Use a freq_map to keep track of the characters
- Can i use a stack?

Examples:
Input: s = "AABABBA", k = 1
                r
            l

Output: 4

"""
from collections import defaultdict

def longest_substr_same_letter(s, k):
    stack = []

    l = 0
    max_len = 0

    for r in range(len(s)):
        if stack and stack[-1] != s[r] and k != 0:
            k -= 1
        
        while stack and stack[-1] != s[r] and k == 0:
            stack.pop()


        stack.append(s[r])

        






