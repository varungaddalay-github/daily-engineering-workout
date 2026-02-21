"""
Rate Limiter: Limit the system to only allow given max_num_requests and the window size

So, given window size of 10 we can only pass around 3 requests

For example, 
1s - request - True - count_requests -- 1
2s - request - True - count_requests -- 2
3s - request - True - count_requests -- 3
4s 
5s - request - False why? 5 - 10 is -5. The window is -5 to 5 - There are already 3 requests
6s
7s
8s
9s
10s - request - False - why? 10 - 10 is 0. So in the window we already have 3 requests
11s - 

So, let's maintain a queue and then keep on tracking the last 10 seconds. if the queue size increases then we popleft from the queue

So based on the above,
- Allow Requests 
    - if len(queue) < maxRequests. Then, append to the queue
    - If not, then return False
    - Checking if the curr_ts - window_size is valid. 

For each user_id, 
- a list/ queue     

"""

from collections import defaultdict, deque
import time

class RateLimiter:
    def __init__(self, maxRequests, window_size):
        self.maxRequests = maxRequests
        self.window_size = window_size
        self.requests = defaultdict(deque)

    def allow_request(self, user_id):        
        curr_ts = time.time()

        window_start = curr_ts - self.window_size

        while self.requests[user_id] and self.requests[user_id][0] < window_start:
            self.requests[user_id].popleft
        
        if len(self.requests[user_id]) < self.maxRequests:
            self.requests[user_id].append(curr_ts)
            return True
        else:
            return False


import threading

class ThreadSafeRateLimiter:
    def __init__(self, maxRequests, window_size):
        self.maxRequests = maxRequests
        self.window_size = window_size
        self.requests = defaultdict(deque)
        self.lock = threading.Lock()

    def allow_request(self, user_id):  
        with self.lock:      
            curr_ts = time.time()

            window_start = curr_ts - self.window_size

            while self.requests[user_id] and self.requests[user_id][0] < window_start:
                self.requests[user_id].popleft()
            
            if len(self.requests[user_id]) < self.maxRequests:
                self.requests[user_id].append(curr_ts)
                return True
            else:
                return False    

from concurrent.futures import ThreadPoolExecutor

class ProductionAPIGateway:
    def __init__(self):
        self.rate_limiter = ThreadSafeRateLimiter(
            maxRequests=1000,
            window_size=60
        )
        self.executor = ThreadPoolExecutor(max_workers=50)

    def handle_api_request(self, user_id):
        result = self.rate_limiter.allow_request(user_id)

        # if not result.allowed:
        #     return Response(status=429, body={
        #         "error": "Rate limit exceeded",
        #         "retry_after": self.rate_limiter.window_seconds
        #     })

    def start(self):
        while True:
            request = get_next_request()

            self.executor.submit(self.handle_api_request, request)

"""
Token Algorithm Implementation

- Use a Token bucket of tokens capacity equal to the max requests
- And then we will have a refill rate where we add tokens per second. This is calculated using max_requests// num_seconds
- And for every second we keep on adding the refill rate into the bucket

For each user, we are creating a bucket

So, basically there is a global capacity

- last refill

"""        
from collections import defaultdict

from dataclasses import dataclass

from typing import Dict

@dataclass
class TokenBucket:
    """
    Token bucket for one user
    
    Attributes:
        capacity: Current number of tokens available
        last_refill: Timestamp of last refill
    """
    capacity: float
    last_refill: float


class TokenBucketRateLimiter:
    def __init__(self, maxNumRequests, window_size):
        self.maxNumRequests = maxNumRequests
        self.window_size = window_size
        self.refill_rate = maxNumRequests // window_size
        self.buckets: Dict[str, TokenBucket] = {}

    def allow_requests(self, user_id):
        curr_ts = time.time()

        if user_id not in self.buckets:
            self.buckets[user_id] = TokenBucket(
                capacity=self.maxNumRequests,
                last_refill=curr_ts
            )
        

from concurrent.futures import ThreadPoolExecutor
from collections import defaultdict, deque
import threading
import time

class SingleServerRateLimiter:
    """
    Rate limiter for ONE server
    Uses ThreadPoolExecutor for concurrent request handling
    """
    def __init__(self, max_requests, window_seconds):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = defaultdict(deque)
        self.lock = threading.Lock()
    
    def allow_request(self, user_id):
        with self.lock:
            current_time = time.time()
            window_start = current_time - self.window_seconds
            
            timestamps = self.requests[user_id]
            while timestamps and timestamps[0] < window_start:
                timestamps.popleft()
            
            if len(timestamps) < self.max_requests:
                timestamps.append(current_time)
                return True
            return False

# Single server handling requests
limiter = SingleServerRateLimiter(max_requests=100, window_seconds=60)

def handle_request(request):
    """Process one request"""
    user_id = request['user_id']
    
    # Check rate limit
    if not limiter.allow_request(user_id):
        return {"status": 429, "message": "Rate limited"}
    
    # Process request
    return {"status": 200, "data": "Success"}

# Use ThreadPoolExecutor to handle concurrent requests ON THIS SERVER
with ThreadPoolExecutor(max_workers=20) as executor:
    # 20 threads on THIS server process requests concurrently
    requests = [{"user_id": f"user_{i}"} for i in range(1000)]
    
    futures = [executor.submit(handle_request, req) for req in requests]
    results = [f.result() for f in futures]

print(f"Processed {len(results)} requests on single server")





