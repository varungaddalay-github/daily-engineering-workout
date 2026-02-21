def combine(nums, k, start):
    if k == 0:
        return [[]]
    if start == len(nums):
        return []

    res = []

    for combo in combine(nums, k-1, start+1):
        res.append([nums[start]] + combo)

    res.extend(combine(nums, k, start+1))

    return res


def combine(nums, k, start):
    if k == 0:
        return [[]]
    if start == len(nums):
        return []
    
    res = []

    for combo in combine(nums, k - 1, start + 1):
        res.append([nums[start]] + combo)

    res.extend(combine(nums, k, start + 1))

    return res


def combine(nums, k, start):
    res = []

    for combo in combine(nums, k - 1, start + 1):
        res.append([nums[start]] + combo)

    res.extend(combine(nums, k, start + 1))

    return res

print(combine([1,2,3], k=2, start=0))


"""
Given a list of distinct integers nums and an integer k, 
return all combinations of size k.

nums = [1, 2, 3, 4], k = 2
        
[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]


"""










