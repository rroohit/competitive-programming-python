from typing import List


def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    prices = [float("inf")] * n
    prices[src] = 0

    for i in range(k + 1):
        tempPrice = prices.copy()

        for s, d, p in flights:
            if prices[s] == float("inf"):
                continue
            if prices[s] + p < tempPrice[d]:
                tempPrice[d] = prices[s] + p

        prices = tempPrice

    return -1 if prices[dst] == float("inf") else prices[dst]


nn = 4
flight_ = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
frm = 0
to = 3
kk = 1
print(findCheapestPrice(nn,flight_, frm, to, kk))
