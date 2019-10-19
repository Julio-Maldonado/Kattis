#include <math.h>
#include <vector>
#include <iostream>

using namespace std;

bool dfs(vector<vector<int> > graph, vector<bool> &visited, vector<int> &match, int u){
    for (int i = graph[u].size() - 1; i >= 0; i--){
        int v = graph[u][i];
        if (!visited[v]) {
            visited[v] = true;
            if ((match[v] == -1) || dfs(graph, visited, match, match[v])) {
                match[v] = u;
                return true;
            }
        }
    }
    return false;
}

int maximum_matching(vector<vector<int> > graph, int n, int m) {
    // int X = 100, Y = 100;
    vector<int> match(m, -1);

    int ans = 0;
    for (int i = 0; i < n; i++) {
        vector<bool> visited(m, false);
        ans += dfs(graph, visited, match, i);
    }

    return ans;
}

int main() {
	int n, m, s, v;
	while (cin >> n >> m >> s >> v) {
        double x1[100], y1[100], x2[100], y2[100];
		for (int i = 0; i < n; i++) {
            double gx, gy;
            cin >> gx >> gy;
            x1[i] = gx;
            y1[i] = gy;
        }
		for (int i = 0; i < m; i++) {
            double ghx, ghy;
            cin >> ghx >> ghy;
            x2[i] = ghx;
            y2[i] = ghy;
        }

        vector<vector<int> > graph(n);

		for (int i = 0; i < n; i++)
			for (int j = 0; j < m; j++) {
				if ((pow(x1[i]-x2[j], 2) + pow(y1[i]-y2[j], 2)) / (s * s) <= (v * v))
					graph[i].push_back(j);
            }

        // for (int i = 0; i < graph.size(); i++) {
        //     for (int j = 0; j < graph[i].size(); j++) {
        //         cout << graph[i][j] << " ";
        //     }
        //     cout << endl;
        // }
        // cout << "here\n";
		cout << n - maximum_matching(graph, n, m) << endl;
	}

	return 0;
}
