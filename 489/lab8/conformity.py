from __future__ import print_function

def solve():
    n = int(raw_input())

    graph = []
    for i in range(n):
        graph.append(sorted(raw_input().split(" ")))

    max = 0
    count = {}
    for i in graph:
        count[str(i)] = 0

    for i in graph:
        count[str(i)] += 1
        if (count[str(i)] > max):
            max = count[str(i)]
    
    total = 0
    for i in count:
        if (count[i] == max):
            total += max

    print(total)
    #if (max == 1):
    #    print(n)
    #else:
    #    print(max)

def main():
    solve()

main()
