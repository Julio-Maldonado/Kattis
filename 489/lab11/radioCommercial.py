from __future__ import print_function

def solve():
    n, p = map(int, input().split(" "))

    students = list(map(int, input().split(" ")))
    
    maxSoFar, maxEndingHere = students[0] - p, students[0] - p
    
    i = 1
    while i < n:
        s = students[i] - p
        maxEndingHere = max(s, maxEndingHere + s)
        maxSoFar = max(maxSoFar, maxEndingHere)
        i += 1
    print(maxSoFar)


def main():
    solve()

if __name__ == "__main__":
    main()
