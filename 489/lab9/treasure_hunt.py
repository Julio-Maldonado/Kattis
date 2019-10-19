from __future__ import print_function

def bfs(graph, r, c):
    # if (graph[0][0] == "T"):
    #     print(0)
    count, i, j = 0, 0, 0
    visited = [[False] * c for k in range(r)]
    while True:
        if (i < 0 or i >= r):
            print("Out")
            return
        elif (j < 0 or j >= c):
            print("Out")
            return

        if (visited[i][j]):
            print("Lost")
            return

        visited[i][j] = True
        #print("i =", i, "j =", j)
        play = graph[i][j]
        #print(play)
        if (play == "T"):
            print(count)
            return

        if (play == "N"):
            i -= 1
        elif (play == "S"):
            i += 1
        elif (play == "E"):
            j += 1
        elif (play == "W"):
            j -= 1

        count += 1

def solve():
    r, c = map(int, raw_input().split())
    graph = []
    for i in range(r):
        graph.append(list(raw_input().strip()))

    # for i in range(r):
    #     for j in range(c):
    #         print(graph[i][j], end=" ")
    #     print()
    bfs(graph, r, c)

def main():
    solve()

if __name__ == '__main__':
    main()
