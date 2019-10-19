#include <math.h>
#include <string>
#include <iostream>

using namespace std;

int main() {
    string s;
    while (cin >> s) {
        string line = s.substr(2,s.size());
        int n = stoi(line);
        // cout << n << endl;
        int ans = 0;
        for (int i = n + 1; i < 2*n + 1; i++) {
            int y = n * i;
            if (y % (i - n) == 0) {
                ans++;
            }
        }
        
        cout << ans << endl;
    }
    return 0;
}