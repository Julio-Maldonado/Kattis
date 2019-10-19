from __future__ import print_function

def isEqualColumn(matrix, mid, x, c):
    for i in range(c - 1):
        sub1 = matrix[i][0:x]
        sub2 = matrix[i+1][0:x]
        # print(sub1, sub2)
        if sub1 == sub2:
            return False
    return True

def solve():
    r, c = map(int, input().split())
    matrix = []
    for _ in range(r):
        matrix.append(input())

    mmatrix = []
    for i in range(c):
        t = []
        for j in range(r):
            t.insert(0, matrix[j][i])
        mmatrix.append(t)

    mmatrix = sorted(mmatrix)

    low, high = 0, r
    while low < high:
        mid = (low + high) >> 1
        if isEqualColumn(mmatrix, mid, r - mid, c):
            maxDeleted = mid
            low = mid + 1
        else:
            high = mid

    print(maxDeleted)

def main():
    solve()

if __name__ == '__main__':
    main()