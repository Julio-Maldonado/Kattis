from __future__ import print_function

def solve():
    n = int(input())
    words = {}
    for _ in range(n):
        word = input()
        length = len(word)
        count = 0
        if word in words:
            count += words[word]

        for i in range(length, 0, -1):
            truncatedWord = word[:i]
            if truncatedWord not in words:
                words[truncatedWord] = 1
            else:
                words[truncatedWord] += 1
        print(count)

def main():
    solve()

if __name__ == '__main__':
    main()