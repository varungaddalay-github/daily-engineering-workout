"""
Problem Statement
Implement a rate limiter that restricts a given user to a maximum number of requests in a given time window.

Constraints:
- Single server (not distributed)
- Support multiple users independently
- Time window: configurable (e.g., 1 minute, 1 hour)
- Max requests: configurable (e.g., 100 requests per minute)


maxRequests: 3, window_seconds: 10

- We can use a queue to store the timestamps and check the conditions
- First condition, 
    - To add, This queue length is less than max_requests and the window_size is in between the window_start and curr_ts
- Second condition,
    - To remove, When there is timestamp outside the window_start which is curr_ts - window_seconds

- This is per user, in order to work with multiple users we need to do something like
    {u_1: [], u_2: [], ...} So basically initialzing default dict so we do not need to think about initializing

"""

from collections import defaultdict, deque
import time


class RateLimiter:
    def __init__(self, max_requests: int, window_seconds: int, time_func):
        """Initialize rate limiter"""
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.users = defaultdict(deque)
        self.time_func = time_func or time.time
        
    
    def allow_request(self, user_id: str) -> bool:
        """
        Returns True if request allowed, False if rate limited
        """
        curr_ts = self.time_func()

        window_start = curr_ts - self.window_seconds

        # 10 and window_start is 10
        while self.users[user_id] and self.users[user_id][0] < window_start:
            self.users[user_id].popleft()


        if len(self.users[user_id]) < self.max_requests:
            self.users[user_id].append(curr_ts)
            return True
        else:
            return False
        


    def basic_tests():
        fake_time = 0
        
        def mock_time():
            return fake_time
        
        rl = RateLimiter(max_requests=3, window_seconds=10, time_func=mock_time)    

        print(rl.allow_request("u1"))
        fake_time = 2
        print(rl.allow_request("u1"))
        
        fake_time = 5
        print(rl.allow_request("u2"))
        print(rl.allow_request("u2"))

        fake_time = 11
        print(rl.allow_request("u1"))
        print(rl.allow_request("u1"))



"""
Problem Statement:
- Implement a system that tracks caregiver availability and efficiently queries which caregivers are available at a given time.

Constraints:
- 10,000+ caregivers in the system
- Each caregiver can have multiple availability slots (e.g., "Mon 9-5", "Tue 2-8", "Wed 9-12")

Query: "Who is available on Monday at 3 PM?" must return in < 100ms

Support add, remove, and update operations
Handle overlapping time slots for same caregiver



tracker = AvailabilityTracker()

# Alice available Monday 9 AM - 5 PM
tracker.add_availability("alice", DayOfWeek.MONDAY, time(9, 0), time(17, 0))

# Bob available Monday 1 PM - 9 PM
tracker.add_availability("bob", DayOfWeek.MONDAY, time(13, 0), time(21, 0))

# Charlie available Tuesday 9 AM - 5 PM
tracker.add_availability("charlie", DayOfWeek.TUESDAY, time(9, 0), time(17, 0))

# Query: Who is available Monday at 3 PM?
available = tracker.find_available_caregivers(DayOfWeek.MONDAY, time(15, 0))


- Given their schedules, find the first available caregiver

- Sort the availaibility based on the time.
- return the first person in the sorted times


- add_availability(user_id, DayOfWeek, query_time)

{"alice": [MONDAY, [9, 17]], "bob": [MONDAY, [13, 21]]}


# Query: Who is available Monday at 3 PM?
- return first available person. on Monday and then at 3 PM -> 15:00

So, for each dayofWeek - create list of lists

{
MONDAY: 
    [
        [[9, 17], "alice"], 
        [[13, 21], "bob"]
    ],
TUESDAY: 
    [
        [[9, 17], "charlie"]
    ]  
}

- Now Sort all the lists for each day by the start_time 


"""        


from datetime import time
from enum import IntEnum
from sortedcontainers import SortedList

class DayOfWeek(IntEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

class AvailabilityTracker:
    def __init__(self):
        """Initialize tracker"""
        self.schedule = {
            day: SortedList(key=lambda x: x[0]) for day in DayOfWeek
        }

    def time_to_minutes(self, t: time):
        return t.hour * 60 + t.minute
    
    def add_availability(self, caregiver_id: str, day: DayOfWeek, 
                        start_time: time, end_time: time) -> None:
        """Add availability slot for caregiver"""
        start_min = self.time_to_minutes(start_time)
        end_min = self.time_to_minutes(end_time)

        if end_min <= start_min:
            raise ValueError("end_time must be after start_time")
        
        self.schedule[day].add((start_min, end_min, caregiver_id))

    
    def find_available_caregivers(self, day: DayOfWeek, query_time: time) -> set:
        """Return set of caregiver IDs available at given day/time"""
        pass
    
    def remove_availability(self, caregiver_id: str, day: DayOfWeek, 
                           start_time: time) -> None:
        """Remove specific availability slot"""
        pass

"""
Find the first available caregiver in a list of busy schedule

- For each person, we have a list of busy schedules
    1. Sort the list of busy schedules.
    2. Merge any overlapping schedules
    3. iterate through the list of overlapping schedule to see their FIRST available gap >= duration
    4. store
- Compare all first gaps
- Return the earliest one


Given Schedules are busyslots. Other variant is non busy slots

Variant - Duration:
- Iterate for each person
    - Sort the time slots for each person
        sorted(input, key= lambda x: x[0])
    - merge any continuous (start, end) or overlapping intervals 
        - res = []. Iterate through the intervals. At each interval compare with the res[-1] and then append (start, max(end_times))
    - Now for each date, - filter for each date - curr_date = date_time.date()
        - For each curr_date,
            - find the slots where the difference between the end and start of contiguous slots is equal to the duration
        - 

Variant - Specific time:
- Iterate for each person
    - Sort the time slots for each person
        sorted(input, key= lambda x: x[0])
    - merge any continuous (start, end) or overlapping intervals 
        - res = []. Iterate through the intervals. At each interval compare with the res[-1][1] and then append (start, max(end_times))
    - Now for each date, - filter for each date - curr_date = date_time.date()
        - For each curr_date,
            - find the slots where the start time is > than the previous end time. Similarly, the end time is less than the next start time
        -         


- Implement the above - Not very confident on working with datetimes in python

- multiple users, multiple days

"""




"""
- allow_request(u1)
- allow_request(u1)
- time.sleep(5)
- allow_request(u2)


- Create a map of user_id with list of timestamps


allow request:
{

}


1. If the user is new. Append to a map
- Make sure, your window is valid. map(user_id: queue). pop from beginning. - while loop - O()
2. If len(timestamps for that user) < max_requests, then append the new timestamp
3. Else, return false

How are you going to make sure it is 10 sec window


"""
    
    