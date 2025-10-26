"""
Question:
design a rate-limiting component for Google's API Gateway.

Each incoming request contains - (user_id, endpoint, timestamp)

Requirements:
- Each user can make no more than K requests in any rolling N-second window.
- Different endpoints may have different limits (e.g., /search = 100 req/10 s, /upload = 10 req/60 s)

Example Rule:
/search: 100 requests per 10 seconds
/upload: 10 requests per 60 seconds

"""

from collections import deque, defaultdict
from typing import Dict, Tuple, Deque


class RateLimiter:
    """
    Sliding window rate limiter supporting per-endpoint limits.

    Time Complexity: O(1) amortized per request
    Space Complexity: O(U * E * K) where U=users, E=endpoints, K=threshold
    """

    def __init__(self, endpoint_configs: Dict[str, Tuple[int, int]]):
        """
        Initialize the rate limiter.

        Args:
            endpoint_configs: Dict mapping endpoint -> (threshold, window_seconds)
                            e.g., {'/search': (100, 10), '/upload': (10, 60)}
        """
        self.endpoint_configs = endpoint_configs
        # state[user_id][endpoint] -> deque of timestamps
        self.state: Dict[str, Dict[str, Deque[float]]] = defaultdict(lambda: defaultdict(deque))

    def on_event(self, user_id: str, endpoint: str, timestamp: float) -> bool:
        """
        Process an incoming request and determine if it should be allowed.

        Args:
            user_id: Unique identifier for the user
            endpoint: API endpoint being accessed
            timestamp: Unix timestamp of the request

        Returns:
            True if request is allowed, False if rate limit exceeded
        """
        # If endpoint has no rate limit configured, reject
        if endpoint not in self.endpoint_configs:
            return False

        threshold, window = self.endpoint_configs[endpoint]

        # Get the deque for this user-endpoint combination
        dq = self.state[user_id][endpoint]

        # Remove requests outside the current sliding window
        cutoff = timestamp - window
        while dq and dq[0] < cutoff:
            dq.popleft()

        # Check if adding this request would exceed the limit
        if len(dq) >= threshold:
            return False  # Rate limit exceeded

        # Add the current request timestamp
        dq.append(timestamp)
        return True  # Request allowed


# Example usage and tests
if __name__ == "__main__":
    # Initialize with endpoint configurations
    limiter = RateLimiter({
        '/search': (100, 10),   # 100 requests per 10 seconds
        '/upload': (10, 60)      # 10 requests per 60 seconds
    })

    print("Test 1: Basic rate limiting")
    # Make 3 requests within limit
    for i in range(3):
        result = limiter.on_event('user1', '/search', timestamp=i)
        print(f"Request {i+1}: {'ALLOWED' if result else 'REJECTED'}")

    print("\nTest 2: Exceeding limit")
    # Configure a stricter limit for testing
    test_limiter = RateLimiter({'/test': (3, 10)})

    # First 3 should pass
    for i in range(3):
        result = test_limiter.on_event('user1', '/test', timestamp=i)
        assert result == True, f"Request {i+1} should be allowed"

    # 4th should fail
    result = test_limiter.on_event('user1', '/test', timestamp=3)
    assert result == False, "Request 4 should be rejected"
    print("Request 4: REJECTED (as expected)")

    print("\nTest 3: Sliding window expiration")
    # Request at timestamp 11 (first request at 0 is now outside 10s window)
    result = test_limiter.on_event('user1', '/test', timestamp=11)
    assert result == True, "Request should be allowed after window slides"
    print("Request after window slide: ALLOWED")

    print("\nTest 4: Different users are independent")
    result1 = test_limiter.on_event('user2', '/test', timestamp=15)
    result2 = test_limiter.on_event('user2', '/test', timestamp=16)
    assert result1 == True and result2 == True
    print("Different user requests: ALLOWED")

    print("\nAll tests passed! ✓")
