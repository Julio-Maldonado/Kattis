from __future__ import print_function
from collections import OrderedDict

def solve():
    T = int(input())

    input()

    while T:
        n = int(input())
        arr = []

        for _ in range(n):
            team, placement = input().split(" ")
            placement = int(placement)
            arr.append(placement)
        arr = sorted(arr)
        ans = 0
        i = 1
        for t in arr:
            ans += abs(i - t)
            i += 1
        # print(arr)
        print(ans)
        T -= 1
        if T != 0:
            input()
    

def main():
    solve()

if __name__ == "__main__":
    main()