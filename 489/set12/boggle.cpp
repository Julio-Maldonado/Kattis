#include <string>
#include <vector>
#include <iostream>

using namespace std; 

vector<int> dx = {-1, -1, -1, 0, 0, 1, 1, 1};
vector<int> dy = {-1, 0, 1, -1, 1, -1, 0, 1};
vector<int> scores = {0, 0, 0, 1, 1, 2, 3, 5, 11};
vector<vector<bool> > visited(4, vector<bool> (4, false));

bool dfs(vector<string>& matrix, string word, int i, int j, int k) {
    if (k == word.size())
        return true;
    if (i < 0 || i > 3 || j < 0 || j > 3)
        return false;
    if (visited[i][j])
        return false;
    if (word[k] != matrix[i][j])
        return false;
    for (int z = 0; z < 8; z++) {
        int zi = dx[z], zj = dy[z];
        visited[i][j] = true;
        bool flag = dfs(matrix, word, i + zi, j + zj, k + 1);
        visited[i][j] = false;
        if (flag)
            return true;
    }
    return false;
}

bool findBoggle(vector<string>& matrix, string &word) {
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++)
            if (dfs(matrix, word, i, j, 0))
                return true;
    return false;
}

int main() {
    int w;
    cin >> w;
    vector<string> words(w);
    for (auto &word : words)
        cin >> word;

    int b;
    cin >> b;
    while (b--) {
        vector<string> matrix(4);
        for (auto &m : matrix)
            cin >> m;

        int score = 0, foundWords = 0;
        string longestWord = "";

        for (auto &word : words) {
            if (findBoggle(matrix, word)) {
                foundWords++;
                if (word.size() > longestWord.size())
                    longestWord = word;
                if (word.size() == longestWord.size() && word < longestWord)
                    longestWord = word;
                score += scores[word.size()];
            }
        }
        cout << score << " " << longestWord << " " << foundWords << endl;
    }

    return 0; 
}

/*
#include <string>
#include <vector>
#include <iostream>
#include <unordered_map>

using namespace std;

struct Node {
    char c;
    vector<int> indexes;
    unordered_map<char, Node*> children;
    Node(char c): c(c){}
};

int maxLen = 0;

void insert(Node* root, string str, int index, int level) {
    root->indexes.push_back(index);

    // it is repeated and length is greater than maxLen
    // then store the substring
    if (str.empty())
        return;

    if (root->indexes.size() > 1 && maxLen < level)
        maxLen = level;

    Node* child;
    if (root->children.count(str[0]) == 0) {
        child = new Node(str[0]);
        root->children[str[0]] = child;
    } else child = root->children[str[0]];

    insert(child, str.substr(1), index, level+1);
}

int main() {
    int l;
    string str;
    cin >> l >> str;

    Node* root = new Node('.');

    for (int i = 0; i < l; i++) {
        string sub = str.substr(i);
        insert(root, sub, i, 0);
    }

    cout << maxLen << endl;

    return 1;
}
*/