from __future__ import print_function
import math

def solve():
    line1 = input().split(" ")
    n, m, r = int(line1[0]), int(line1[1]), float(line1[2])
    
    a1, b1, a2, b2 = map(int, input().split(" "))

    sz = r / m
    dist = abs(b1 - b2) * sz
    rec = abs(a1 - a2) / n

    b = min(b1, b2)
    while (b):
        a = 2 * sz
        dist1 = math.pi * rec * sz * (b - 1) + a
        dist2 = math.pi * rec * sz * b

        if (dist1 < dist2):
            dist += a
            b -= 1
        else:
            dist += dist2
            break
    
    if (dist > 0.0000001):
        print(dist)
    else:
        print(0)

def main():
    solve()

if __name__ == "__main__":
    main()
  