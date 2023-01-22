mod = 1000000007


def partition(N, C, A):
    dp = [0] * (N + 1)
    dp[0] = 1
    for i in range(1, N + 1):
        dp[i] = 0
        freq = {}
        distinct = 0
        for j in range(i - 1, -1, -1):
            if A[j] not in freq:
                freq[A[j]] = 1
                distinct += 1
            else:
                freq[A[j]] += 1
            if distinct == C:
                dp[i] = (dp[i] + dp[j]) % mod
    return dp[N]


nn = 9
cc = 3
aa = [1, 2, 3, 1, 2, 3, 1, 2, 3]
print(partition(nn, cc, aa))
