from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    total = 0
    for n in nums:
        total += n
    return total

# list = [1, 6, 4, 0]
# for the number in [1, 6, 4, 0]
# if that number is less than the value of the first index 
# cur_min starts at first index nums[0]
# then current minimum is n 
def get_min(nums: List[int]) -> int:
    cur_min = nums[0]
    for n in nums:
        if n < cur_min:
            cur_min = n
    return cur_min


def get_max(nums: List[int]) -> int:
    cur_max = nums[0]
    for n in nums:
        if n > cur_max:
            cur_max = n
    return cur_max

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
