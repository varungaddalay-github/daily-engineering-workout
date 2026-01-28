"""
design a component inside Google Dataflow that continuously aggregates metrics from a high-throughput stream of sensor data.

Each event contains:

(sensor_id, timestamp, value)

Expected:

1. The moving average of value for each sensor over the last N seconds.
2. The minimum and maximum values in that same rolling window.

"""


"""
1. Let's Calculate moving average of value for each sensor over the last N seconds

Average = Total_sum of the rolling window / len(rolling window)

Each rolling window is of N seconds

Skeleton:
- Insert an event into a data structure for each sensor
- Discard an event from the data structure if any events are > N seconds from the new event
- Calculate the average of the values which is Average = Total_sum of the rolling window / len(rolling window)
"""

"""
Now for the implementation, from the skeleton we have the following, Also, Ask clarifying questions if the events are ordered **. If events are not orderderd, we need to implement different data structures in addition to this.

- We can use a deque to insert at the end and discard from the beginning in O(1)
- Everytime, we insert the element, we need to keep a track of the total sum as well as the length of the deque

"""


"""
2. Now let's calculate The minimum and maximum values in that same rolling window.

Skeleton:
- Keep track of the max value and min value in the window for the sensor
- The main problem is, if the max value is not in the N window. Then we need to keep track of the second max, min value again 
- Or after the event function, we can create a heap for the deque() and find the max and min in O(logN). 
- Thinking of implementing in O(1) - How to store the second max element always? I think heap is the only best option

"""


from collections import defaultdict, deque
import heapq

class Sensor:
    def __init__(self):
        self.dq = deque()
        self.total_sum = 0
        self.max_deque = deque()
        self.min_deque = deque()

class Aggregator:
    def __init__(self, window):
        self.state = defaultdict(Sensor)
        self.window = window

    def on_event(self, sensor_id, timestamp, value):
        sensor = self.state[sensor_id]
        dq = sensor.dq

        cutoff = timestamp - self.window

        removed_count = 0

        while dq and dq[0][0] < cutoff:
            ts, val = dq.popleft()
            sensor.total_sum -= val
            removed_count += 1            

        while sensor.min_deque and sensor.min_deque[0] < removed_count:
            sensor.min_deque.popleft()

        while sensor.max_deque and sensor.max_deque[0] < removed_count:
            sensor.max_deque.popleft()

        # Shift remaining indices down
        if removed_count > 0:
            sensor.min_deque = deque(idx - removed_count for idx in sensor.min_deque)
            sensor.max_deque = deque(idx - removed_count for idx in sensor.max_deque)

        
        dq.append((timestamp, value))
        sensor.total_sum += value

        new_idx = len(dq) - 1

        while sensor.min_deque:
            back_idx = sensor.min_deque[-1]
            back_val = dq[back_idx][1]
            if back_val >= value:
                sensor.min_deque.pop()
            else:
                break
        sensor.min_deque.append(new_idx)


        while sensor.max_deque:
            back_idx = sensor.max_deque[-1]
            back_val = dq[back_idx][1]
            if back_val <= value:
                sensor.max_deque.pop()
            else:
                break
        sensor.max_deque.append(new_idx)        

        return round((sensor.total_sum/ len(dq)), 2)
    

    def max_min_in_window(self, sensor_id):
        sensor = self.state[sensor_id]
        
        if not sensor.dq:
            return (None, None)
        
        min_idx = sensor.min_deque[0]
        max_idx = sensor.max_deque[0]

        min_val = sensor.dq[min_idx][1]
        max_val = sensor.dq[max_idx][1]

        return (min_val, max_val)


