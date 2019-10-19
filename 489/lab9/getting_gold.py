from __future__ import print_function

def nearTrap(graph, i, j):
    return graph[i-1][j] == 'T' or graph[i+1][j] == 'T' or graph[i][j-1] == 'T' or graph[i][j+1] == 'T'

def bfs(graph, w, h, i, j):
    count = 0
    visited = [[False] * w for k in range(h)]
    stack = [(i, j)]
    gotten = set()

    while stack:
        cur = stack.pop()
        i, j = cur[0], cur[1]

        if (visited[i][j]):
            continue
        visited[i][j] = True

        if (graph[i][j] == 'G'):
            gotten.add((i, j))
            count += 1

        if nearTrap(graph, i, j):
            continue

        if (i > 0): # up
            if graph[i-1][j] != '#' and graph[i-1][j] != 'T':
                stack.append((i - 1, j))
        if ((j + 1) < w): # right
            if graph[i][j+1] != '#' and graph[i][j+1] != 'T':
                stack.append((i, j + 1))
        if ((i + 1) < h): # down
            if graph[i+1][j] != '#' and graph[i+1][j] != 'T':
                stack.append((i + 1, j))
        if (j > 0): # left
            if graph[i][j-1] != '#' and graph[i][j-1] != 'T':
                stack.append((i, j - 1))

    print(count)

def solve():
    w, h = map(int, input().split())
    graph = []
    si, sj = 0, 0
    found = False
    for i in range(h):
        line = input().strip()
        if (not found):
            si = i
            sj = line.find('P')
            #print(sj)
            if (sj != -1):
                found = True
        graph.append(line)

    bfs(graph, w, h, si, sj)

def main():
    solve()

if __name__ == '__main__':
    main()
