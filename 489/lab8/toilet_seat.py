from __future__ import print_function

def solve():
    string = raw_input()
    first1, first2, first3 = string[0], string[0], string[0]
    string = string[1:]
    stringSize = len(string)
    total1, total2, total3 = 0, 0, 0
    
    for i in range(stringSize):
        s = string[i]
        if (s != first1):
            first1 = s
            total1 += 1
        if (first1 != 'U'):
            first1 = 'U'
            total1 += 1
        if (s != first2):
            first2 = s
            total2 += 1
        if (first2 != 'D'):
            first2 = 'D'
            total2 += 1
        if (s != first3):
            first3 = s
            total3 += 1

    print(total1)
    print(total2)
    print(total3)

def main():
    solve()

main()
