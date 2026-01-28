from collections import defaultdict, deque

"""
Given, an array of sales, find the most sales in any 7 day period

sales = [0, 3, 7, 12, 10, 5, 0, 1, 0, 15, 12, 11, 1]
         0  1  2   3   4  5  6  7  8   9  10  11 12
                                   i

curr_sum = 37
max_sum = 37

curr_sum += 1 - 0
curr_sum = 38
max_sum = 38



Output: 44

- Create a window of size 7. Calculate the sum of the entire window
- Iterate through the array one by one. 

This is expensive.

Instead,
- While iterating through the window of size 7, try to update the window by adding the last element of the window with next element and subtracting the first index of the window.
- Now check the sum of window and update max accordignly

"""

def most_sales_7_days(sales):    
    l, r = 0, 0

    curr_sum = 0
    max_sum = 0

    while r < len(sales):
        curr_sum += sales[r]
        r += 1
        if r - l == 7:
            max_sum = max(max_sum, curr_sum)
            curr_sum -= sales[l]
            l += 1
    return max_sum



"""
Given a string s, and an integer k, return the length of the longest substring of s that contains atmost K distinct characters.

s = "eceba", k = 2

- So, we will be using a dictionary to store if the window satisfies the distinct k
- iterate through the string and create a window and check
- If the condition (window satisfies the distinct K) fails then increment the left pointer until the condition satisfies

- I have a dictionary built up. Now i need to decrease the size of the window if the number of distinct elements is > K

- {e: 2, c: 1, b: 1}

- So, i have to check if any of the values is 0 and do a count every time?


"""

def longest_substring_k_distinct(s):
    d = defaultdict(int)

    l = 0
    max_len = 0

    for r in range(len(s)):
        d[s[r]] += 1        

        while len(d) > 2:            
            d[s[l]] -= 1
            if d[s[l]] == 0:
                del d[s[l]]
            l += 1

        max_len = max(max_len, r - l + 1)

    return max_len






    




        

    
