from collections import Counter
from collections import defaultdict, deque

class Leetcode:
    """
    Batch:
      - 1 DSA Problem (Python)
      - 1 Data Engineering Problem (Python)
      - 1 Spark Continuation Problem (PySpark)
    No solutions. Placeholders + complexity expectations only.
    """


    # ---------------------------------------------------------
    # 1️⃣ DSA: Find All Anagrams in a String
    # ---------------------------------------------------------
    """
    Problem:
      Given two strings s and p, return a list of all start indices of p's anagrams in s.
      The answer can be returned in any order.

      An anagram is a permutation of the letters of p.

    Example 1:
      s = "cbaebabacd", p = "abc"
      Output: [0, 6]
      Explanation:
        - s[0:3] = "cba" is an anagram of "abc"
        - s[6:9] = "bac" is an anagram of "abc"

    Example 2:
      s = "abab", p = "ab"
      Output: [0, 1, 2]
      Explanation:
        - "ab", "ba", "ab" are all anagrams of "ab"

    Notes:
      - Sliding window + frequency counts.
      - Be careful about time complexity when comparing frequency maps.
    """
    def find_anagrams(self, s: str, p: str) -> list[int]:
        # Expected Time: O(n) where n = len(s) (assuming fixed alphabet or efficient diff tracking)
        # Expected Space: O(1) or O(k) where k is alphabet size / unique chars in p
        def is_anagram(p, window):
            return Counter(p) == Counter(window)
        
        l = 0
        res = []
        for r in range(len(s)):
            if (r - l + 1) == len(p):
                if is_anagram(p, s[l:r+1]):
                    res.append(l)
                l += 1
        return res        


    # ---------------------------------------------------------
    # 2️⃣ Data Engineering: Detect API Abuse (100+ requests in any rolling 60s window)
    # ---------------------------------------------------------
    """
    Problem (Data Engineering flavored):

      Logs come as:
        (user_id: str, timestamp_seconds: int)

      A user is considered "abusive" if they exceed 100 (3) requests
      in ANY rolling 60-second window (inclusive).

      Task:
        Return a set of abusive user_ids.

      Example:
        logs = [
          ("u1", 1), ("u1", 2), ..., ("u1", 101)   # all within 60 seconds
        ]
        → {"u1"}

      Notes:
        - Logs may be unsorted.
        - Multiple users are interleaved.
        - You must detect existence of ANY window with >100 (3) events for that user.
        - Assume timestamps are in seconds (integers).
        - Think about scale: millions of events, many users, skew (a few very hot users).


        - Basically, grouping the number of events for a specific user in the last 60 seconds
        - Grouping the events by the user_id - 
        {
            u1: [1, 2, 3, 50, 80],
            u2: [20, 85]
        }
        - Sliding window of 60 seconds for each user
        
    """
    def detect_api_abuse(self, logs: list[tuple[str, int]]) -> set[str]:
        # Expected Time: O(n log n) if you sort per user or globally, then two-pointer per user
        # Expected Space: O(n) for grouping per user (can be reduced with streaming assumptions)
        temp = defaultdict(list)
        
        for event, ts in logs:
            temp[event].append(ts)
        
        # sort the values in the dict
        for _, v in temp.items():
            v.sort()

        res = set()

        for k, v in temp.items():            
            l = 0
            for r in range(len(v)):
                while v[r] - v[l] >= 60:
                    res.add(k)
                    l += 1
                window_size = r - l + 1
                if window_size > 3:
                    res.add(k)
                    break
        return res
                

    def detect_api_abuse_optimized(self, logs):
        # external sort + stream - So no dict with event_ts lists
        res = set()
        
        logs.sort(key=lambda x: (x[0], x[1]))

        curr_usr = None
        window = []

        for usr, ts in logs:
            if usr != curr_usr:
                curr_usr = usr
                window = [ts]
            else:
                window.append(ts)

                while window and ts - window[0] > 60:
                    window.pop(0)
                
                if len(window) > 3:
                    res.add(usr)
                    window = []

        return res


        


    # ---------------------------------------------------------
    # 3️⃣ Spark Continuation: Detect API Abuse in PySpark
    # ---------------------------------------------------------
    """
    Spark Version of the DE Problem:

    Problem:
      Implement abusive-user detection in PySpark.

    Input:
      PySpark DataFrame `df` with schema:

        root
         |-- user_id: string
         |-- ts: long   -- timestamp in seconds

    Output:
      A DataFrame (or list) of abusive user_ids (distinct) where:
        - There exists a 60-second window where the user has > 100 events.

    Constraints / Notes:
      - Logs can be huge (billions of rows).
      - Data may be skewed (a few users dominate traffic).
      - Exact requirement: detect existence, not count all windows.

    Hints (conceptual, no code required):
      - Consider using Spark's windowed aggregations:
          - groupBy(window(col("ts"), "60 seconds"), col("user_id")).count()
        BUT beware:
          - standard tumbling windows are NOT the same as "any rolling window."
      - For true rolling windows:
          - you may need event-time range joins or per-user ordered windows.
      - A practical approximation might use:
          - 1-second buckets per user then sliding sum over 60 seconds.
      - Define expected behavior explicitly (exact rolling vs acceptable approximation).

    You do NOT need to write actual Spark code here; just a function placeholder.
    """
    def detect_api_abuse_spark(self, df):
        """
        df: PySpark DataFrame with columns:
              - user_id (string)
              - ts (long)

        return: PySpark DataFrame (or collection) with distinct abusive user_ids

        Expected Time: O(n) distributed + window/join overhead
        Expected Space: O(n) distributed
        """
        pass



# -------------------------------------------------------------
# Simple Test Harness (for your implementations)
# -------------------------------------------------------------
if __name__ == "__main__":
    lc = Leetcode()

    # 1️⃣ Find anagrams
    print("1: find_anagrams →", lc.find_anagrams("abab", "ab"))

    # 2️⃣ Detect API abuse (toy example; not actually 101 rows here)
    logs_example = [
        ("u1", 1), ("u1", 2), ("u1", 3),
        ("u2", 10), ("u2", 80),
        ("u1", 50), ("u1", 60),
    ]
    print("2: detect_api_abuse →", lc.detect_api_abuse_optimized(logs_example))

    # 3️⃣ Spark continuation placeholder
    print("3: detect_api_abuse_spark →", lc.detect_api_abuse_spark(None))
