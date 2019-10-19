#include <iostream>

using namespace std;

int main() {
    int t; cin >> t;
    while (t--) {
        int k, a, b;
        string s;
        cin >> k >> s;
        int p = stoi(s.substr(0, s.find("/")));
        int q = stoi(s.substr(s.find("/") + 1, s.size()));
        if (p == 1 && q == 1) {
            a = 1;
            b = 2;
        } else if (p == 1) {
            a = q;
            b = q - 1;
        } else if (q == 1) {
            a = 1;
            b = p + 1;
        } else {
            int r = p / q;
            a = p % q;
            b = q - a;

            a = q;
            b = b + (q * r);
        }

        cout << k << " " << a << "/" << b << endl;
    }
    return 0;
}
