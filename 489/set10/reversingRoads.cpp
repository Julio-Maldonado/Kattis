#include <string>
#include <vector>
#include <iostream>
#include <limits.h>

using namespace std;

void isComponentRoot(int i, vector<int> &s, vector<int> &low, vector<vector<int> > & components) {
    vector<int> component;
    while (true) {
        int last = s.back(); s.pop_back();
        component.push_back(last);
        low[last] = INT_MAX;
        if (last == i)
            break;
    }
    components.push_back(component);
}

void dfs(int i, vector<vector<int> > &graph, vector<bool> &visited, vector<int> &s, int &time, vector<int> &low, vector<vector<int> > & components) {
    s.push_back(i);
    low[i] = time++;
    visited[i] = true;

    bool isRoot = true;
    for (int j = 0; j < graph[i].size(); j++) {
        int v = graph[i][j];
        if (!visited[v])
            dfs(v, graph, visited, s, time, low, components);
        if (low[i] > low[v]) {
            low[i] = low[v];
            isRoot = false;
        }
    }

    if (isRoot) isComponentRoot(i, s, low, components);
}

bool in(vector<int> v, int x) {
    for (int i = 0; i < v.size(); i++)
        if (v[i] == x)
            return true;

    return false;
}

bool tarjan(vector<vector<int> > &graph) {
    int n = graph.size();
    int time = 0;
    vector<int> s, low(n);
    vector<bool> visited(n, false);
    vector<vector<int> > components;
    for (int i = 0; i < n; i++)
        if (!visited[i])
            dfs(i, graph, visited, s, time, low, components);

    for (int i = 0; i < n; i++)
        if (!in(components[0], i))
            return false;

    return true;
}

int main() {
    int m, n, testCase = 1;
    while (cin >> m >> n) {
        if (cin.eof()) {
            return 0;
        }
        vector<vector<int> > graph(m);
        vector<pair<int, int> > edges(n);
        vector<bool> possible(n);
        for (int i = 0; i < n; i++) {
            int a, b;
            cin >> a >> b;
            graph[a].push_back(b);
            edges[i] = make_pair(a, b);
        }
        cout << "Case " << testCase << ": ";
        if (tarjan(graph))
            cout << "valid" << endl;
        else {
            bool reverse = false;
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < graph[i].size(); j++) {
                    int x = i, y = graph[x][0];
                    graph[x].erase(graph[x].begin());
                    graph[y].push_back(x);
                    if (tarjan(graph)) {
                        reverse = true;
                        pair<int, int> pr = make_pair(x, y);
                        for (int k = 0; k < n; k++)
                            if (edges[k] == pr)
                                possible[k] = true;
                    }
                    graph[x].push_back(y);
                    graph[y].erase(graph[y].end() - 1);
                }
            }
            if (reverse) {
                for (int i = 0; i < n; i++) 
                    if (possible[i]) {
                        cout << edges[i].first << " " << edges[i].second << endl;
                        break;
                    }
            } else cout << "invalid\n";
        }
        testCase++;
    }

    return 0;
}
