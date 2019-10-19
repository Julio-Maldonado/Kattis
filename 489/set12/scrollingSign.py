from __future__ import print_function

def solve():
    n = int(input())
    for _ in range(n):
        k, w = map(int, input().split(' '))
        word1 = input()
        c = k
        for _ in range(w - 1):
            word = input()
            res = 0
            for i in range(k):
                flag = True
                for j in range(k - i):
                    # print(i + j)
                    if (word1[i + j] != word[j]):
                        flag = False
                        break
                if flag:
                    res = k - i
                    break

            c += k - res
            word1 = word
        print(c)
    


def main():
    solve()

if __name__ == '__main__':
    main()