"""
Problem Statement:
Given a list of gene sequence identifiers (represented as strings) from a sequencing run, return the k most frequently occurring sequences.
Example:
sequences = ["BRCA1", "TP53", "BRCA1", "EGFR", "TP53", "BRCA1", "KRAS", "TP53", "TP53"]
k = 2

Output: ["TP53", "BRCA1"]  (or ["BRCA1", "TP53"] - order doesn't matter)

Explanation: TP53 appears 4 times, BRCA1 appears 3 times
Constraints:

1 ≤ sequences.length ≤ 10^5 (typical batch size in genomic processing)
1 ≤ k ≤ number of unique sequences
Sequence IDs are strings (length 1-20 characters)

- Given a list
- Return the k top most frequent elements 
- {BRCA1: 3, TP53: 4}

- Ask questions? BUt how to ask these questions. You need to be very well experienced to ask these questions. How to get experienced? 
    - Is the list already sorted? 
    - Duplicates allowed?
    - Input size

- Iterate through the entire sequence and have a counter to save the counts of repeated elements 
- Sort the elements in the counter by the count. This operation is O(n log n)

- Initialize a heap
- Store all the elements onto a min heap. So what exactly are we storing? We are storing the ('val', count)
- If the number of elements in a heap > k. Then, we can just pop the values.

sequences = ["BRCA1", "TP53", "BRCA1", "EGFR", "TP53", "BRCA1", "KRAS", "TP53", "TP53"]
k = 2

TP53 appears 4 times, BRCA1 appears 3 times

heap = [(2, BRCA1), (1, TP53)]
d = {BRCA1: 2, TP53: 1}

- Count the sequences
- Use heap to go through the counts

"""
import heapq
from collections import Counter, defaultdict

def top_k_elements(sequences, k):
    heap = []
    c = Counter(sequences)  # ← O(n)

    for key, count in c.items():  # ← O(n) worst case
        heapq.heappush(heap, (count, key))  # ← O (log k)
        if len(heap) > k:
            heapq.heappop(heap)  # ← O(log k)
    
    return [v for _, v in heap]  # ← O(k)



"""
Problem 1: Maximum Number of Events That Can Be Attended
Context: At Genentech, you're managing clinical trial scheduling. Each trial has a start date and end date. You can only attend one trial per day, and once you attend a trial, you don't need to come back to it. What's the maximum number of trials you can attend?
Problem Statement:
Given an array of events where events[i] = [startDay_i, endDay_i], 
you can attend an event at any day d where startDay_i <= d <= endDay_i. 

You can only attend one event per day. Return the maximum number of events you can attend.

Max number of events that can be attended

Given, the start_day and end_day. You can attend an events on either the start day or the end day

If we have 3 instances of [1, 2] i.e [[1, 2], [1, 2], [1, 2]]
The max num of events that can be attended is only 2. 


Examples:
pythonExample 1:
events = [[1,2],[2,3],[3,4]]
Output: 3
[1, 2] - Yes on day 1
[2, 3] - Yes on day 2
[3, 4] - Yes on day 3


Example 2:
events = [[1,2],[2,3],[3,4],[1,2]]
Output: 4

[1, 2] - Day 1
[1, 2] - Day 2
[2, 3] - Day 3
[3, 4] - Day 4

Example 3:
events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
Output: 4

heap = []
event_index = 0
count = 0

sorted_events = [[1,1],[1,4],[2,2],[3,4],[4,4]]
- Add events on day 1
    [1,1] -> push end_day to heap
    [1,4] -> push end_day to heap
    - heap = [1,4]
    - pop minimum - attend event on day 1
    - count = 1

- Add events starting on day 2 to heap. We are only adding the end_day to find the minimum
    - [2,2] -> push end_day to heap
    - heap = [4, 2] -> [2, 4]
    - pop min -> 2
    - heap = [4]
    - count = 2

    
- Add events starting on day 3 to heap. We are only adding the end_day to find the minimum
    - [3,4] -> push to end of heap
    - heap = [3, 4]
    - pop min -> 3
    - heap = [4]
    - count = 3

- Add events on day 4 to heap. We are adding only the end_day to find the minimum
    - [4,4] -> push the end day to heap
    - heap = [4,4]
    - count = 4
    - pop - 4


- Sort the input array with the first element and then the second element
- Store the element in a dictionary for faster lookup?
"""



"""
Problem Statement:
Given a string s, find the length of the longest substring without repeating characters.

Examples:
pythonExample 1:
s = "abcabcbb"
Output: 3
Explanation: "abc" is the longest substring without repeating characters

Example 2:
s = "bbbbb"
Output: 1
Explanation: "b" is the longest (entire string is same character)

Example 3:
s = "pwwkew"
Output: 3
Explanation: "wke" is the longest substring
Note: "pwke" is NOT valid because 'w' repeats

Example 4:
s = "abcdefgh"
Output: 8
Explanation: Entire string has no repeats

Example 5:
s = ""
Output: 0
Explanation: Empty string

Example 6:
s = "dvdf"
Output: 3
Explanation: "vdf" is the longest
Constraints:

0 ≤ s.length ≤ 5 × 10^4
s consists of English letters, digits, symbols, and spaces


- return the max length of a window which do not have any repeating characters or basically ditsinct

- Lets try to approach this using sliding window
- Two pointers there is left pointer and right pointer which indicate the window size 

s = "abcbca"
        l r

unique_set = {a, b, c} -> {c,b} -> {b, c} -> {b, c, a}
max_count = 3

while loop to check the invalid window condition

"""

def longest_unique_substring(s):
    l = 0
    max_len = 0
    unique_set = set()

    for r in range(len(s)):        

        while s[r] in unique_set:
            unique_set.remove(s[l])
            l += 1

        unique_set.add(s[r])
        max_len = max(max_len, r - l + 1)

    return max_len
        
"""
Problem Statement:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An anagram is a word formed by rearranging the letters of another word, using all original letters exactly once.


Examples:
pythonExample 1:
strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

- Sort each value and this value to a dictionary as key.
- Append the original word in a value list
- Return the values from the dictionary


- Instead of sorting which is k log k, we can use a dict of tuples as key
- Initialize a list which is of size 26. Calculate the index for each char using ord(ch) - ord('a')
- Use this to store the number of times each word is repeated
- Convert this list to tuple and add the values to a list


"""

def group_anagrams(words):
    d = defaultdict(list)

    for word in words:
        chars_count = [0]*26
        for ch in word:
            chars_count[ord(ch) - ord('a')] += 1
        
        key = tuple(chars_count)

        d[key].append(word)

    return [v for _, v in d.items()]
    

"""
Problem Statement:

Given two strings s and p, return an array of all the start indices of p's anagrams in s. 
You may return the answer in any order.
An anagram is a word formed by rearranging the letters of another word using all original letters exactly once.

Examples:

s = "cbaebabacd"
p = "abc"
Output: [0, 6]

Explanation:
- Index 0: "cba" is an anagram of "abc"
- Index 6: "bac" is an anagram of "abc"


- Return all the start indices of p's anagrams in s
- abc, bca, cba are all anagrams of abc

- So, in short we have a word. We create a counter or similar data structure for the p anagram
- We check if that counter matches any of the substrings inside s

- If the dict_substr == dict_p, then we return the index of the substring. So basically the left pointer
- We can also make sure the length of the window is equal to the length of p

Example:
s = "cbaebabacd"
       l r
p = "abc" - len = 3

Using counter dict vs counter tuple?

"""

def find_anagrams(s, p):
    p_len = len(p)

    p_counter = [0]*26
    for ch in p:
        p_counter[ord(ch) - ord('a')] += 1

    l = 0
    res = []    
    s_counter = [0]*26

    for r in range(len(s)):
        s_counter[ord(s[r]) - ord('a')] += 1

        while (r - l + 1) > p_len:
            # update the counter
            s_counter[ord(s[l]) - ord('a')] -= 1
            l += 1
        
        if s_counter == p_counter:
            res.append(l)

    return res


"""
During the Interview:
* Start by restating the problem to confirm understanding.
* Ask clarifying questions (e.g., input size? duplicates allowed? sorted?).
* Verbalize every step—interviewers at Genentech/Roche often score communication highly.
* Write clean, readable code (good variable names, comments if time).
* Test with small examples + edge cases (empty input, single element, max constraints).
* End strong: Summarize complexity and one optimization idea.

restate the problem → clarify requirements → discuss approach → code → test verbally → analyze Big O → optimize.
"""


"""
Problem Statement:
Given an integer array nums and an integer k, 
return the kth largest element in the array.

Note that it is the kth largest element in sorted order, not the kth distinct element.

- Sort the array in desc order and then return the kth element - O(n log n)

- Creating a heap and pushing the elements on to the heap
- If len(heap) > k then we just pop the element 
- Since this is the min heap, we always pop the minimum element.
- Therefore, Once we complete the entire iteration we just return the first element from the heap

"""

def kth_largest(nums, k):
    heap = []

    for num in nums:
        heapq.heappush(heap, num)

        if len(heap) > k:
            heapq.heappop(heap)
    
    return heap[0]







