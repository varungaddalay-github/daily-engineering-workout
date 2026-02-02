"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. 
Each hour, she chooses some pile of bananas and eats k bananas from that pile. 
If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4


piles = [3,6,7,11], h = 8, 

n = 4 piles 3, 6, 7, 11

Each hour, i.e. h = 1 -> k = ?. If the pile has less than k bananas. 
So basically she can only eat from 1 pile in 1 hour

3, 6, 7, 11 and total hours = 8

We are trying to determine the minimum K such that she can eat all the bananas within given hours

total hours = 8 and n = 4
k = ? such that n * c*(piles[i]) = h -> I am missing something

c*(piles[i]) = k

Simple example:
piles = [1, 1, 1, 1], h = 4
k = 1


for a given k, 
total_hours_needed = sum(piles[i]/k)

we want total_hours_needed <= given h

So need to find a K, where the above condition holds true

Why Binary Search?
- If koko can finish in h hours at speed k, then she can definitely finish at any speed > K

Monotonic relationship:
- Speed increases -> Hours needed decreases
- Speed decreases -> Hours needed increases

The search space:
- minimum possible k is 1 
- maximum possible k is max(piles)

The approach:

- Binary search on possible speeds (from 1 to max(piles))
- for each candidate k, Calculate "How many hours would it take?"
    - If hours_needed <= h, then we can go even slower (search left)
    - If hours_needed > h, then we can go faster (search right)


piles = [3,6,7,11], h = 8, 

k = 1 to 11

Calculate total_hours_needed = sum(piles[i]/k) at each step and then compare

mid of k is (1 + 11)/2 = 6

if k = 6, then total_hours_needed = sum (3/6 + 6/6 + 7/6 + 11/6) -> (0.5 + 1 + 1 + 2) <= 8
therefore, we search to the left which is 1 to 6

calculate the mid which is k = 3
then 
total_hours_needed = sum (3/3 + 6/3 + 7/3 + 11/3) -> (1 + 2 + 2 + 4) > 8
therefore, we search to the right which is 4 to 6

"""


"""

You have N stalls at positions: [1, 2, 4, 8, 9]
You need to place C = 3 cows in these stalls.
The cows are aggressive and fight if they're too close.

Goal: Maximize the MINIMUM distance between any two cows.

Example:
If you place cows at positions [1, 4, 8]:
  - Distance between cow1 and cow2: 4 - 1 = 3
  - Distance between cow2 and cow3: 8 - 4 = 4
  - Minimum distance = 3

If you place cows at positions [1, 2, 9]:
  - Distance between cow1 and cow2: 2 - 1 = 1
  - Distance between cow2 and cow3: 9 - 2 = 7
  - Minimum distance = 1

First placement is better (min distance = 3 vs 1)

"""




"""
Given: sorted array [1, 3, 5, 7, 9, 11], target = 12
Find: two numbers that sum to target

Example solutions:
- indices (1, 4) → values 3 + 9 = 12 ✓
- indices (2, 3) → values 5 + 7 = 12 ✓


Two sum in a sorted array using binary search?

nums = [1, 3, 5, 7, 9, 11], target = 12

- Calculate mid
- Check in the range of left or right

The range of search is different for every index?

target - nums[0] = 12 - 1 = 11

So, for each element we are searching in the right side of the array

-> Calculate the mid which is at index 3
-> We have to search on the right side of the array which is from 7 to 11
-> Again we calculate the mid in the right side of the array and return 9 

"""