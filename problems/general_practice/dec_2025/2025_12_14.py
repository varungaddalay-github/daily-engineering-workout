from collections import defaultdict

class Leetcode:
    """
    Batch:
      - 1 DSA Problem (Python)
      - 1 Data Engineering Problem (Python)
      - 1 Spark Continuation Problem (PySpark)
    No solutions. Placeholders + complexity expectations only.
    """


    # ---------------------------------------------------------
    # 1️⃣ DSA: Longest Substring with At Most K Distinct Characters
    # ---------------------------------------------------------
    """
    Problem:
      Given a string s and an integer k, return the length of the longest
      substring of s that contains at most k distinct characters.

    Examples:
      1) s = "eceba", k = 2
         - Longest substring with at most 2 distinct chars is "ece" → length 3

      2) s = "aa", k = 1
         - Longest substring = "aa" → length 2

      3) s = "aabacbebebe", k = 3
         - One such substring is "cbebebe" → length 7

    Notes:
      - Classic sliding window + hashmap/frequency-count problem.
      - You should be able to solve it in O(n) by expanding the window
        and shrinking when you exceed k distinct characters.
    """
    def length_of_longest_substring_k_distinct(self, s: str, k: int) -> int:
        # Expected Time: O(n) where n = len(s)
        # Expected Space: O(min(n, k)) for the hashmap of character counts        

        l = 0
        freq = defaultdict(int)
        max_len = 0

        for r, ch in enumerate(s):
            freq[ch] += 1

            while len(freq) > k:
                left_ch = s[l]
                freq[left_ch] -= 1
                if freq[left_ch] == 0:
                    del freq[left_ch]
                l += 1
            
            max_len = max(max_len, r - l + 1)
        return max_len
    


    # ---------------------------------------------------------
    # 2️⃣ Data Engineering: User Sessionization by 30-Minute Gaps
    # ---------------------------------------------------------
    """
    Problem (Data Engineering flavored):

      You are given a list of events:
        (user_id: str, event_ts: int)   # event_ts = UNIX timestamp in seconds

      A "session" is defined per user as a sequence of events where
        consecutive events are no more than 30 minutes (1800 seconds) apart.

      If the gap between two events exceeds 30 minutes,
      a NEW session must start.

      Task:
        For each user, compute:
          - total number of sessions
          - average session length in seconds
            (session_length = last_event_ts - first_event_ts)

      Return:
        A dictionary:
          user_id → {
              "sessions": <int>,
              "avg_session_length": <float>
          }

      Example:

        events = [
          ("u1", 100),          # session1 starts
          ("u1", 400),          # still session1 (300 sec apart)
          ("u1", 2100),         # new session (gap = 1700 > 1800)
          ("u2", 50),           # session1
          ("u2", 100),          # same session
          ("u2", 5000),         # new session
        ]

        u1:
          session1 length = 400 - 100 = 300
          session2 length = 2100 - 2100 = 0
          total sessions = 2
          avg session length = (300 + 0) / 2 = 150

        u2:
          session1 length = 100 - 50 = 50
          session2 length = 5000 - 5000 = 0
          avg session length = 25

        Output:
          {
            "u1": {"sessions": 2, "avg_session_length": 150},
            "u2": {"sessions": 2, "avg_session_length": 25}
          }

      Notes:
        - Must sort events per user by timestamp.
        - Streaming logs may require online sessionization.
    """
    def user_sessionization(
        self,
        events: list[tuple[str, int]]
    ) -> dict[str, dict[str, float]]:
        # Expected Time: O(n log n) due to sorting per user
        # Expected Space: O(n)
        user_ts = defaultdict(list)

        for usr, ts in events:
            user_ts[usr].append(ts)
        
        res = {}

        for usr, ts_lst in user_ts.items():
            ts_lst.sort()
            sessions = 0
            total_session_len = 0

            session_start = ts_lst[0]
            prev_ts = ts_lst[0]

            for ts in ts_lst[1:]:
                if ts - prev_ts > 1800:
                    sessions += 1
                    total_session_len += prev_ts - session_start
                    session_start = ts
                prev_ts = ts

            sessions += 1
            total_session_len += prev_ts - session_start
            avg_len = total_session_len / sessions if sessions > 0 else 0.0

            res[usr] = {'sessions': sessions, 'avg_session_length': float(avg_len)}
        
        return res


if __name__ == "__main__":
    lc = Leetcode()

    # 1️⃣ Longest substring with at most K distinct characters
    print("1: length_of_longest_substring_k_distinct →",
          lc.length_of_longest_substring_k_distinct("aabacbebebe", 3))


    # 2️⃣ User sessionization
    events_example = [
        ("u1", 100),
        ("u1", 400),
        ("u1", 2100),
        ("u2", 50),
        ("u2", 100),
        ("u2", 5000),
    ]
    print("2: user_sessionization →",
          lc.user_sessionization(events_example))