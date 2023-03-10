from collections import defaultdict
import random
from typing import List

class Solution:
    def __init__(self, nums: List[int]):
        self.result = defaultdict(list)
        for i, num in enumerate(nums):
            self.result[num].append(i)

    def pick(self, target: int) -> int:
        indices = self.result[target]
        return random.choice(indices)


n = [1, 2, 3, 3, 3]
obj = Solution(n)
print(obj.pick(1))
print()
print(obj.pick(3))
print(obj.pick(3))
