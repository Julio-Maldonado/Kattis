from __future__ import print_function
import math

def solve():
    n, m = map(int, raw_input().split())
    
    deg = [0] * (n)
    graph = [[] * (n) for i in range(n)]
    for i in range(m):
        a, b = map(int, raw_input().split())
        a, b = a - 1, b - 1
        deg[b] += 1
        graph[a].append(b)
    # print(graph)
    q = []
    for i in range(n):
        if (deg[i] == 0):
            q.append(i)

    path = []
    while q:
        cur = q.pop(0)
        path.append(cur)
        # print(cur)
        for i in graph[cur]:
            deg[i] -= 1
            if (deg[i] == 0):
                q.append(i)
    
    if (len(path) == n):
        for i in path:
            print(i + 1)
    else:
        print("IMPOSSIBLE")

    return

    
def main():
    solve()

if __name__ == "__main__":
    main()
