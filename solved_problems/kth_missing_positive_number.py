from typing import List


# Solved
def findKthPositive(arr: List[int], k: int) -> int:
    l = 0

    for i in range(0, len(arr) + k):
        if l < len(arr) and arr[l] == i + 1:
            l += 1
        else:
            k -= 1

        if k == 0:
            return i + 1


arr_ = [1, 2, 3, 4, 5, 6, 7]
k_ = 4
print("ans", findKthPositive(arr_, k_))
