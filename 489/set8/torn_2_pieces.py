from __future__ import print_function

def dfs(graph, q, path, end):
    #visited = {q[0]: True}
    #print(graph)
    #print()
    while q:
        current = q.pop(-1)
        if (current not in graph):
            continue
        for stop in graph[current]:
            if (stop not in path and stop in graph):
                #visited[stop] = True
                # if probably not needed
                if current in path:
                    path[stop] = current
                q.append(stop)
                if (stop == end):
                    #print(path)
                    return path, True
                    break

    #print(path)
    return path, False

def solve():
    n = int(raw_input())

    graph = {}
    for i in range(n):
        line = raw_input().split(" ")
        first = line[0]
        #graph[first] = {}
        for stop in line:
            if stop not in graph:
                graph[stop] = {}
            #if stop != first:
            
        for stop in line:
            graph[stop][first] = True#.add(first)
            graph[first][stop] = True#.add(stop)

    #print(graph)
    a, b = raw_input().split(" ")
    q = [a]
    path = {a: "start"}
    path, found = dfs(graph, q, path, b)

    if not found:
        print("no route found")
        return

    stack = []
    stop = b
    while (stop != "start"):
        stack.append(stop)
        stop = path[stop]

    for i in range(len(stack) - 1, -1, -1):
        print(stack[i], end=" ")
    print()

def main():
    solve()

main()
