from collections import defaultdict

class Leetcode:
    """
    Batch 1 (Spark Day):
      - 1 DSA Problem (Python)
      - 1 Data Engineering Problem (Python)
      - 1 Spark Continuation Problem (PySpark)
    """


    # ---------------------------------------------------------
    # 1️⃣ DSA: Valid Parentheses with Multiple Types
    # ---------------------------------------------------------
    """
    Problem:
    Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
    determine if the input string is valid.

    A string is valid if:
      - Open brackets are closed by the same type of brackets.
      - Open brackets are closed in the correct order.

    Example:
      s = "()"        → True
      s = "()[]{}"    → True
      s = "(]"        → False
      s = "([)]"      → False
      s = "{[]}"      → True
    """
    def is_valid_parentheses(self, s: str) -> bool:
        # Expected Time: O(n)
        # Expected Space: O(n) for stack
        pass


    # ---------------------------------------------------------
    # 2️⃣ DE: Compute Average Session Time per User
    # ---------------------------------------------------------
    """
    Problem (Data Engineering flavored):
    You are given a list of session tuples:
        (user_id: str, session_start_ts: int, session_end_ts: int)

    - session timestamps are UNIX seconds.
    - Session duration = (end - start).

    Return:
      user_id → average_session_duration_in_seconds

    Example:
      sessions = [
        ("u1", 0, 100),      # duration = 100
        ("u1", 200, 260),    # duration = 60
        ("u2", 0, 20)        # duration = 20
      ]

      Output:
        {
          "u1": 80,   # (100 + 60)/2
          "u2": 20
        }
    """
    def avg_session_time(self, sessions: list[tuple[str, int, int]]) -> dict[str, float]:
        # Expected Time: O(n)
        # Expected Space: O(u) where u = number of users
        temp = defaultdict(lambda: {'total_dur': 0, 'total_len': 0})

        for session in sessions:
            temp[session[0]]['total_dur'] += session[2] - session[1]
            temp[session[0]]['total_len'] += 1
        
        res = {}
        for k, v in temp.items():
            res[k] = v['total_dur']/ v['total_len']
        return res




    # ---------------------------------------------------------
    # 3️⃣ Spark Continuation: Compute Average Session Time in Spark
    # ---------------------------------------------------------
    """
    Spark Version of the DE Problem:

    Problem:
      Using PySpark, compute the average session duration per user.

    Input Spark DataFrame schema:
      root
       |-- user_id: string
       |-- session_start_ts: long
       |-- session_end_ts: long

    Required Output:
      DataFrame with:
       |-- user_id: string
       |-- avg_session_duration: double

    Example Data:
        +--------+-----------------+---------------+
        | user_id| session_start_ts| session_end_ts|
        +--------+-----------------+---------------+
        | u1     | 0               | 100           |
        | u1     | 200             | 260           |
        | u2     | 0               | 20            |
        +--------+-----------------+---------------+

    Expected Output:
        +--------+----------------------+
        | user_id| avg_session_duration |
        +--------+----------------------+
        | u1     | 80.0                 |
        | u2     | 20.0                 |
        +--------+----------------------+

    Notes:
      - You must compute (session_end_ts - session_start_ts).
      - Group by user_id.
      - Compute avg duration per user.
      - Return a DataFrame.

    Do NOT write actual Spark code — only a function placeholder.
    """
    def avg_session_time_spark(self, df):
        """
        Expected Time: O(n) distributed
        Expected Space: O(n) distributed across cluster

        df: PySpark DataFrame with columns:
            - user_id (string)
            - session_start_ts (long)
            - session_end_ts (long)

        return: PySpark DataFrame with:
            - user_id (string)
            - avg_session_duration (double)
        """
        pass



# -------------------------------------------------------------
# Test Harness
# -------------------------------------------------------------
if __name__ == "__main__":
    lc = Leetcode()

    # print("1: is_valid_parentheses →", lc.is_valid_parentheses("()[]{}"))
    
    sessions_example = [
        ("u1", 0, 100),
        ("u1", 200, 260),
        ("u2", 0, 20)
    ]
    print("2: avg_session_time →", lc.avg_session_time(sessions_example))

    # print("3: avg_session_time_spark →", lc.avg_session_time_spark(None))  # placeholder
