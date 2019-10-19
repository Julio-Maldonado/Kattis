from __future__ import print_function

#test = True
test = False
def solve():
    N = int(input())
    graph, count = {}, {}
    for i in range(N):
        line = input().split()
        first = line[0].replace(':', '')
        if first not in graph:
            count[first] = 0
            graph[first] = set()
        for i in range(1, len(line)):
            rule = line[i]
            if rule not in graph:
                count[rule] = 0
                graph[rule] = set()
            graph[rule].add(first)

    # for i in graph:
    #     print(i, graph[i])

    c = input()
    stack = [c]
    visited = set()
    while stack:
        cur = stack.pop()
        #print(cur, end = "TEST\n")
        if cur not in visited:
            #print(cur)
            visited.add(cur)
            for rule in graph[cur]:
                count[rule] += 1
                if rule not in visited:
                    stack.append(rule)

    ans = [c]
    while ans:
        #print(ans)
        cur = ans.pop()
        print(cur)
        for rule in graph[cur]:
            count[rule] -= 1
            if (count[rule] == 0):
                ans.append(rule)

def main():
    solve()

if __name__ == '__main__':
    main()
