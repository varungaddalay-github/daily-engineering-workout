"""
build a part of a fraud-detection service used by Google Ads to identify potentially fraudulent spending activity.

Every event in the input stream contains:
(user_id, timestamp, amount)

These events arrive roughly in chronological order, though occasionally they may be slightly delayed.

Your task is to design a function or class that can ingest a continuous stream of transactions 
and efficiently determine whether a user’s total spending within the past N minutes exceeds a given threshold.

"""

"""
Skeleton - Rolling window of size N minutes function per user:

- Insert a record into the data structure
- Discard the record which is > than the given N minutes 
- Calculate the sum of the records in the data structure. If greater than the threshold return Rejection

Required O(1) Operations - Assuming the records are in order 

- The best data structure to insert a record and discard an old record from the beginning would be a Deque()
- The key note to discard a record from the beginning is to maintain the records in ascending order based on timestamp

Extension if records not in order,
- To achieve this, we need something like a Heap operation which maintains the min or max element at the top

So, we can achieve detecting fraud in a window per user by 
1. Creating a Deuqe()

3. Now, Push the elements on to a Deque()
4. Create a total_sum variable and add the total amount
5. If the front of the Deque() does not satisfy the N minutes window. subtract from total_amount and pop the element from the beginning

-- Extension if records not in order, 
2. Create a heap Insert an element into heap to handle the delayed records or old records


- This is repeated for each User.
- So, create a class to maintain this (deque, total_sum) for each user
- Create a dictionary for each user for O(1) lookup. Something like defaultdict(User)

"""


"""
Skeleton for Duplicate records 


"""


from collections import deque, defaultdict

class User:
    def __init__(self):        
        self.q = deque()
        self.total_sum = 0


class FraudDetection:
    def __init__(self, window_size, threshold):
        self.window = window_size
        self.threshold = threshold
        self.user_state = defaultdict(User)

    def event(self, user_id, timestamp, amount):
        user = self.user_state[user_id]
        dq = user.q

        cutoff = timestamp - self.window

        # Check if the beginning of the window is still inside the window
        while dq and dq[0][0] < cutoff:
            old_ts, old_amount = dq.popleft()
            user.total_sum -= old_amount
            
        # New transaction
        user.total_sum += amount
        dq.append((timestamp, amount))

        # Check Threshold
        if user.total_sum > self.threshold:
            return f"Fraud Detected for user {user_id}"
            
            


        

        
