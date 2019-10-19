#include <iostream>

using namespace std;

int main() {
    int q, m, s, l;
    cin >> q >> m >> s >> l;

    int time = 0;
    int maxQTime = 0;
    if (l > m) {
        int x;
        if (l % m == 0)
            x = l / m;
        else
            x = l / m + 1;
        maxQTime =  x * q;
        cout << "x = " << x << endl;
    } else {
        int machinesLeft =  m - l;
        int secondCPUTimes = s / machinesLeft;
        maxQTime = q;

    }

    cout << maxQTime << endl;

    return 0;
}
