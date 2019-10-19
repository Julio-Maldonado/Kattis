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

bool compareVector(vector<int> a, vector<int> b) {
    return a[2] < b[2];
}

int main() {
    int n, m;
    cin >> n >> m;

    vector<vector<int> > vec;
    for (int i = 0; i < m; i++) {
        vector<int> line(3);
        int n1, n2, l;
        cin >> n1 >> n2 >> l;
        line[0] = n1; line[1] = n2; line[2] = l;
        vec.push_back(line);
    }

    sort(vec.begin(), vec.end(), compareVector);

    initSet(n);
    int min = 0;
    for (int i = 0; i < vec.size(); i++) {
        vector<int> v = vec[i];
        if (!isSameSet(v[0], v[1])) {
            unionSet(v[0], v[1]);
            if (min < v[2])
                min = v[2];
        }
    }

    for (int i = 1; i < n; i++) {
        if (!isSameSet(i - 1, i)) {
            cout << "IMPOSSIBLE" << endl;
            return 0;
        }
    }

    cout << min << endl;
    return 0;
}