from typing import List

mod = 10 ** 9 + 7


def solve(A: List[int], P: List[int]) -> int:
    n = len(A)
    sum_of_gcd = 0
    for i in range(n):
        a = A[i]
        b = A[P[i] - 1]
        while b:
            a, b = b, a % b
        sum_of_gcd += a
    return sum_of_gcd % mod


aa = [10, 6, 15]
pp = [3, 1, 2]
print(solve(aa, pp))
