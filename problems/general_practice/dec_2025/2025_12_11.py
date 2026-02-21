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
    # 1️⃣ DSA: Number of Islands (Grid DFS/BFS)
    # ---------------------------------------------------------
    """
    Problem:
      Given an m x n 2D grid map of '1's (land) and '0's (water),
      return the number of islands.

      An island is surrounded by water and is formed by connecting adjacent lands
      horizontally or vertically. You may assume all four edges of the grid are
      surrounded by water.

    Example 1:
      grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
      ]
      → 1

    Example 2:
      grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
      ]
      → 3

    Notes:
      - You can modify the grid in-place to mark visited cells, or maintain
        a separate visited set.
      - You can use either DFS or BFS.
    """
    def num_islands(self, grid: list[list[str]]) -> int:
        # Expected Time: O(m * n) — visit each cell at most once
        # Expected Space: O(m * n) in worst case for recursion/queue or visited
        pass


    # ---------------------------------------------------------
    # 2️⃣ Data Engineering: Deduplicate Events & Compute Per-User Total Amount
    # ---------------------------------------------------------
    """
    Problem (Data Engineering flavored):

      You are given a list of events from a transactional system. Each event is:
        (user_id: str, event_id: str, event_ts: int, amount: float)

      - user_id: identifies the user.
      - event_id: identifies the logical event (e.g., "order_123").
      - event_ts: UNIX timestamp (seconds) when the event version was produced.
      - amount: monetary value associated with the event (e.g., order amount).

      Because of late-arriving updates and retries, the same (user_id, event_id)
      pair may appear multiple times with different event_ts and amount.
      For example, an order might be updated after a status change.

      Task:

        1) First, **deduplicate** events by (user_id, event_id), keeping only the
           event with the **largest event_ts** (i.e., the latest version).

        2) Then, compute the total amount per user_id based on these deduplicated
           events.

      Return:
        A dictionary:
          user_id → total_amount (float)

      Example:

        events = [
          ("u1", "e1", 100, 10.0),
          ("u1", "e1", 120, 12.5),   # later version of same event
          ("u1", "e2", 90, 5.0),
          ("u2", "e5", 80, 20.0),
          ("u2", "e5", 95, 30.0),    # later version of same event
        ]

        Deduplicated (keeping latest ts for each (user,event)):
          ("u1", "e1", 120, 12.5)
          ("u1", "e2", 90, 5.0)
          ("u2", "e5", 95, 30.0)

        Per-user totals:
          u1: 12.5 + 5.0 = 17.5
          u2: 30.0

        Expected output:
          {
            "u1": 17.5,
            "u2": 30.0
          }

      Hints:
        - Use a dictionary keyed by (user_id, event_id) to track the latest event.
        - After deduplication, aggregate by user_id.


        - How to Deduplicate the events? And get the latest timestamp for that event? - Basically sort all the timestamps for each user, event
        - Group all event timestamps by user and event
        - Sort the event timestamps by user and event
        
        (u1, e1): [(100, 10.0), (120, 12.5)]
        - Instead of sorting just keep tab of max. Basically, compare current, new value. If new value is > then update the event_ts and amount

        - Now, group by user_id - For each user_id, calculate the sum of amounts

    """
    def dedup_events_and_sum_per_user(
        self,
        events: list[tuple[str, str, int, float]]
    ) -> dict[str, float]:
        # Expected Time: O(n) — single pass to dedup plus aggregation
        # Expected Space: O(n) — to store latest events and per-user totals
        dedup = defaultdict(tuple)

        for usr, event, ts, amt in events:
            if (usr, event) in dedup:
                if ts > dedup[(usr, event)][0]:
                    dedup[(usr, event)] = (ts, amt)
            else:
                dedup[(usr, event)] = (ts, amt)
        
        res = defaultdict(int)

        for usr_evnt, ts_amt in dedup.items():
            res[usr_evnt[0]] += ts_amt[1]
        return dict(res)

        



        


    # ---------------------------------------------------------
    # 3️⃣ Spark Continuation: Deduplicate Events & Sum Amount per User in PySpark
    # ---------------------------------------------------------
    """
    Spark Version of the DE Problem:

    Problem:
      Implement the same logic using PySpark DataFrame APIs.

    Input:
      A PySpark DataFrame `df` with schema:

        root
         |-- user_id: string
         |-- event_id: string
         |-- event_ts: long      -- UNIX timestamp in seconds
         |-- amount: double

      Semantics:
        - Each row is a version of an event.
        - You must keep only the latest version per (user_id, event_id),
          where "latest" = largest event_ts.
        - Then, compute total amount per user_id.

    Required Output:
      A PySpark DataFrame with schema:

        root
         |-- user_id: string
         |-- total_amount: double

      Where total_amount is the sum of deduplicated event amounts for that user.

    Example (conceptual):

      Input df:

        +--------+--------+---------+------+
        | user_id|event_id| event_ts|amount|
        +--------+--------+---------+------+
        | u1     | e1     | 100     |10.0  |
        | u1     | e1     | 120     |12.5  |
        | u1     | e2     | 90      |5.0   |
        | u2     | e5     | 80      |20.0  |
        | u2     | e5     | 95      |30.0  |
        +--------+--------+---------+------+

      After dedup by (user_id, event_id) on max(event_ts):

        +--------+--------+---------+------+
        | user_id|event_id| event_ts|amount|
        +--------+--------+---------+------+
        | u1     | e1     | 120     |12.5  |
        | u1     | e2     | 90      |5.0   |
        | u2     | e5     | 95      |30.0  |
        +--------+--------+---------+------+

      Aggregate per user:

        +--------+------------+
        | user_id|total_amount|
        +--------+------------+
        | u1     |17.5        |
        | u2     |30.0        |
        +--------+------------+

    Hints:
      - Common pattern:
          - Use window functions:
              ROW_NUMBER() OVER (PARTITION BY user_id, event_id ORDER BY event_ts DESC)
            then filter row_number = 1.
          - Or use groupBy(user_id, event_id) with max(event_ts), then join back.
          - Then groupBy(user_id) and sum(amount).

    You do NOT need to write actual Spark code here; just a function placeholder.
    """
    def dedup_events_and_sum_per_user_spark(self, df):
        """
        df: PySpark DataFrame with columns:
              - user_id (string)
              - event_id (string)
              - event_ts (long)
              - amount (double)

        return: PySpark DataFrame with columns:
              - user_id (string)
              - total_amount (double)

        Expected Time: O(n) distributed, plus overhead for window/groupBy
        Expected Space: O(n) distributed across the cluster
        """
        pass



# -------------------------------------------------------------
# Simple Test Harness (for your future implementations)
# -------------------------------------------------------------
if __name__ == "__main__":
    lc = Leetcode()

    # 1️⃣ Number of islands
    grid_example = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    print("1: num_islands →", lc.num_islands(grid_example))

    # 2️⃣ Dedup events and sum per user
    events_example = [
        ("u1", "e1", 100, 10.0),
        ("u1", "e1", 120, 12.5),
        ("u1", "e2", 90, 5.0),
        ("u2", "e5", 80, 20.0),
        ("u2", "e5", 95, 30.0),
    ]
    print("2: dedup_events_and_sum_per_user →",
          lc.dedup_events_and_sum_per_user(events_example))

    # 3️⃣ Spark continuation placeholder
    print("3: dedup_events_and_sum_per_user_spark →",
          lc.dedup_events_and_sum_per_user_spark(None))
