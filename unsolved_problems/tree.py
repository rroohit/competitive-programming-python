def solve(N, Q, edges, query):
    minVal = [float('inf')] * (N + 1)
    maxVal = [0] * (N + 1)
    parent = [0] * (N + 1)
    depth = [0] * (N + 1)
    ans = 0

    def dfs(u, p):
        parent[u] = p
        depth[u] = depth[p] + 1
        for v in edges[u]:
            if v != p:
                dfs(v, u)

    def lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        while depth[u] > depth[v]:
            u = parent[u]
        if u == v:
            return u
        while parent[u] != parent[v]:
            u = parent[u]
            v = parent[v]
        return parent[u]

    def updatePath(u, v, w):
        x = lca(u, v)
        minVal[x] = min(minVal[x], w)
        while u != x:
            minVal[u] = min(minVal[u], w)
            u = parent[u]
        while v != x:
            minVal[v] = min(minVal[v], w)
            v = parent[v]
        u = v
        while u != x:
            maxVal[u] = max(maxVal[u], w - minVal[u])
            for v in edges[u]:
                if v != parent[u]:
                    maxVal[u] = max(maxVal[u], maxVal[v])
            u = parent[u]

    def quer(u, v):
        ans = 0
        while u != v:
            if depth[u] < depth[v]:
                u, v = v, u
            ans = max(ans, maxVal[u])
            u = parent[u]
        return ans

    dfs(1, 0)
    for i in range(Q):
        x, y, u, v, w = query[i]
        updatePath(u, v, w)
        ans ^= quer(x, y)
    return ans



nn = 3
qq = 2
edgess = [[0, 0], [1, 2], [1, 2]]
queryy = [[2, 3, 2, 3, 3]], [2, 3, 2, 3, 1]
print(solve(nn, qq, edgess, queryy))
