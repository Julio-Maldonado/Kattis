from __future__ import print_function

def solve():
    p = int(input())
    for i in range(p):
        k, n = map(int, input().split(' '))
        print(k, int(n * (n + 3) / 2))

def main():
    solve()

if __name__ == "__main__":
    main()
