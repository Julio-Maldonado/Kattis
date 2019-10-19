from __future__ import print_function

def dfs(graph, visited, stack, i):
    if i in visited:
        return
    visited.add(i)
    if i in graph:
        for n in graph[i]:
            dfs(graph, visited, stack, n)

    stack.append(i)

def canBeBroken(graph, p, pairs):

    for pr in pairs:
        stack = []
        visited = set()
        a, b = pr[0], pr[1]
        graph[a].remove(b)
        graph[b].remove(a)
        dfs(graph, visited, stack, a)
        graph[a].add(b)
        graph[b].add(a)
        if (len(visited) != p):
            return True

    return False

def solve():
    while (True):
        p, c = map(int, raw_input().split(" "))
        if ((p == 0) and (c == 0)):
            return

        graph = {}
        pairs = []
        for i in range(c):
            a, b = map(int, raw_input().split(" "))

            if a not in graph:
                graph[a] = set()
            if b not in graph:
                graph[b] = set()

            graph[a].add(b)
            graph[b].add(a)
            pairs.append((a,b))

        if (canBeBroken(graph, p, pairs)):
            print("Yes")
        else:
            print("No")

    return

def main():
    solve()

if __name__ == "__main__":
    main()
