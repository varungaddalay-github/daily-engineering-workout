from collections import defaultdict, deque

# ============================================================
# 6️⃣ Linked Accounts (Connected Components)
# ============================================================
"""
Given account links:
    links = [(acct1, acct2)]

    links = [
        ("a1", "a2"),
        ("a2", "a3"),
        ("b1", "b2"),
        ("c1", "c2"),
        ("c2", "c3"),
        ("c3", "c4"),
    ]    

    a1: a2
    a2: a3
    b1: b2
    c1: c2
    c2: c3
    c3: c4

    [a1 -> a2 -> a3], [b1 -> b2], [c1 -> c2 -> c3 -> c4]

    Create an adj list
    a1: a2
    a2: a1, a3
    b1: b2
    b2: b1
    c1: c2
    c2: c1, c3
    c3: c2, c4
    c4: c3

An entity is suspicious if its connected component size > k.

Return sorted list of ALL accounts in suspicious components.
"""

def wrong_suspicious_linked_accounts(links, k):
    # create an adj list
    adj_list = defaultdict(list)

    for u, v in links:
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    # calculate the component size and check if > k
    res = set()

    for key, v in adj_list.items():        
        if len(v) >= k:
            res.add(key)
            for i in v:
                res.add(i)
    return sorted(res)



def suspicious_linked_accounts(links, k):
    adj_list = defaultdict(list)

    for u, v in links:
        adj_list[u].append(v)
        adj_list[v].append(u)

    visited = set()
    res = set()

    for node in adj_list:
        if node not in visited:
            q = deque([node])  
            component = []
            visited.add(node)

            while q:
                curr = q.popleft()
                component.append(curr)
                for neighbor in adj_list[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
            
            if len(component) > k:
                res.update(component)
    return sorted(res)



# ============================================================
# 7️⃣ Daily Limit Breach
# ============================================================
"""
Given:
    txns = [(user_id, date_str, amount)]

A user violates if total for ANY date exceeds daily_limit.

Return sorted list of violators.
"""

def daily_limit_breach(txns, daily_limit):
    pass


# ============================================================
# 8️⃣ Consecutive Days Activity Streak
# ============================================================
"""
Given:
    events = [(user_id, date_str)]

Compute each user's max streak of consecutive calendar days.

Return:
    { user_id: max_streak }
"""

def max_activity_streak(events):
    pass


# ============================================================
# 9️⃣ Redact Sensitive Account Patterns
# ============================================================
"""
Given a string s, redact any token of form:
    "ACC" + >=4 digits

Example matches: ACC1234, ACC99999
Non-matches: ACC12, ACX1234

Replace with "REDACTED" and return string.
"""

def redact_accounts(s):
    pass


# ============================================================
# 🔟 Users Exceeding Per-Rule Limits
# ============================================================
"""
Given:
- violations = [(user_id, rule_id)]
- rule_limits = {rule_id: max_allowed_count}

A user violates if they exceed ANY rule's limit.

Return sorted user_ids.
"""

def users_exceeding_rule_limits(violations, rule_limits):
    pass



# ============================================================
# TEST HARNESS FOR QUESTIONS 6–10
# ============================================================
if __name__ == "__main__":

    print("\n--- Test 6: suspicious_linked_accounts ---")
    links = [
        ("a1", "a2"),
        ("a2", "a3"),
        ("b1", "b2"),
        ("c1", "c2"),
        ("c2", "c3"),
        ("c3", "c4"),
    ]
    print(suspicious_linked_accounts(links,k=2))
    # Expected: ["a1","a2","a3","c1","c2","c3","c4"]


    print("\n--- Test 7: daily_limit_breach ---")
    txns = [
        ("u1", "2025-12-01", 50.0),
        ("u1", "2025-12-01", 60.0),
        ("u1", "2025-12-02", 20.0),
        ("u2", "2025-12-01", 90.0),
        ("u2", "2025-12-01", 5.0),
    ]
    print(daily_limit_breach(txns, daily_limit=100.0))  # Expected: ["u1"]


    print("\n--- Test 8: max_activity_streak ---")
    ev2 = [
        ("u1", "2025-12-01"),
        ("u1", "2025-12-02"),
        ("u1", "2025-12-04"),
        ("u1", "2025-12-05"),
        ("u2", "2025-12-10"),
        ("u2", "2025-12-11"),
    ]
    print(max_activity_streak(ev2))  # Expected: {"u1": 2, "u2": 2}


    print("\n--- Test 9: redact_accounts ---")
    s = "Send this to ACC1234, but not to ACC12 or ACC99999."
    print(redact_accounts(s))
    # Expected: "Send this to REDACTED, but not to ACC12 or REDACTED."


    print("\n--- Test 10: users_exceeding_rule_limits ---")
    violations = [
        ("u1", "R1"),
        ("u1", "R1"),
        ("u1", "R2"),
        ("u2", "R1"),
        ("u2", "R1"),
        ("u2", "R1"),
    ]
    limits = {"R1": 2, "R2": 1}
    print(users_exceeding_rule_limits(violations, limits))  # Expected: ["u2"]
