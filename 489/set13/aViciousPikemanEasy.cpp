#include <iostream>

using namespace std;

int compare (const void *a, const void *b) {
  return *(int*)a - *(int*)b;
}

int main() {
    int n, t;
    cin >> n >> t;

    int a, b, c;
    long long timeArr[10000];
    cin >> a >> b >> c >> timeArr[0];

    for (int i = 1; i < n; i++)
        timeArr[i] = ((a * timeArr[i-1] + b) % c) + 1;

    qsort(timeArr, n, sizeof(long long), compare);

    long long minPenalty = 0, solved = 0, maxSolved = 0;
    for (int i = 0; i < n; i++) {
        if ((maxSolved + timeArr[i]) <= t) {
            maxSolved += timeArr[i];
            minPenalty = (minPenalty + maxSolved) % 1000000007;
            solved++;
        } else {
            break;
        }
    }

    cout << solved << " " << minPenalty << endl;
    return 0;
}
