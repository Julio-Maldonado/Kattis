from __future__ import print_function

def solve():
    while True:
        x = input()
        a,n = map(int,x.split("/"))
        count = 0
        for x in range(n + 1, 2*n + 1): 
            for y in range (x + 1, 2*n + 1):
                if x * y == n * x + n * y:
                    count += 1
        print(count)

def main():
    solve()

if __name__ == "__main__":
    main()

'''
1/1 = 1/2 + 1/2
1
1/2 = 1/3 + 1/6 = 1/4 + 1/4
2
1/3 = 1/4 + 1/12 = 1/6 + 1/6
2
1/4 = 1/8 + 1/8 = 1/5 + 1/20 = 1/6 + 1/12
3
1/5 = 1/10 + 1/10 = 1/6 + 1/30
2
1/6


1/5000 = 1/10000 + 1/10000

1/x + 1/y = 1/n

y + x = xy/n

y = xy/n - x = x(y/n - 1)

nx + ny = xy



1 + x/y = x/n

x/y = x/n - 1
x = y(x/n - 1)

1 = x/n - x/y = 8/4 - 8/8 = 20/4 - 20/5 = 12/4 - 12/6
y = xy/n - x

1/4 = 1/8 + 1/8 = 1/5 + 1/20 = 1/6 + 1/12
3

'''
