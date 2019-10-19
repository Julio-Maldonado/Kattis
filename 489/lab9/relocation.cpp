#include <vector>
#include <iostream>

using namespace std;

int main() {
    int n, q;
    cin >> n >> q;

    vector<int> vec(n + 1);
    for(int i = 0; i < n; i++) {
        int val;
        cin >> val;
        vec[i + 1] = val;
    }

    for(int i = 0; i < q; i++) {
        int option, a, b;
        cin >> option >> a >> b;
        // a--; b--;
        if (option == 2)
            cout << abs(vec[a]-vec[b]) << endl;
        else if (option == 1)
            vec[a] = b;
    }

    return 0;
}