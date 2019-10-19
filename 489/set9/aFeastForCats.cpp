#include <vector>
#include <iostream>
#include <algorithm>

#define REP(i, a, b) for (int i = int(a); i <= int(b); i++) // all codes involving REP uses this macro

using namespace std;

vector<int>pset(1000); // 1000 is just an initial number, it is user-adjustable.

void initSet(int _size) { pset.resize(_size); REP (i, 0, _size - 1) pset[i] = i; }

int findSet(int i) { return (pset[i] == i) ? i : (pset[i] = findSet(pset[i])); }

void unionSet(int i, int j) { pset[findSet(i)] = findSet(j); }

bool isSameSet(int i, int j) { return findSet(i) == findSet(j); }

bool compareMatrix(vector<int> m1, vector<int> m2) {
    return m1[2] < m2[2];
}

int main() {
    int T;
    cin >> T;

    while (T--) {
        int m, c;
        cin >> m >> c;
        int size = (c * (c - 1)) / 2;
        initSet(c);

        // input is of matrix market format
        vector<vector<int> > matrix(size, vector<int>(3,0));
        for (int k = 0; k < size; k++) {
            int i, j , d;
            cin >> i >> j >> d;

            matrix[k][0] = i;
            matrix[k][1] = j;
            matrix[k][2] = d;
            //cout << matrix[k][0] << " " << matrix[k][1] << " " << matrix[k][2] << "\n";
        }

        sort(matrix.begin(), matrix.end(), compareMatrix);
        // for (int i = 0; i < size; i++) {
        //     cout << matrix[i][0] << " " << matrix[i][1] << " " << matrix[i][2] << "\n";
        // }
        int droppedMilk = 0;
        for (int i = 0; i < size; i++) {
            vector<int> cat = matrix[i];
            if (!isSameSet(cat[0], cat[1])) {
                unionSet(cat[0], cat[1]);
                droppedMilk += cat[2];
            }
        }

        if ((m - c - droppedMilk) >= 0) cout << "yes\n";
        else cout << "no\n";
    }

    return 0;
}
