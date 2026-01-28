from collections import defaultdict
import heapq
import random

class Leetcode:
    """
    Batch: 2 DSA + 2 Data Engineering + 1 System Design + 1 Terraform
    No DP. No solutions. Placeholders only.
    """

    # ---------------------------------------------------------
    # 2️⃣ DE: Error Rate per Endpoint
    # ---------------------------------------------------------
    """
    Problem (Data Engineering flavored):
    You are given HTTP request logs as tuples:
      (endpoint: str, status_code: int)

    Compute, for each endpoint, the error rate defined as:
      error_rate = error_count / total_count
    where an "error" is any status_code >= 400.

    Return a dictionary mapping endpoint → error_rate (float between 0 and 1).

    Example:
    logs = [
      ("/api/users", 200),
      ("/api/users", 500),
      ("/api/users", 404),
      ("/api/orders", 200),
      ("/api/orders", 201),
      ("/api/orders", 503),
    ]

    For "/api/users":
      total = 3, errors = 2 → 2/3 ≈ 0.6666

    For "/api/orders":
      total = 3, errors = 1 → 1/3 ≈ 0.3333

    Output (order not important):
    {
      "/api/users": 0.6666...,
      "/api/orders": 0.3333...
    }

    Assume logs can be very large (millions of rows).
    """
    def error_rate_per_endpoint(self, logs: list[tuple[str, int]]) -> dict[str, float]:
        # Expected Time: O(n)
        # Expected Space: O(m) where m is number of distinct endpoints
        temp = defaultdict(list)
        res = {}

        for log in logs:
            end_point = log[0]
            status_code = log[1]            
            temp[end_point].append(status_code)
        
        for k, v in temp.items():
            error_rate = len([x for x in v if x>= 400])/len(v)
            res[k] = error_rate

        return res
    
    def error_rate_per_endpoint_optimal_storage(self, logs: list[tuple[str, int]]) -> dict[str, float]:
        # Expected Time: O(n)
        # Expected Space: O(m) where m is number of distinct endpoints
        
        # Above solution will run into issues if > 10M requests.  Store counts instead and not values. 
        temp = defaultdict(lambda: {'total': 0, 'errors': 0})        
        res = {}

        for endpoint, status_code in logs:
            temp[endpoint]['total'] += 1
            if status_code >= 400:
                temp[endpoint]['errors'] += 1
        
        for k, v in temp.items():
            error_rate = v['errors']/v['total']
            res[k] = error_rate

        return res    


    # ---------------------------------------------------------
    # 3️⃣ DSA: Kth Largest Element in an Array
    # ---------------------------------------------------------
    """
    Problem:
    Given an integer array nums and an integer k, return the k-th largest
    element in the array.

    Note:
      - It is the k-th largest element in sorted order, not distinct order.
      - You must solve it in better than O(n log n) time on average
        (i.e., think heap or Quickselect).

    Example 1:
    nums = [3,2,1,5,6,4], k = 2 → 5

    Example 2:
    nums = [3,2,3,1,2,4,5,5,6], k = 4 → 4

    Constraints:
      - 1 <= k <= len(nums)
    """
    def find_kth_largest_heap(self, nums: list[int], k: int) -> int:
        # Expected Time: O(n) average with Quickselect or O(n log k) with heap
        # Expected Space: O(1) for Quickselect or O(k) for heap
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)        
        return min_heap[0]
    
    def find_kth_largest_quick_select(self, nums):
        target = len(nums) - k
        def quickselect(l, r):
            pivot_idx = random.randint(l, r)
            nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]

            



    # ---------------------------------------------------------
    # 4️⃣ DE: Daily Revenue per Country
    # ---------------------------------------------------------
    """
    Problem (Data Engineering flavored):
    You are given purchase events as tuples:
      (user_id: str, country: str, timestamp: str, amount: float)

    - timestamp is an ISO-like string: "YYYY-MM-DDTHH:MM:SSZ".
    - amount is the purchase amount in USD.

    Compute the total daily revenue per country.
    Return a dictionary mapping:
      (date_string: "YYYY-MM-DD", country) → total_revenue (float)

    Example:
    events = [
      ("u1", "US", "2025-11-21T10:00:00Z", 10.0),
      ("u2", "IN", "2025-11-21T12:00:00Z", 5.5),
      ("u3", "US", "2025-11-21T18:30:00Z", 20.0),
      ("u1", "US", "2025-11-22T09:00:00Z", 7.0),
    ]

    Output:
    {
      ("2025-11-21","US"): 30.0,
      ("2025-11-21","IN"): 5.5,
      ("2025-11-22","US"): 7.0
    }

    Assume input can be large; design for a single-machine solution here.
    """
    def daily_revenue_per_country(
        self,
        events: list[tuple[str, str, str, float]]
    ) -> dict[tuple[str, str], float]:
        # Expected Time: O(n)
        # Expected Space: O(d * c) where d=#days, c=#countries
        pass


    # ---------------------------------------------------------
    # 5️⃣ System Design: Notification Service (Email / Push)
    # ---------------------------------------------------------
    """
    SYSTEM DESIGN PROBLEM (no coding required, placeholder only):

    Problem:
    Design a scalable notification service that can send:
      - transactional emails (password reset, receipts)
      - marketing emails
      - push notifications (mobile/web)

    Requirements:
      - APIs:
          - send_notification(user_id, type, payload)
      - Supports templates and localization (per language).
      - Must avoid over-notifying users (per-user rate limits, quiet hours).
      - Must integrate with multiple providers (e.g., SES, SendGrid, FCM, APNs).
      - Handles retries, dead-lettering, and failure monitoring.
      - Should be able to scale to millions of notifications per hour.

    Discussion points:
      - High-level architecture (producer → queue → worker → provider).
      - How to model notification templates and preferences.
      - Choosing between synchronous vs asynchronous flows.
      - Idempotency and deduplication (avoid duplicate sends).
      - Data model for user preferences and opt-outs.
      - Monitoring: success rate, latency, bounce rate, spam complaints.
      - Handling provider failures and failover strategies.

    No implementation required; this is for design discussion.
    """
    def design_notification_service(self):
        # Time Complexity: N/A (system design)
        # Space Complexity: N/A (system design)
        pass


    # ---------------------------------------------------------
    # 6️⃣ Terraform: Create an S3 Bucket with Versioning and Lifecycle
    # ---------------------------------------------------------
    """
    TERRAFORM IMPLEMENTATION QUESTION (no Python code required):

    Problem:
    Write Terraform configuration to create an AWS S3 bucket with the following:
      - Bucket name should be based on:
          - a required variable "project"
          - a required variable "env" (e.g., "dev", "staging", "prod")
        Example pattern: "<project>-<env>-data-bucket"
      - Enable versioning on the bucket.
      - Enable default server-side encryption with AWS-managed keys (SSE-S3).
      - Add tags:
          - "Project" = var.project
          - "Environment" = var.env
      - Add a lifecycle rule:
          - Transition objects to STANDARD_IA after 30 days.
          - Transition objects to GLACIER after 90 days.
      - Block public access at the bucket level.

    Requirements:
      - Use variables for project and env.
      - Use outputs to expose:
          - bucket_name
          - bucket_arn
      - Use a main.tf, variables.tf, and outputs.tf layout (you don’t have to
        write separate files here, but structure your Terraform code logically).

    Your task:
      - Write the HCL Terraform configuration (in your editor) that satisfies
        the above requirements.
      - You do NOT need to provide it here unless you want a review later.

    This Python placeholder exists only so this Terraform task stays coupled
    with your daily coding practice.
    """
    def terraform_s3_versioned_lifecycle_bucket(self):
        # Time Complexity: N/A (Terraform configuration)
        # Space Complexity: N/A (Terraform configuration)
        pass



# -------------------------------------------------------------
# Test Harness (for your implementations where applicable)
# -------------------------------------------------------------
if __name__ == "__main__":
    lc = Leetcode()

    # # 1️⃣ Binary Tree Right Side View
    # print("1: right_side_view →", lc.right_side_view(None))  # build a real tree when testing

    # # 2️⃣ Error Rate per Endpoint
    # logs_example = [
    #     ("/api/users", 200),
    #     ("/api/users", 500),
    #     ("/api/users", 404),
    #     ("/api/orders", 200),
    #     ("/api/orders", 201),
    #     ("/api/orders", 503),
    # ]
    # print("2: error_rate_per_endpoint →",
    #       lc.error_rate_per_endpoint_optimal_storage(logs_example))

    # 3️⃣ Kth Largest Element
    print("3: find_kth_largest →",
          lc.find_kth_largest_heap([3,2,1,5,6,4], 2))

    # # 4️⃣ Daily Revenue per Country
    # events_example = [
    #     ("u1", "US", "2025-11-21T10:00:00Z", 10.0),
    #     ("u2", "IN", "2025-11-21T12:00:00Z", 5.5),
    #     ("u3", "US", "2025-11-21T18:30:00Z", 20.0),
    #     ("u1", "US", "2025-11-22T09:00:00Z", 7.0),
    # ]
    # print("4: daily_revenue_per_country →",
    #       lc.daily_revenue_per_country(events_example))

    # # 5️⃣ System design placeholder
    # print("5: design_notification_service →",
    #       lc.design_notification_service())

    # # 6️⃣ Terraform placeholder
    # print("6: terraform_s3_versioned_lifecycle_bucket →",
    #       lc.terraform_s3_versioned_lifecycle_bucket())
