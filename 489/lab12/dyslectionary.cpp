#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int max(int a, int b) { return (a > b) ? a : b; }

void print(vector<string> vec) {
    int maxLength = 0;
    for (int i = 0; i < vec.size(); i++) {
        maxLength = max(maxLength, vec[i].size());
        reverse(vec[i].begin(), vec[i].end());
    }
    sort(vec.begin(), vec.end());
    for (int i = 0; i < vec.size(); i++)
        reverse(vec[i].begin(), vec[i].end());

    for (int i = 0; i < vec.size(); i++) {
        if (vec[i].size() < maxLength) {
            for (int j = 0; j < maxLength - vec[i].size(); j++)
                cout << " ";
        }
        cout << vec[i] << endl;
    }
}

int main() {
    string line;
    vector<string> vec;
    while (getline(cin, line)) {
        if (line == "") {
            print(vec);
            cout << endl;
            vec.clear();
        } else {
            vec.push_back(line);
        }
    }
    print(vec);

    return 0;
}