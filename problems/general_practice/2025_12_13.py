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
        pass


    # ---------------------------------------------------------
    # 2️⃣ Data Engineering: Daily Error Rate per Service
    # ---------------------------------------------------------
    """
    Problem (Data Engineering flavored):

      You are given HTTP request logs as a list of tuples:
        (service_name: str, timestamp: str, status_code: int)

      - timestamp is an ISO-like string: "YYYY-MM-DDTHH:MM:SSZ".
      - service_name identifies the microservice (e.g., "auth", "payments", "orders").

      Define:
        - A request is considered an "error" if status_code >= 400.
        - The "day" is derived from timestamp as the "YYYY-MM-DD" part.

      Task:
        For each (service_name, day), compute:
          - total_requests: total number of requests
          - error_requests: number of error requests
          - error_rate: error_requests / total_requests (float between 0 and 1)

      Return:
        A dictionary:
          (service_name, day_str) → (total_requests: int, error_requests: int, error_rate: float)

      Example:

        logs = [
          ("auth",    "2025-11-21T10:00:00Z", 200),
          ("auth",    "2025-11-21T10:05:00Z", 500),
          ("payments","2025-11-21T11:00:00Z", 200),
          ("payments","2025-11-21T11:10:00Z", 404),
          ("auth",    "2025-11-22T09:00:00Z", 503),
        ]

        For ("auth","2025-11-21"):
          total_requests = 2
          error_requests = 1 (status 500)
          error_rate = 0.5

        For ("payments","2025-11-21"):
          total_requests = 2
          error_requests = 1 (status 404)
          error_rate = 0.5

        For ("auth","2025-11-22"):
          total_requests = 1
          error_requests = 1
          error_rate = 1.0

        Possible output:
          {
            ("auth",    "2025-11-21"): (2, 1, 0.5),
            ("payments","2025-11-21"): (2, 1, 0.5),
            ("auth",    "2025-11-22"): (1, 1, 1.0),
          }

      Notes:
        - Input can be large (millions of rows).
        - You should parse date strings efficiently (or use slicing: ts[:10]).

        total_requests
        - ("auth", "date"): total_count

        error_request
        - ("auth", "date"): if error_code >= 400

    """
    def daily_error_rate_per_service(
        self,
        logs: list[tuple[str, str, int]]
    ) -> dict[tuple[str, str], tuple[int, int, float]]:
        # Expected Time: O(n)
        # Expected Space: O(m) where m is number of distinct (service, day) pairs
        
        total_requests = defaultdict(lambda: {'total': 0, 'error': 0} )        

        for svc, ts, code in logs:
            key = (svc, ts[:10])
            total_requests[key]['total'] += 1
            if code >= 400:
                total_requests[key]['error'] += 1

        result = {}
        for key, counts in total_requests.items():
            totals = counts['total']
            errors = counts['error']
            error_rate = errors/totals
            result[key] = (totals, errors, error_rate)
        
        return result
                




    # ---------------------------------------------------------
    # 3️⃣ Spark Continuation: Daily Error Rate per Service in PySpark
    # ---------------------------------------------------------
    """
    Spark Version of the DE Problem:

    Problem:
      Implement the same "Daily Error Rate per Service" logic using PySpark.

    Input:
      A PySpark DataFrame `df` with schema:

        root
         |-- service_name: string
         |-- timestamp: timestamp   -- or string convertible to timestamp
         |-- status_code: integer

      Task:
        Produce a DataFrame with:

         |-- service_name: string
         |-- day: date
         |-- total_requests: long
         |-- error_requests: long
         |-- error_rate: double

        Where:
          - day is derived from timestamp (DATE(timestamp)).
          - error_requests = count of rows with status_code >= 400 per (service_name, day).
          - total_requests = total count of rows per (service_name, day).
          - error_rate = error_requests / total_requests.

      Example (conceptual):

        Input df:

          service_name |       timestamp        | status_code
          -------------+------------------------+------------
          auth         | 2025-11-21 10:00:00    | 200
          auth         | 2025-11-21 10:05:00    | 500
          payments     | 2025-11-21 11:00:00    | 200
          payments     | 2025-11-21 11:10:00    | 404
          auth         | 2025-11-22 09:00:00    | 503

        Output df:

          service_name |    day      | total_requests | error_requests | error_rate
          -------------+-------------+----------------+----------------+-----------
          auth         | 2025-11-21  |       2        |       1        |   0.5
          payments     | 2025-11-21  |       2        |       1        |   0.5
          auth         | 2025-11-22  |       1        |       1        |   1.0

      Hints:
        - Derive day with to_date(timestamp) or DATE(timestamp).
        - Use a CASE WHEN or a boolean expression to count errors.
        - groupBy(service_name, day) and aggregate:
            total_requests = count(*)
            error_requests = sum( (status_code >= 400).cast("int") )
            error_rate = error_requests / total_requests
        - Return a DataFrame with the required schema.

    You do NOT need to write actual Spark code here; just a function placeholder.
    """
    def daily_error_rate_per_service_spark(self, df):
        """
        df: PySpark DataFrame with columns:
              - service_name (string)
              - timestamp (timestamp or string)
              - status_code (int)

        return: PySpark DataFrame with columns:
              - service_name (string)
              - day (date)
              - total_requests (long)
              - error_requests (long)
              - error_rate (double)

        Expected Time: O(n) distributed, plus groupBy overhead
        Expected Space: O(n) distributed across the cluster
        """
        pass



# -------------------------------------------------------------
# Simple Test Harness (for your implementations)
# -------------------------------------------------------------
if __name__ == "__main__":
    lc = Leetcode()

    # 1️⃣ Longest substring with at most K distinct characters
    print("1: length_of_longest_substring_k_distinct →",
          lc.length_of_longest_substring_k_distinct("eceba", 2))

    # 2️⃣ Daily error rate per service
    logs_example = [
        ("auth",    "2025-11-21T10:00:00Z", 200),
        ("auth",    "2025-11-21T10:05:00Z", 500),
        ("payments","2025-11-21T11:00:00Z", 200),
        ("payments","2025-11-21T11:10:00Z", 404),
        ("auth",    "2025-11-22T09:00:00Z", 503),
    ]
    print("2: daily_error_rate_per_service →",
          lc.daily_error_rate_per_service(logs_example))

    # 3️⃣ Spark continuation placeholder
    print("3: daily_error_rate_per_service_spark →",
          lc.daily_error_rate_per_service_spark(None))
