from __future__ import print_function

def solve():
    n = int(input())

    sum = 0
    turns = int(2 ** (n - 1))
    while n:
        c = input()
        if (c == 'O'):
            sum += turns
        turns = int(turns / 2)
        n -= 1
    print(int(sum))

def main():
    solve()

if __name__ == '__main__':
    main()