"""
Implement Rate Limiter Class
- Write working code
- Test Edge cases

Rate Limiter:

- This is a controlled way to pass the request without overloading the downstream
- The data can come from EMR's, Third party API's

- Let's say, we set the number of requests - 10 req/sec

- User - Should be limited to 10 req/sec

How? 

Are we doung this on the client side or the server side>

The problem with the client side, the user can manipulate the number of requests
Doing it on the server side gives us more control. Let's say if we have deployed a new feature and do not want to overload the system

- How? So, if i am implementing a rate limiter class, I need to make sure, we are allowing the request only if it obeys the condition - i.e. 
    max_requests = 3, window = 10 secs


     ...         ..
    |----------||----------|
    1          10          20


    - We are basically using a queue to implement this. 
    - So, as soon as we get the requests we add it to a queue.
    - Need to make sure, 2 things,
        1. The len(queue) == Max_Num_Requests 
        2. Inside the Window - Always check if curr_ts > window_start and curr_ts < window_end --> curr_ts (11) - total_window (10) >= window_start
            - So, i need to keep on updating my window start?
        3. Reset the max request as soon as the window is done

    - (curr_ts - 10, curr_ts] (left exlusive)
            
"""
from collections import defaultdict, deque

# Sliding window log
class RateLimiter:
    def __init__(self, max_requests, window):
        self.max_requests = max_requests
        self.window = window
        self.list = deque()

    def allow(self, curr_ts) -> bool:
        # reject Out of Order events
        if self.list and curr_ts < self.list[-1]:
            return False
            
        while self.list and curr_ts - self.window >= self.list[0]:
            self.list.popleft()
                
        if len(self.list) < self.max_requests:
            self.list.append(curr_ts)            
            return True
        else:
            return False

# Sliding window log + Threads
import threading

class ThreadSafeRateLimiter:
    def __init__(self, max_requests, window):
        self.max_requests = max_requests
        self.window = window
        self.list = deque()
        self.lock = threading.Lock()

    def allow(self, curr_ts) -> bool:
        with self.lock:
            # reject Out of Order events
            if self.list and curr_ts < self.list[-1]:
                return False
            
            window_start = curr_ts - self.window 

            while self.list and self.list[0] <= window_start:
                self.list.popleft()
                    
            if len(self.list) < self.max_requests:
                self.list.append(curr_ts)            
                return True
            else:
                return False

# Sliding window log + Threads + shards

class ShardedSafeRateLimiter:
    def __init__(self, max_requests, window, num_shards):
        self.max_requests = max_requests
        self.window = window
        self.num_shards = num_shards

        self.shards = [
            {
                'lock': threading.Lock(),
                'limiters': defaultdict(lambda: deque())
            }
            for _ in range(num_shards)
        ]

    def _get_shard(self, user_id):
        shard_idx = hash(user_id) % self.num_shards
        return self.shards[shard_idx]

    def allow(self, user_id, curr_ts) -> bool:
        shard = self._get_shard(user_id)

        with shard['lock']:
            timestamps = shard['limiters'][user_id]

            # reject Out of Order events
            if timestamps and curr_ts < timestamps[-1]:
                return False
            
            window_start = curr_ts - self.window 

            while timestamps and timestamps[0] <= window_start:
                timestamps.popleft()
                    
            if len(timestamps) < self.max_requests:
                timestamps.append(curr_ts)            
                return True
            else:
                return False


if __name__ == "__main__":
    rl = RateLimiter(max_requests=3, window=10)
    print(rl.allow(1))
    print(rl.allow(1))
    print(rl.allow(2))
    print(rl.allow(3))
    print(rl.allow(11))
    print(rl.allow(8)) # late arriving
    print(rl.allow(13))
    print(rl.allow(3)) # late arriving 

        