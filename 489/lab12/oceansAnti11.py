from __future__ import print_function

def solve():
    t = int(input())

    dp = [0] * 10001
    dp[1] = 2
    dp[2] = 3
    dp[3] = 5
    for i in range(4, 10001):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007

    for i in range(t):
        n = int(input())
        print(dp[n] % 1000000007)

def main():
    solve()

if __name__ == "__main__":
    main()
