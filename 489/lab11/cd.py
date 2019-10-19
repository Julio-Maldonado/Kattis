from __future__ import print_function

def solve():
    while True:
        n, m = map(int, raw_input().split(" "))
        if (n == 0 and m == 0):
            return
        graph = {}
        total = 0
        for _ in range(n):
            graph[int(raw_input())] = True
        for _ in range(m):
            if int(raw_input()) in graph:
                total += 1
        print(total)
    

def main():
    solve()

if __name__ == "__main__":
    main()
