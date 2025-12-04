from collections import defaultdict

# ============================================================
# 1️⃣ Chat Rule Violations by User
# ============================================================
"""
Problem:
You are given:
- messages: a list of (user_id, message_text)
- banned: a list of banned words
- k: integer threshold

A user is NON-COMPLIANT if total occurrences of ANY banned words across
all messages is >= k.

Rules:
- Case-insensitive
- Word-boundary based
- Strip punctuation . , ! ?

Return sorted list of violating user_ids.


message = This trade has inside info.
- If any of the words is in the banned list 
- for each message, we are checking all the words if they are in the banned list
- Then keeping a counter for the banned words used for each user and checking the threshold


- We are iterating througn the input and creating a dict for each user id and the value can be a counter of banned words
"""

def non_compliant_users(messages, banned, k):
    temp = defaultdict(int)

    res = []

    for user, message in messages:
        count = sum(w.strip(".,!?").lower() in banned for w in message.split())        
        temp[user] += count    
    
    for key, v in temp.items():
        if v >= k:
            res.append(key)
    return sorted(res)

    



# ============================================================
# 2️⃣ Suspicious Trading Bursts (Sliding Window)
# ============================================================
"""
Given:
    trades = [(trader_id, timestamp_seconds), ...]

A trader is suspicious if in ANY 600-second window they made >= m trades.

Return sorted trader_ids.

    trades = [
        ("a", 100),
        ("a", 200),
        ("a", 400),
        ("a", 650),
        ("b", 100),
        ("b", 1200),
    ]
    m = 3

If in any 600 second window they made
- first we need find how many trades were made by the user in every 600 second window
for each user,
100, 200, 400, 650
    l           r
- sliding window for every 600 seconds if greater than 600 seconds then we need to move the left pointer
- then have a counter for the number of trades in that 600 second window

- I cannot directly do the sliding window over here because we need to store the a: ['100', '200', '400', '650']

"""

def suspicious_traders(trades, m):
    temp = defaultdict(list)
    
    # Very expensive in memory because the list size can be > 10 Mil and break
    for user, ts in trades:
        temp[user].append(ts)
    
    suspicious_traders = []

    for user, trade_lst in temp.items():
        l = 0
        for r in range(len(trade_lst)):            
            while trade_lst[r] - trade_lst[l] >= 600:
                l += 1
            window_size = r - l + 1
            if window_size >= m:
                suspicious_traders.append(user)
                break
    return suspicious_traders


# ============================================================
# 3️⃣ First Violation Timestamp per User
# ============================================================
"""
Given:
    events = [(timestamp, user_id, rule_id)]

Return:
    { user_id: earliest_timestamp }


    ev = [
        (100, "u1", "R1"),
        (90, "u2", "R3"),
        (120, "u1", "R2"),
        (95, "u2", "R1"),
    ]

    u1: [100, 120]    and u2: []

    - Find all timestamps for each user. So group all timestamps for each user. u1: [100, 120] and u2: [90, 95]
    - Sort the elements in the timestamps and return teh first element

    - Memory issue. Because the timestamps can be very large
"""

def first_violation_per_user(events):
    temp = defaultdict(list)

    for ts, user_id, _ in events:
        temp[user_id].append(ts)
    
    res = {}
    for user_id, ts_lst  in temp.items():
        sorted_lst = sorted(ts_lst)
        res[user_id] = sorted_lst[0]
    return res

# find the min as we iterate
def first_violation_per_user_optimal(events):
    res = {}

    for ts, user_id, _ in events:
        if user_id not in res:
            res[user_id] = ts
        else:
            if ts < res[user_id]:
                res[user_id] = ts
    return res





# ============================================================
# 4️⃣ Excessive Counterparty Exposure
# ============================================================
"""
Given trades:
    (trader_id, counterparty_id, notional_amount)

A trader is non-compliant if any (trader → counterparty) total exceeds limit.

Return sorted list of trader_ids.
"""

def overexposed_traders(trades, limit):
    pass


def has_proximity_violation(s, keywords_a, keywords_b, window_size):
    """
    Given:
    - s: message string
    - keywords_a: set[str]
    - keywords_b: set[str]
    - window_size: integer (# words)

    Return True if ANY window of size <= window_size contains:
    - at least 1 word from keywords_a
    - at least 1 word from keywords_b

    Matching is case-insensitive and strips . , ! ? from word boundaries.
    """
    if window_size <= 0:
        return False

    # Normalize keyword sets to lowercase
    A = {w.lower() for w in keywords_a}
    B = {w.lower() for w in keywords_b}

    if not A or not B:
        return False

    # Normalize message -> list of cleaned words
    words = [w.strip(".,!?").lower() for w in s.split() if w.strip(".,!?")]
    n = len(words)
    if n == 0:
        return False

    # Sliding window over words with counts of A/B hits
    countA = 0
    countB = 0
    l = 0

    for r in range(n):
        w = words[r]
        if w in A:
            countA += 1
        if w in B:
            countB += 1

        # Ensure window size <= window_size
        while r - l + 1 > window_size:
            left_w = words[l]
            if left_w in A:
                countA -= 1
            if left_w in B:
                countB -= 1
            l += 1

        # Check condition in current window [l, r]
        if countA > 0 and countB > 0:
            return True

    return False




# ============================================================
# TEST HARNESS FOR QUESTIONS 1–5
# ============================================================
if __name__ == "__main__":

    # print("\n--- Test 1: non_compliant_users ---")
    # msgs = [
    #     ("u1", "This trade has inside info."),
    #     ("u2", "Totally legit TRADE."),
    #     ("u1", "Do not share this INSIDER tip."),
    # ]
    # banned_words = ["inside", "insider"]
    # print(non_compliant_users(msgs, banned_words, k=2))  # Expected: ["u1"]


    # print("\n--- Test 2: suspicious_traders ---")
    # trades = [
    #     ("a", 100),
    #     ("a", 200),
    #     ("a", 400),
    #     ("a", 650),
    #     ("b", 100),
    #     ("b", 1200),
    # ]
    # print(suspicious_traders(trades, m=3))  # Expected: ["a"]


    # print("\n--- Test 3: first_violation_per_user ---")
    # ev = [
    #     (100, "u1", "R1"),
    #     (90, "u2", "R3"),
    #     (120, "u1", "R2"),
    #     (95, "u2", "R1"),
    # ]
    # print(first_violation_per_user_optimal(ev))  # Expected: {"u1": 100, "u2": 90}


    # print("\n--- Test 4: overexposed_traders ---")
    # trades2 = [
    #     ("t1", "c1", 50.0),
    #     ("t1", "c1", 60.0),
    #     ("t1", "c2", 100.0),
    #     ("t2", "c1", 30.0),
    #     ("t2", "c3", 20.0),
    # ]
    # print(overexposed_traders(trades2, limit=100.0))  # Expected: ["t1"]


    print("\n--- Test 5: has_proximity_violation ---")
    msg = "We should buy before the announcement and then quietly sell later"
    A = {"buy", "sell"}
    B = {"before", "insider", "tip"}
    print(has_proximity_violation(msg, A, B, window_size=4))  # Expected: True
