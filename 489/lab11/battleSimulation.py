from __future__ import print_function

def solve():
    graph = {
        'R': 'S',
        'B': 'K',
        'L': 'H',
        'RBL': 'C',
        'RLB': 'C',
        'BRL': 'C',
        'BLR': 'C',
        'LBR': 'C',
        'LRB': 'C',
        'C': 'C'
    }
    line = input()
    size = len(line)
    i = 0
    outputtedLine = []

    while i < size:
        code = line[i:i+3]
        # print(code)
        if code in graph:
            outputtedLine += graph[code]
            i+=3
        else:
            outputtedLine += graph[line[i]]
            i+=1
    print(outputtedLine)

def main():
    solve()

if __name__ == "__main__":
    main()
