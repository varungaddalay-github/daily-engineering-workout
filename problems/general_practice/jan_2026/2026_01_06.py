from collections import Counter, defaultdict
import heapq


class Leetcode:
    # ============================================================
    # 1) DSA Problem (Medium, no DP): Top K Frequent Elements
    # ============================================================
    # Problem:
    # Given an integer array nums and an integer k, return the k most frequent elements.
    # You may return the answer in any order.
    #
    # Notes:
    # - An element's frequency is the number of times it appears in nums.
    # - k is valid: 1 <= k <= number of unique elements.
    #
    # Examples:
    # nums = [1,1,1,2,2,3], k = 2  -> [1,2]
    # nums = [1], k = 1          -> [1]
    #
    # Function signature:
    # def topKFrequent(self, nums: list[int], k: int) -> list[int]:
    #
    # Expected complexity (comment only):
    # Time: O(n) average (or O(n log k) depending on approach)
    # Space: O(n)

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        heap = []
        freq_map = Counter(nums)

        for key, v in freq_map.items():
            heapq.heappush(heap, (v, key))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for _, num in heap]
    
    def topKFrequent_buckets(self, nums: list[int], k: int) -> list[int]:
        freq_map = Counter(nums)

        buckets = [[] for _ in range(len(nums)+1)]

        for num, freq in freq_map.items():
            buckets[freq].append(num)
        
        res = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res
        return res




    # ============================================================
    # 2) Data Engineering Problem (Python): 30-min Rolling Metrics with Late Events + Dedup
    # ============================================================
    # Scenario (Meta-scale flavored):
    # You ingest clickstream events from mobile clients. Events can arrive late/out-of-order.
    # You must compute rolling 30-minute per-user metrics at "query time" over an in-memory batch
    # of events, while deduplicating retries.
    #
    # Each event record:
    # - event_id: globally unique string (but retries can repeat the same event_id)
    # - user_id: string
    # - event_ts: integer epoch seconds when event happened (event time)
    # - ingest_ts: integer epoch seconds when your pipeline received it (processing time)
    # - event_type: string in {"view", "click", "purchase"}
    #
    # Requirements:
    # A) Deduplicate by event_id, keeping the earliest ingest_ts (the "first seen" copy).
    # B) Apply a lateness watermark: only include events where
    #       ingest_ts <= query_ts
    #   and
    #       event_ts >= query_ts - (30*60 + allowed_lateness_secs)
    #   (i.e., you will consider events up to 30 minutes of rolling window plus a lateness buffer).
    # C) For each user_id, compute at query_ts:
    #    - views_30m: count of "view" events with event_ts in (query_ts-30m, query_ts]
    #    - clicks_30m: count of "click" events with event_ts in (query_ts-30m, query_ts]
    #    - purchases_30m: count of "purchase" events in the same window
    #    - ctr_30m: clicks_30m / max(views_30m, 1) as float
    #
    # Input format:
    # - events: list[dict] where each dict has keys:
    #   ["event_id","user_id","event_ts","ingest_ts","event_type"]
    # - query_ts: int epoch seconds
    # - allowed_lateness_secs: int (e.g., 300 for 5 minutes)
    #
    # Output:
    # dict[str, dict[str, float|int]] keyed by user_id with metrics.
    #
    # Example:
    # events = [
    #   {"event_id":"e1","user_id":"u1","event_ts":1000,"ingest_ts":1010,"event_type":"view"},
    #   {"event_id":"e2","user_id":"u1","event_ts":1020,"ingest_ts":1030,"event_type":"click"},
    #   {"event_id":"e2","user_id":"u1","event_ts":1020,"ingest_ts":1040,"event_type":"click"},  # retry dup
    #   {"event_id":"e3","user_id":"u2","event_ts": 800,"ingest_ts":1100,"event_type":"view"},   # late event-time
    # ]
    # query_ts = 1200, allowed_lateness_secs = 300
    #
    # Function signature:
    # def rolling_user_metrics(self, events: list[dict], query_ts: int, allowed_lateness_secs: int) -> dict:
    #
    # Expected complexity (comment only):
    # Time: O(n) (single pass + hash maps)
    # Space: O(u + n_dedup) where u=users, n_dedup=unique event_ids retained

    def rolling_user_metrics(self, events: list[dict], query_ts: int, allowed_lateness_secs: int) -> dict:
        pass

    # ============================================================
    # 3) Spark Continuation (PySpark, no Spark code): Same rolling metrics at scale
    # ============================================================
    # You now have events in a PySpark DataFrame and need the same output at query_ts.
    #
    # Input schema (DataFrame events_df):
    # - event_id: string
    # - user_id: string
    # - event_ts: long   (epoch seconds)
    # - ingest_ts: long  (epoch seconds)
    # - event_type: string  ("view"|"click"|"purchase")
    #
    # Output schema (DataFrame metrics_df):
    # - user_id: string
    # - views_30m: long
    # - clicks_30m: long
    # - purchases_30m: long
    # - ctr_30m: double
    #
    # Required transformations (conceptual, no code):
    # 1) Dedup by event_id keeping row with MIN(ingest_ts) (stable tie-breaker if needed).
    # 2) Filter to rows with ingest_ts <= query_ts.
    # 3) Filter by event_ts window: (query_ts-30m, query_ts] for metrics,
    #    but optionally prefilter by (query_ts-30m-allowed_lateness, query_ts] to reduce scan.
    # 4) Conditional aggregations by user_id:
    #    SUM(CASE WHEN event_type='view' THEN 1 ELSE 0 END) as views_30m, etc.
    # 5) ctr_30m = clicks_30m / greatest(views_30m, 1) cast to double.
    #
    # Function signature:
    # def rolling_user_metrics_spark(self, events_df, query_ts: int, allowed_lateness_secs: int):
    #
    # Expected distributed complexity (comment only):
    # Time: O(N) scan + shuffle on (event_id) for dedup + shuffle on (user_id) for agg
    # Space: Shuffle + hash aggregate state; watch skew on hot user_id / event_id
    #
    # NOTE: Do NOT write Spark code.

    def rolling_user_metrics_spark(self, events_df, query_ts: int, allowed_lateness_secs: int):
        pass


if __name__ == "__main__":
    # Placeholder test harness (no real logic; just shape checks / placeholder calls)
    lc = Leetcode()

    # DSA placeholder
    print(lc.topKFrequent_buckets(nums=[1, 1, 1, 2, 2, 3], k=2))


    # DE placeholder
    events = [
        {"event_id": "e1", "user_id": "u1", "event_ts": 1000, "ingest_ts": 1010, "event_type": "view"},
        {"event_id": "e2", "user_id": "u1", "event_ts": 1020, "ingest_ts": 1030, "event_type": "click"},
    ]
    _ = lc.rolling_user_metrics(events=events, query_ts=1200, allowed_lateness_secs=300)

    # Spark placeholder (assume events_df exists in real run)
    events_df = None
    _ = lc.rolling_user_metrics_spark(events_df=events_df, query_ts=1200, allowed_lateness_secs=300)
