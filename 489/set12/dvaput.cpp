#include <string>
#include <iostream>
#include <unordered_map>

using namespace std;

struct Node {
    char c;
    int count;
    unordered_map<char, Node*> children;
    Node(char c): c(c), count(0){}
};

void insert(Node* root, string &str, int &maxLength, int lvl, int i) {
    while (str.size() != 1) {
        // cout << str << endl;
        if (root->count > 1 && maxLength < lvl)
            maxLength = lvl;

        Node* child;
        if (root->children.count(str[0]) == 0) {
            child = new Node(str[0]);
            root->children[str[0]] = child;
        } else child = root->children[str[0]];
        lvl++;
        root = child;
        str = str.substr(1);
        root->count++;
    }
}

int suffixTreeCount(string str, int l) {
    Node* root = new Node('.');
    int maxLength = 0;
    for (int i = 0; i < 3*l/4; i++) {
        string sub = str.substr(i);
        insert(root, sub, maxLength, 0, i);
    }
    return maxLength;
}

int main() {
    int l;
    string str;
    cin >> l >> str;

    cout << suffixTreeCount(str, l) << endl;

    return 0;
}
