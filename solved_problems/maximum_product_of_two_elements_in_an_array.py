from typing import List


# solved
def maxProduct(nums: List[int]) -> int:
    a = min(nums[0], nums[1])
    b = max(nums[0], nums[1])

    if len(nums) <= 2:
        return (a - 1) * (b - 1)

    for i in nums:
        if i > b:
            a = b
            b = i
        elif i > a:
            a = i

    return (a - 1) * (b - 1)


my_list = [2, 2, 3, 4, 5]
ans = maxProduct(my_list)
print(ans)
