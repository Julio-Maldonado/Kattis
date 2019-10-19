from __future__ import print_function

def solve():
    n = int(input())
    if n < 2:
        print(0)
    else:
        print((1 << n) - n - 1)

def main():
    solve()

if __name__ == "__main__":
    main()
