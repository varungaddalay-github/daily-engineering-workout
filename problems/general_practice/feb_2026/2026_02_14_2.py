"""
Recursion

"""

def infinite_recursion(n):
    print(n)
    return infinite_recursion(n)

def proper_recursion(n):
    print(n)

    if n == 0:
        return
    proper_recursion(n-1) # make n smaller


"""
factorial 
5 * 4 * 3 * 2 * 1

"""    

def fact_recursion(n):
    if n == 1:
        return 1
    return n * fact_recursion(n-1) 


"""
Fibonacci
1 1 2 3 5 8 ...
add the last 2 elements
"""

def fib_recursive(n):
    if n == 0 or n == 1:
        return 1
    return fib_recursive(n-1) + fib_recursive(n-2)


"""
Back tracking


def backtrack(choices):
    if no_more_choices:
        return
    
    for each_choice in choices:
        make choice
        backtrack()
        undo choice

"""



"""
Generate all subsets

i/p: [1, 2, 3]

o/p: [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]

- Given list - 

Base Case: empty list
Recursive case: 

"""


def generate_subsets(nums):
    if len(nums) == 0:
        return [[]]
    
    # recursive case: Get all subsets of the rest of the list
    first = nums[0]
    rest = nums[1:]

    subsets_without_first = generate_subsets(rest)
    
    for num in nums:
        generate_subsets



"""
Trace the output for the 4 given inputs. Show all intermediate steps
Explain what the function is doing.
Identify the base case and recursive case.
Summarize the final output for each input.

# Inputs: [1,2,3,4,5,6,7,8], [9,8,7,6], ["a","b","c","d","e","f"], list(range(10)) 

def mystery(lst):
    if not lst:
        return []
    return mystery(lst[2:]) + [lst[1]] if len(lst) > 1 else []

At each step:
- Skip 2 elements (`lst[2:]`)
- Take the element at index 1 (`lst[1]`)    

[1,2,3,4,5,6,7,8]

return mystery([3,4,5,6,7,8]) + [2]

mystery([5,6,7,8]) + [4]

mystery([7,8]) + [6]

mystery([]) + [8]

[]



[1, 2, 3, 4, 5, 6, 7, 8]  → Take 2, skip to position 2
   [3, 4, 5, 6, 7, 8]     → Take 4, skip to position 2
      [5, 6, 7, 8]        → Take 6, skip to position 2
         [7, 8]           → Take 8, skip to position 2
            []            → Done


[1, 2, 3, 4, 5] → Take 2, skip to position 2
  [3, 4, 5]     → Take 4, skip to position 2
     [5]        -> DOne         

"""





"""
def f(n):
    if n <= 1:
        return 1
    return f(n // 5) + f(7 * n // 10) + n

What is the recurrence relation for the runtime of this function?


"""