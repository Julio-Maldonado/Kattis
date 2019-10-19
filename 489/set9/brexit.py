from __future__ import print_function
from collections import deque

class Country:
    def __init__(self, idx):
        self.idx = idx
        self.edges = [] 
        self.left = False
        self.left_edges = set()

def bfs(countries, l, x):
    q = deque(countries[l].edges[:])
    while q:
        curr = q.popleft()
        if curr.left:
            continue
        if ((len(curr.left_edges) * 2) >= len(curr.edges)):
            curr.left = True
            for country in curr.edges:
                if country.left:
                    continue
                country.left_edges.add(curr.idx)
                q.append(country)
    
    if (countries[x].left):
        print('leave')
    else:
        print('stay')

def solve():
    c, p, x, l = map(int, raw_input().split())
    countries = []
    for i in range(c):
        countries.append(Country(i))

    for i in range(p):
        a, b = map(int, raw_input().split())
        countries[a-1].edges.append(countries[b-1])
        countries[b-1].edges.append(countries[a-1])

    for country in countries[l-1].edges:
        country.left_edges.add(l-1)
    countries[l-1].left = True

    bfs(countries, l - 1, x - 1)

def main():
    solve()

if __name__ == '__main__':
    main()
