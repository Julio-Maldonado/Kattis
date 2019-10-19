from __future__ import print_function

def solve():
    h, w = map(int, raw_input().split(" "))

    left, right = 0, 0
    graph = [[None] * w for i in range(h)]
    for i in range(h):
        line = raw_input()
        j = 0
        k = 0.5
        for char in line:
            if (char != '.'):
                graph[i][j] = k
            else:
                graph[i][j] = 0
            j += 1
            k += 1

    com, sum, count = 0, 0, 0
    for i in range(h):
        for j in range(w):
            sum += graph[i][j]
            if (graph[i][j] != 0):
                count += 1
    com = sum / count

    for i in range(0,len(graph[h - 1])):
        if (graph[h-1][i] != 0):
            left = graph[h-1][i] - 0.5
            break
    for i in range(len(graph[h - 1]) - 1, -1, -1):
        if (graph[h-1][i] != 0):
            right = graph[h-1][i] + 0.5
            break

    if (com < left):
        print("left")
    elif (com > right):
        print("right")
    else:
        print("balanced")

def main():
    solve()

main()
