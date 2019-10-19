from __future__ import print_function

def solve():
    n = int(raw_input())
    graph = {}
    secondGraph = {}
    for i in range(n):
        line = raw_input()
        secondGraph[line] = 0
        if line not in graph:
            graph[line] = 1
        else:
            graph[line] += 1
    #print(graph)

    for i in range(n):
        line = raw_input()
        if line not in secondGraph:
            secondGraph[line] = 1
        else:
            secondGraph[line] += 1

    #print(secondGraph)
    count = 0
    for key in graph:
        if key in secondGraph and key in graph:
            count += min(secondGraph[key], graph[key])
    print(count)

def main():
    solve()

main()
