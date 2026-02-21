"""
Implement Rate Limiter for each user_id

RateLimiter limiter = new RateLimiter(maxRequests=5, windowSize=60) // 5 requests per 60 seconds

limiter.allowRequest("user_123") → true  (1st request)
limiter.allowRequest("user_123") → true  (2nd request)
...
limiter.allowRequest("user_123") → true  (5th request)
limiter.allowRequest("user_123") → false (6th request, rate limited)

// After 60 seconds
limiter.allowRequest("user_123") → true  (window reset)

"""

from collections import defaultdict, deque
import time

class RateLimiter:
    def __init__(self, maxRequests, windowSize):
        self.maxRequests = maxRequests
        self.windowSize = windowSize
        self.users = defaultdict(deque)

    def allowRequest(self, u_id):
        # Get the curr timestamp
        curr_ts = time.time()        

        window = curr_ts - self.windowSize

        # compare curr_ts - windowSize with the top of the queue and is false. 70 - 60, If the top is 6

        while self.users[u_id] and self.users[u_id][0] <= window:
            self.users[u_id].popleft()

        # Append the curr_ts to the queue if the len(queue) < maxRequests and compare curr_ts - windowSize with the top of the queue
        if len(self.users[u_id]) < self.maxRequests:
            self.users[u_id].append(curr_ts)
            return True
        else:
            return False


class TokenBucketRateLimiter:
    def __init__(self, capacity, refill_rate):
        self.capacity = capacity
        self.tokens = capacity
        self.refill_rate = refill_rate
        self.last_refill = time.time()

    def allow_request(self):
        curr_ts = time.time()
        elapsed = curr_ts - self.last_refill
        tokens_to_add = elapsed * self.refill_rate # 10 * 2

        self.tokens = min(self.capacity, self.tokens + tokens_to_add)
        self.last_refill = curr_ts

        if self.tokens >= 1:
            self.tokens -= 1
            return True
        return False
    




        


def test_rate_limiter():
    rl = RateLimiter(maxRequests=3, windowSize=10)
    print(rl.allowRequest("user_123"))
    print(rl.allowRequest("user_123"))
    time.sleep(5)
    print(rl.allowRequest("user_124"))
    time.sleep(3)
    print(rl.allowRequest("user_124"))
    time.sleep(3)
    print(rl.allowRequest("user_124"))
    time.sleep(3)
    print(rl.allowRequest("user_124"))
    time.sleep(3)
    print(rl.allowRequest("user_124"))
    time.sleep(5)
    print(rl.allowRequest("user_123"))
    


        
