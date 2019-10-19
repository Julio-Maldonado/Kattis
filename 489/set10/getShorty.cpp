#include <queue>
#include <vector>
#include <iostream>

using namespace std;

int main() {
    while (true) {
        int n, m;
        cin >> n >> m;
        if (n == 0 && m == 0)
            return 0;

        vector<vector<pair<double, int> > > graph(n);
        for(int i = 0; i < m; i++) {
            int n1, n2;
            double f;
            cin >> n1 >> n2 >> f;
            graph[n1].push_back(make_pair(f, n2));
            graph[n2].push_back(make_pair(f, n1));
        }

        vector<double> ans(n);
        vector<bool> visited(n, false);
        priority_queue<pair<double,int> > pq;
        pq.push(make_pair(1,0));

        while (!pq.empty()) {
            pair<double, int> p = pq.top();
            int cur = p.second;
            double curSize = p.first;
            pq.pop();

            if (!visited[cur]) {
                visited[cur] = true;
                ans[cur] = curSize;

                for(int j = 0; j < graph[cur].size(); j++) {
                    pair<double, int> p = graph[cur][j];
                    int n = p.second;
                    double f = p.first;
                    pq.push(make_pair(curSize * f, n));
                }
            }
        }
        printf("%.4f\n", ans[n - 1]);
    }

    return 0;
}