"""
Bucket Sort

Create buckets for each freq

All the values that match the freq for example 1, we add to a bucket

- return the top k buckets

- freq = [[] for cnt in cnts]
- 

"""

def topKFrequent(violations, k):
    # Count Frequencies
    count = {}
    for violation in violations:
        count[violation] = count.get(violation, 0) + 1

    # Create buckets
    buckets = [[] for _ in range(len(violations) + 1)]

    for violation, freq in count.items():
        buckets[freq].append(violation)

    # Collect top K from highest freq buckets
    res = []
    for freq in range(len(buckets), 0, -1): # Starting from the end
        for violation in buckets[freq]:
            res.append(violation)
            if len(res) == k:
                return res
            
    return res



"""
3 SUM

- shift_hours[i] + shift_hours[j] + shift_hours[k] == 0

- There are duplicate numbers but we should not return duplicate results

nums = [-1,0,1,2,-1,-4]

- Iterate through the array one by one
- for each element check the remaining array. It should match num[j] + nums[k] = -1 * nums[i]. Sort the array and send
- And also need to make sure, we have the visited

[-1, 1, 2, 3, 4]
 l            r

target = 4

nums[l] + nums[r] > target: then decrement r
nums[l] + nums[r] < target: then increment l
nums[l] + nums[r] == target: 

"""


def threeSum(nums):
    nums.sort()

    res = []

    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        l, r = i+1, len(nums) - 1
        target = -1 * nums[i]

        while l < r:
            if nums[l] + nums[r] == target:
                res.append([nums[i], nums[l], nums[r]])
            
                # skip duplicates
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
            
                l += 1
                r -= 1
            
            elif nums[l] + nums[r] > target:
                r -= 1
            
            else:
                l += 1

    return res


"""
prices = [7,1,5,3,6,4]
            l         
                    r 

- Calculate max profit - Buy at Min and Sell at Max

- This minimum must be on the left and the max should be on the right to get the max profit

- So, if prices[l] > prices[r] - This means, the left pointer cannot yeild max profit. So increment l
- If prices[l] < prices[r] - This means we have to calculate the profit. This time decrement r
- Basically we need the most min element on the left and the most max element on the right

- So better to keep tab of the the min value and max value
          
- return the max profit



- Single pass - Just track the minimum value seen so far

"""

def maxProfit(prices):
    min_price = float("inf")
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)

        curr_profit = price - min_price

        max_profit = max(max_profit, curr_profit)
    
    return max_profit

"""
LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS 

s = "abcabcbb"
     l
       r

set = {a: 1, b: 1, c: 1}     

s = "bbbbb"
     l
     r     

- Use a set to store the visited or existing variable in the string
- Calculate the len(substr_no_repeating)
- So increment the right pointer as you go forward.
- Check if the curr right pointer is in the set already. 
    - If yes, 
        - Increment the left pointer and decrement the value by -1
        - Make sure, you are just keepinhgza;kA:l'spcklj


"""
from collections import defaultdict

def longest_substring_without_repeating_chars(s):
    l = 0
    d = defaultdict(int)
    res_len = 0

    for r in range(len(s)):
        while s[r] in d:
            if s[l] != s[r]:
                l += 1            
            else:
                d[s[r]] -= 1

        d[s[r]] += 1
        res_len = max(res_len, r - l + 1)    
    return res_len



"""
Invert Binary Tree

        4
    2       7
1      3 6     9

- What should we do?

- DFS - left, root, right
- reverse the left and right values at the base.

temp = self.left.val
self.left.val = self.right.val

Base Case:
- 

    dfs(left)
    dfs(right)

"""


def invertTree(root):
    if root is None:
        return None
    
    root.left, root.right = root.right, root.left

    invertTree(root.left)
    invertTree(root.right)

    return root



"""
- Return level order traversal

     3
   /   \
  9    20
      /  \
    15    7

BFS
- Use a queue to store the elements. Pop from the front as we traverse

"""
from collections import deque

def level_order_traversal(root):
    queue = deque()
    res = []

    queue.append(root)

    while queue:
        level_size = len(queue)
        temp = []

        for i in range(level_size):
            curr = queue.popleft()
            temp.append(curr.val)

            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

        res.append(temp)
    
    return res

"""
Number of Islands

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

- Traverse through the matrix using r and c
- Directions: [(1,0), (-1,0), (0,1), (0,-1)]

- Traverse through the grid. If r and c == 1 then 
    - increment number of islands result + 1
    - do a dfs for all the nodes around it until all are 0's
- Mark visited as 0 to stop duplicate traversals

- Initilialization
- For each node, 

"""


def numIslands(grid):
    num_islands = 0
    rows, cols = len(grid), len(grid[0])

    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols:
            return 
        
        if grid[r][c] != "1":
            return
        
        grid[r][c] = "0"

        for k, v in directions:
            dfs(k+r, v+c)

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "1":
                num_islands += 1
                dfs(r, c)

    return num_islands

"""
Merge Intervals

- Sorting and Intervals

intervals = [[1,3],[2,6],[8,10],[15,18]]

- So, we try to compare the adjacent elements
- I will use a stack and add all the elements to a stack

"""

def mergeIntervals(intervals):
    stack = []    
    intervals.sort()

    for start, end in intervals:
        if not stack or start > stack[-1][1]:
            stack.append([start, end])
        
        else:            
            stack[-1][1] = max(stack[-1][1], end)

    return stack



"""
Arya Health Context:
Arya integrates with EMR (Electronic Medical Records) systems via APIs. EMRs have strict rate limits:

Epic EMR: 100 requests per 60 seconds
Cerner EMR: 50 requests per 30 seconds
If exceeded → 5-minute block (serious production issue!)

Arya's integration layer needs a RateLimiter that enforces these limits to prevent blocking and maintain system reliability.

Problem Statement:
Implement a RateLimiter class that:

- Tracks requests in a sliding time window
- Returns True if request is allowed (within limit)
- Returns False if request would exceed limit
- Must be O(1) amortized time complexity
- Must handle 100,000+ requests efficiently


100 requests per 60 seconds window

3 requests per 10 seconds window

limiter.allow_request(ts)

limiter.allow_request(1) + 1
limiter.allow_request(1) + 1
limiter.allow_request(2) + 1

limiter.allow_request(11) + 1



We need to count the number of requests in the 10 sec window
- Calculate, window_start = ts - 10 sec. Use this window_start to calculate the number of requests in the last 10 sec


- Initialize a deque to add at the end of deque and remove from the beginning
- We also need to be sure about the counts in the condition
- So, as soon as we move the left pointer we need to decrement the size of the rate limting and then return true or false

"""

class RateLimiter:
    def __init__(self, max_requests, window_seconds):
        self.q = deque()
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.count = 0

    def allow_request(self, ts):        
        window_start = ts - self.window_seconds # 11 - 10 = 1

        while self.q and self.q[0] <= window_start:
            self.q.popleft()

        if len(self.q) < self.max_requests:
            self.q.append(ts)
            return True
        
        return False
                    

