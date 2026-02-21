from typing import List, Dict, Tuple
from collections import defaultdict, deque

# ============================================================
# 1️⃣ Evaluate Division (Graph + Queries)
# ============================================================
"""
LeetCode-style: 399. Evaluate Division (Medium)

You are given:
    equations: List of equations, where equations[i] = [A_i, B_i]
    values:    List of real numbers, where values[i] = A_i / B_i
    queries:   List of queries, where queries[j] = [C_j, D_j]

Each variable is a string representing some entity.

You must compute the result of each query:
    C_j / D_j

If the result cannot be determined from the given equations,
return -1.0 for that query.

Example:
    equations = [["a","b"],["b","c"]]
    values    = [2.0, 3.0]
    queries   = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]

    Output: [6.0, 0.5, -1.0, 1.0, -1.0]

Notes:
- Division is transitive: a/b * b/c = a/c.
- Use a graph where edge(A->B) = value and edge(B->A) = 1/value.
- Use DFS/BFS to answer queries.
"""

def calcEquation(equations: List[List[str]],
                 values: List[float],
                 queries: List[List[str]]) -> List[float]:
    graph = defaultdict(list)
    for (a, b), v in zip(equations, values):
        graph[a].append((b, v))
        graph[b].append((a, 1.0 / v))

    def bfs(src, dst):
        if src not in graph or dst not in graph:
            return -1.0
        if src == dst:
            return 1.0
        
        q = deque([(src, 1.0)])
        visited = {src}

        while q:
            node, val = q.popleft()
            if node == dst:
                return val
            for neighbor, w in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append((neighbor, val * w))
        return -1.0
    
    return [bfs(a, b) for a, b in queries]


# ============================================================
# 2️⃣ Minimum Penalty for a Shop (Prefix/Suffix Scans)
# ============================================================
"""
LeetCode-style: 2483. Minimum Penalty for a Shop (Medium)

A shop is open from hour 0 to hour n-1. You are given:
    customers: a string of length n consisting of 'Y' and 'N'

For each hour i:
- If the shop is OPEN at hour i and customers[i] == 'N', that's 1 penalty.
- If the shop is CLOSED at hour i and customers[i] == 'Y', that's 1 penalty.

You may choose a closing time 'k' where:
- Shop is OPEN for hours [0, k-1]
- Shop is CLOSED for hours [k, n]

Goal:
Find the closing time k (0 <= k <= n) that MINIMIZES penalty.
Return the smallest such k if there are multiple.

Example:
    customers = "YYNY"
    Optimal close time is 2.
"""

def best_closing_time(customers: str) -> int:
    pass



# ============================================================
# 3️⃣ Simple Bank System (Array + Operations)
# ============================================================
"""
LeetCode-style: 2043. Simple Bank System (Medium)

You are designing a simple banking system.

Given:
    n accounts, numbered 1..n
    balances: List[int] of length n, where balances[i] is balance of account (i+1)

Supported operations:
- "deposit(account, money)"
- "withdraw(account, money)"
- "transfer(account1, account2, money)"

All operations must:
- Check account existence (1..n)
- Ensure sufficient balance on withdraw/transfer
- Return success/failure (True/False) or manage state accordingly

For this coding version:
Implement a class Bank:

    class Bank:
        def __init__(self, balance: List[int]): ...
        def transfer(self, account1: int, account2: int, money: int) -> bool: ...
        def deposit(self, account: int, money: int) -> bool: ...
        def withdraw(self, account: int, money: int) -> bool: ...

No extra methods needed.
"""

class Bank:
    def __init__(self, balance: List[int]):
        pass

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        pass

    def deposit(self, account: int, money: int) -> bool:
        pass

    def withdraw(self, account: int, money: int) -> bool:
        pass



# ============================================================
# 4️⃣ Calculate Amount Paid in Taxes (Brackets)
# ============================================================
"""
LeetCode-style: 2303. Calculate Amount Paid in Taxes (Easy)

You are given:
    brackets: a 2D list where brackets[i] = [upper_i, percent_i]
    income:   an integer representing income

The i-th tax bracket has:
- Upper bound 'upper_i'
- Tax rate 'percent_i' (percentage)

Brackets are sorted by upper bound:
    upper_(i-1) < upper_i

Tax is calculated progressively:
- First 'upper_0' dollars are taxed at 'percent_0'%
- Next (upper_1 - upper_0) dollars at 'percent_1'%
- Next (upper_2 - upper_1) dollars at 'percent_2'%
- And so on, until income is exhausted.

The upper bound of the last bracket is guaranteed >= income.

Return total tax as a float.

Example:
    brackets = [[3,50],[7,10],[12,25]], income = 10
    -> 2.65
"""

def calculate_tax(brackets: List[List[int]], income: int) -> float:
    pass



# ============================================================
# 5️⃣ Invalid Transactions (Parsing + Rules)
# ============================================================
"""
LeetCode-style: 1169. Invalid Transactions (Medium)

A transaction is a string:
    "name,time,amount,city"
where:
    - name:   string
    - time:   int (minutes from 0 to 1000)
    - amount: int
    - city:   string

A transaction is INVALID if:
1. amount > 1000, OR
2. exists ANOTHER transaction with the same 'name' such that:
   - |time1 - time2| <= 60, AND
   - city1 != city2

Given:
    transactions: List[str]

Return:
    List of all INVALID transactions (in any order).

Example:
    ["alice,20,800,mtv","alice,50,100,beijing"]
    -> both are invalid (same name, diff cities, within 60 mins).
"""

def invalidTransactions(transactions: List[str]) -> List[str]:
    pass
