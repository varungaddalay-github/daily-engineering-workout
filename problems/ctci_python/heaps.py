

"""
nums = [3, 2, 1, 5, 6, 4], k = 2

return kth largest element in the array

- We can use a heap to store the elements of the array. 
- Since Python only supports min heap in order to keep track of large elements. We can pop the element on the top of the heap directly to keep track of larger elements only.
- This way, when we are done iterating through the array nums we will only have the top k large elements. Return the mentioned kth element
- Condition: We pop the element when the len(heap) > k
- So that, at the end of the iteration we only have k elements in the heap

heap [3, 2, 1, 5, 6, 4]

heap - 5, 6

"""
import heapq

def findKthLargest(nums, k):
    heap = []
    for i in range(len(nums)):
        heapq.heappush(heap, nums[i])

        if len(heap) > k:
            heapq.heappop(heap)
    
    return heap[0]

"""
lists = [[1,4,5], [1,3,4], [2,6]]

Merge K lists into one asc list

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedLists:
    def mergeKlists(self, lists):
        heap = []
        for node in lists:
            if node:
                


