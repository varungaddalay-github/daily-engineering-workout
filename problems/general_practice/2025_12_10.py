from collections import defaultdict, deque
import datetime

class Leetcode:
    """
    Batch: 
      - 1 DSA Problem (Python)
      - 1 Data Engineering Problem (Python)
      - 1 Spark Continuation Problem (PySpark)
    No solutions. Placeholders + complexity expectations only.
    """

    # ---------------------------------------------------------
    # 1️⃣ DSA: Course Schedule (Can You Finish All Courses?)
    # ---------------------------------------------------------
    """
    Problem:
      There are num_courses courses labeled from 0 to num_courses - 1.
      You are given a list of prerequisite pairs where
        prerequisites[i] = [a, b]
      means you must take course b before course a (b → a edge).

      Return True if it is possible to finish all courses, otherwise False.

    Example 1:
      num_courses = 2
      prerequisites = [[1,0]]
      Explanation:
        To take course 1 you must first take 0. This is possible.
      Output: True

    Example 2:
      num_courses = 2
      prerequisites = [[1,0],[0,1]]
      Explanation:
        0 depends on 1 and 1 depends on 0 → cycle.
      Output: False

    Notes:
      - This is a directed graph problem.
      - You need to detect if there is a cycle.
      - You can use DFS with coloring or Kahn's algorithm (BFS topological sort).
    """
    def can_finish_courses(self, num_courses: int, prerequisites: list[list[int]]) -> bool:
        # Expected Time: O(V + E) where V = num_courses, E = len(prerequisites)
        # Expected Space: O(V + E) for adjacency list + recursion/queue
        pass


    # ---------------------------------------------------------
    # 2️⃣ Data Engineering: Daily Active Users + 7-Day Rolling Active Users
    # ---------------------------------------------------------
    """
    Problem (Data Engineering flavored):

      You are given a list of login events:
        (user_id: str, login_date: str)

      - login_date is a string in "YYYY-MM-DD" format (assume valid).
      - A user can have multiple logins on the same day; each event is a row.

      Task:
        For each calendar date present in the data, compute:
          - daily_active_users: number of UNIQUE users who logged in that day. - Set of all the user_ids
          - rolling_7d_active_users: number of UNIQUE users who logged in - For each date, we are trying to get all the active users in the last 7 days
            in the 7-day window ending on that date (inclusive).

      Return:
        A dictionary:
          date_str → (daily_active_users: int, rolling_7d_active_users: int)

      Notes:
        - You may assume all dates are in the same timezone.
        - You should treat the 7-day window as:
            [date - 6 days, date] inclusive.
        - Input may not be sorted by date.

      Example (small conceptual example):

        events = [
          ("u1", "2025-11-20"),
          ("u2", "2025-11-20"),
          ("u1", "2025-11-21"),
          ("u3", "2025-11-21"),
          ("u1", "2025-11-26"),
        ]

        For 2025-11-20:
          - daily_active_users = 2  (u1, u2)
          - rolling_7d_active_users = 2  (u1, u2)

        For 2025-11-21:
          - daily_active_users = 2  (u1, u3)
          - rolling_7d_active_users = 3  (u1, u2, u3) across 20th–21st

        For 2025-11-26:
          - daily_active_users = 1  (u1)
          - rolling_7d_active_users:
              window is 2025-11-20..2025-11-26
              users = {u1, u2, u3} → 3

      Hints:
        - You’ll likely want to:
            - group events by date → set of user_ids
            - sort dates
            - maintain a sliding window of the last 7 dates and a union of user_ids
              (or recompute efficiently).

        - For each date, we are trying to get all the active users in the last 7 days 

        - Set to store for each day - If i can just do a count on the fly for each date
        - And for the rolling 7D window, we need to have a union while calculating the total

        daily_active_users = {
            "2025-11-20": 2,
            "2025-11-21": 2,
            "2025-11-26": 1,
        }

        rolling_7d_active_unique_users = {
            "2025-11-20": 2,
            "2025-11-21": 3,

        }

        2 sets for each date: 1 for the daily active users and 1 for the rolling 7D active unique users

        res = 
        {
            "2025-11-20": ("daily_active_users": 2, "rolling_7d_active_users": 2),
            "2025-11-21": ("daily_active_users": 2, "rolling_7d_active_users": 3),
            "2025-11-26": ("daily_active_users": 1, "rolling_7d_active_users": 3),
        }

        events = [
          ("u1", "2025-11-20"),
          ("u2", "2025-11-20"),
          ("u1", "2025-11-21"),
          ("u3", "2025-11-21"),
          ("u1", "2025-11-26"),
        ]        
        
        
    """
    def daily_and_7d_active_users(
        self,
        events: list[tuple[str, str]]
    ) -> dict[str, tuple[int, int]]:
        # Expected Time: O(n log n) due to sorting by date, plus windowing overhead
        # Expected Space: O(n) for per-day user sets and rolling windows
        res = defaultdict(lambda: {
            "daily_active_users": 0,
            "rolling_7d_active_users": 0
        })

        daily_users = defaultdict(set)
        
        for usr, dt in events:
            daily_users[dt].add(usr)

        sorted_dts = sorted(daily_users.keys())

        res = {}
        window = deque()

        for dt in sorted_dts:
            curr_dt = datetime.datetime.strptime(dt, "%Y-%m-%d")            
            window_start = curr_dt - datetime.timedelta(days=6)

            while window:
                old_dt, _ = window[0]
                old_dt = datetime.datetime.strptime(old_dt, "%Y-%m-%d")
                if old_dt < window_start:
                    window.popleft()
                else:
                    break
            
            window.append((dt, daily_users[dt]))
            rolling_users = set()
            for _, users in window:
                rolling_users.update(users)
            
            daily_active = len(daily_users[dt])
            rolling_7D_active = len(rolling_users)
            res[dt] = (daily_active, rolling_7D_active)

        return res


    # ---------------------------------------------------------
    # 3️⃣ Spark Continuation: DAU + 7-Day Rolling Active Users in PySpark
    # ---------------------------------------------------------
    """
    Spark Version of the DE Problem:

    Problem:
      Implement the same "Daily Active Users + 7-Day Rolling Active Users"
      computation using PySpark.

    Input:
      A PySpark DataFrame with the following schema:

        root
         |-- user_id: string
         |-- login_date: date   -- (or string convertible to date)

      Task:
        Produce a DataFrame with:

         |-- login_date: date
         |-- daily_active_users: long
         |-- rolling_7d_active_users: long

      Definitions:
        - daily_active_users:
            count(DISTINCT user_id) for that exact login_date.
        - rolling_7d_active_users:
            count(DISTINCT user_id) for all login_date in the window
            [login_date - 6 days, login_date].

      Example (conceptual):

        Input df:

          user_id | login_date
          --------+-----------
          u1      | 2025-11-20
          u2      | 2025-11-20
          u1      | 2025-11-21
          u3      | 2025-11-21
          u1      | 2025-11-26

        Output df:

          login_date  | daily_active_users | rolling_7d_active_users
          ------------+--------------------+-------------------------
          2025-11-20  |         2          |            2
          2025-11-21  |         2          |            3
          2025-11-26  |         1          |            3

      Hints:
        - Consider:
            - first computing daily_active_users via groupBy(login_date).
            - then using a window function over a 7-day range if supported
              (or joining on date ranges).
            - DISTINCT over a date range is tricky; one approach is:
                - explode a date range per user and aggregate,
                  or
                - deduplicate (user_id, login_date), then use a window.
        - Exact implementation details depend on PySpark capabilities and constraints.

    You do NOT need to write actual Spark code here; just a function placeholder.
    """
    def daily_and_7d_active_users_spark(self, df):
        """
        df: PySpark DataFrame with columns:
              - user_id (string)
              - login_date (date or string)

        return: PySpark DataFrame with columns:
              - login_date (date)
              - daily_active_users (long)
              - rolling_7d_active_users (long)

        Expected Time: O(n) distributed, plus window aggregation cost
        Expected Space: O(n) distributed across the cluster
        """
        pass



# -------------------------------------------------------------
# Simple Test Harness (for your future implementations)
# -------------------------------------------------------------
if __name__ == "__main__":
    lc = Leetcode()

    # 1️⃣ Can finish courses
    print("1: can_finish_courses →",
          lc.can_finish_courses(2, [[1, 0]]))

    # 2️⃣ Daily and 7-day active users
    events_example = [
        ("u1", "2025-11-20"),
        ("u2", "2025-11-20"),
        ("u1", "2025-11-21"),
        ("u3", "2025-11-21"),
        ("u1", "2025-11-26"),
    ]
    print("2: daily_and_7d_active_users →",
          lc.daily_and_7d_active_users(events_example))

    # 3️⃣ Spark continuation placeholder
    print("3: daily_and_7d_active_users_spark →",
          lc.daily_and_7d_active_users_spark(None))
