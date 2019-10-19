#include <vector>
#include <iostream>

#define REP(i, a, b) for (int i = int(a); i <= int(b); i++) // all codes involving REP uses this macro

using namespace std;

vector<int>pset(1000); // 1000 is just an initial number, it is user-adjustable.

void initSet(int _size) { pset.resize(_size); REP (i, 0, _size - 1) pset[i] = i; }

int findSet(int i) { return (pset[i] == i) ? i : (pset[i] = findSet(pset[i])); }

void unionSet(int i, int j) { pset[findSet(i)] = findSet(j); }

bool isSameSet(int i, int j) { return findSet(i) == findSet(j); }

int main() {
    int r, c;
    cin >> r >> c;
    vector<vector<int> > graph(r, vector<int>(c,0));

    for (int i = 0; i < r; i++) {
        string line;
        cin >> line;
        for (int j = 0; j < line.size(); j++)
            graph[i][j] = line[j] - '0';
    }

    initSet(r * c);

    vector<int> xVec = {-1, 1, 0, 0};
    vector<int> yVec = {0, 0, 1, -1};

    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            for (int z = 0; z < 4; z++) {
                int x = i + xVec[z];
                int y = j + yVec[z];
                if ((x >= r) || (y >= c))
                    continue;
                else if ((x < 0) || (y < 0))
                    continue;
                else if (graph[i][j] == graph[x][y])
                    unionSet((c * i) + j, (c * x) + y);
                else continue;
            }
        }
    }

    int n;
    cin >> n;
    while (n--) {
        int r1, c1, r2, c2;
        cin >> r1 >> c1;
        r1--; c1--;
        cin >> r2 >> c2;
        r2--; c2--;

        if (isSameSet((c * r1) + c1, (c * r2) + c2))
            if (graph[r1][c1] == 0) cout << "binary\n";
            else cout << "decimal\n";
        else cout << "neither\n";
    }

    return 0;
}
