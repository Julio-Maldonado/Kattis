from __future__ import print_function

def dfs(graph, N, M):
    visited = [[False] * (M + 2) for i in range(N + 2)]
    stack = [(0, 0)]
    while stack:
        cur = stack.pop()
        i, j = cur[0], cur[1]

        graph[i][j] = 'w'
        visited[i][j] = True
        
        if (i > 0):
            if (((graph[i-1][j] == '0') or (graph[i-1][j]=='w')) and (not visited[i-1][j])):
                stack.append((i - 1, j))
        if (j > 0):
            if (((graph[i][j-1] == '0') or (graph[i][j-1]=='w')) and (not visited[i][j-1])):
                stack.append((i, j - 1))
                
        if (i < (N + 1)):
            if (((graph[i+1][j] == '0') or (graph[i+1][j]=='w')) and (not visited[i+1][j])):
                stack.append((i + 1, j))
        if (j < (M + 1)):
            if (((graph[i][j+1] == '0') or (graph[i][j+1]=='w')) and (not visited[i][j+1])):
                stack.append((i, j + 1))
    
    return graph

def solve():
    inp = map(int, input().split(" "))
    N, M = map(int, inp)

    graph = [['0'] * (M + 2)]
    for i in range(N):
        graph.append(['0'] + list(input()) + ['0'])
    graph.append(['0'] * (M + 2))

    graph = dfs(graph, N, M)

    coast = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if (graph[i][j] == '1'):
                if (graph[i - 1][j] == 'w'):
                    coast += 1
                if (graph[i + 1][j] == 'w'):
                    coast += 1
                if (graph[i][j - 1] == 'w'):
                    coast += 1    
                if (graph[i][j + 1] == 'w'):
                    coast += 1
    print(coast)

def main():
    solve()

main()
