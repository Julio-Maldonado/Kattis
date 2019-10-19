from __future__ import print_function

def solve():
    n = int(raw_input())

    indexes = []
    for i in range(n):
        indexes.append(int(raw_input()))
    indexes = sorted(indexes)

    i = 1
    h = 0
    for itr in range(len(indexes) - 1, -1, -1):
        if ((indexes[itr] >= i) and ((itr - 1 < 0) or (indexes[itr - 1]) <= i)):
            h = i
        i += 1
    
    print(h)


def main():
    solve()

main()
