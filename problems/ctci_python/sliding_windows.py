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

def most_sales_k_days(sales, k):    
    l, r = 0, 0

    curr_sum = 0
    max_sum = float("-inf")

    while r < len(sales):
        curr_sum += sales[r]
        r += 1
        if r - l == k:
            max_sum = max(max_sum, curr_sum)
            curr_sum -= sales[l]
            l += 1
    return max_sum if max_sum != float("-inf") else 0



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


"""
📋 SLIDING WINDOW PROBLEM - Interview Starting Now
Real-World Context:
You're working on a data quality system at Meta that processes user-generated text. 
We need to identify the longest sequence of characters in a string where we can replace up to K characters to make all characters the same. 
This helps us detect spam patterns where bots make small variations to bypass filters.

Problem Statement:
You are given a string s and an integer k. You can choose up to k characters in the string and replace them with any other character.
Return the length of the longest substring containing the same letter you can get after performing the above operations.

s = "ABAB", k = 2

ABAB -> We can either update to all A's or all B's

AAAA -> the longest substring is 4 

- Probably create a counter? {A: 2, B: 2}
- Greedily pick the highest/ max freq key or character - TC: O(n), SC: O(n)
- ABAB now, If we can use sliding window to calculate the longest substring. Initialize window using 2 pointers. 
    - In the Sliding window, skip if the char is the same as the max freq char
    - decrement the k value if the adjacent char is not equal to the max freq char
    - Do this decrement until the k value is obeyed. and get the length of the curr window
    - If the window condition fails when k == 0, then try to increment the left pointer
- return if this reaches end

- AAAB and k = 1
- AAAA and k = 0
return 


s = "AABABBA", k = 1

- AABABBA, k = 1
- AAAABBA, k = 0
- We see a distinct element and k = 0, then update the l pointer as well as k
- A ABABBA, k = 1
- A AAABBA, k = 0
- Return


Input: s = "AABABBA", k = 1

AABABBA -> Try to update the first occurence? But how do we choose the first occurence?




Examples:
Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.

"""



    




        

    
