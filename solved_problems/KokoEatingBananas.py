import math
from typing import List


# Solved using binary search
def minEatingSpeed(piles: List[int], h: int) -> int:
    l = 1
    r = 0
    for i in piles:
        r = max(i, r)

    ans = r
    while l <= r:
        mid = (l + r) // 2
        totalHour = 0
        for b in piles:
            totalHour += math.ceil(b / mid)

        if totalHour <= h:
            ans = min(ans, mid)
            r = mid - 1
        else:
            l = mid + 1

    return ans


pilesOfBanana = [3, 6, 7, 11]
hh = 8
print("ans", minEatingSpeed(pilesOfBanana, hh))
