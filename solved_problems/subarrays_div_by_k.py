from typing import List


def subarraysDivByK(nums: List[int], k: int) -> int:
    ans = 0
    has_map = {0: 1}

    globTotal = 0

    for i in range(len(nums)):
        globTotal += nums[i]

        reminder = globTotal % k

        if reminder < 0:
            reminder += k

        if reminder in has_map:
            ans += has_map[reminder]

        has_map[reminder] = has_map.get(reminder, 0) + 1

    return ans


nums = [4, 5, 0, -2, -3, 1]
k = 5
print(subarraysDivByK(nums, k))
