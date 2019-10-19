from __future__ import print_function

def inRange(i, j, r, c):
    return i >= 0 and i < c and j >= 0 and j < r

def bfs(graph, finalI, finalJ, r, c):
    SEPERATOR = -999999999
    deque = []
    visited = [[False] * c for i in range(r)]
    for i in range(1, r - 1):
        if (graph[i][0] == 'D'):
            visited[i][0] = True
            deque.insert(0, (i, 0))
        if (graph[i][c - 1] == 'D'):
            visited[i][c - 1] = True
            deque.insert(0, (i, c - 1))

    for i in range(1, c - 1):
        if (graph[0][i] == 'D'):
            visited[0][i] = True
            deque.insert(0, (0, i))
        if (graph[r - 1][i] == 'D'):
            visited[r - 1][i] = True
            deque.insert(0, (r - 1, i))

    count = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    deque.append((SEPERATOR, 0))
    while deque:
        if (deque[0][0] == SEPERATOR):
            deque.append((SEPERATOR, 0))
            deque.pop(0)
            count += 1
        pos = deque.pop(0)
        i = pos[0]
        j = pos[1]
        if (i == finalI and j == finalJ):
            print(count)
            return

        if inRange(i - 1, j, r, c):
            if (graph[i-1][j] == 'c' and not visited[i-1][j]):
                visited[i-1][j] = True
                deque.append((i-1, j))
            if (graph[i-1][j] == 'D' and not visited[i-1][j]):
                visited[i-1][j] = True
                deque.insert(0,(i-1, j))
        if inRange(i, j - 1, r, c):
            if (graph[i][j-1] == 'c' and not visited[i][j-1]):
                visited[i][j-1] = True
                deque.append((i,j-1))
            if (graph[i][j-1] == 'D' and not visited[i][j-1]):
                visited[i][j-1] = True
                deque.insert(0,(i, j-1))
        if inRange(i + 1, j, r, c):
            if (graph[i+1][j] == 'c' and not visited[i+1][j]):
                visited[i+1][j] = True
                deque.append((i+1,j))
            if (graph[i+1][j] == 'D' and not visited[i+1][j]):
                visited[i+1][j] = True
                deque.insert(0,(i+1, j))
        if inRange(i, j + 1, r, c):
            if (graph[i][j+1] == 'c' and not visited[i][j+1]):
                visited[i][j+1] = True
                deque.append((i,j+1))
            if (graph[i][j+1] == 'D' and not visited[i][j+1]):
                visited[i][j+1] = True
                deque.insert(0,(i, j+1))

def solve():
    r, c = map(int, raw_input().split(" "))

    graph = [[None] * c for i in range(r)]
    for i in range(r):
        line = raw_input()
        j = 0
        for char in line:
            graph[i][j] = char
            j += 1

    carI, carJ = map(int, raw_input().split(" "))
    finalI, finalJ = carI - 1, carJ - 1

    bfs(graph, finalI, finalJ, r, c)

def main():
    solve()

main()
