from __future__ import print_function

def solve():
    n = int(input())
    sheets = map(int, input().split(" "))

    answer, needed = 0, 1

    p1, p2 = 2 ** (-3/4), 2 ** (-5/4)

    for sheet in sheets:
        answer += needed * p1

        temp = p2
        p2 = p1
        p1 = temp

        p2 /= 2

        needed = needed * 2 - sheet

        if (needed <= 0):
            print(answer)
            return

    print("impossible")

def main():
    solve()

if __name__ == "__main__":
    main()
