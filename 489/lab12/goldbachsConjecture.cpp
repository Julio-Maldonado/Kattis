#include <math.h>
#include <vector>
#include <iostream>

using namespace std;

bool primes[32000];

bool isPrime(long long n) {
    if (n < 2)
        return false;
    else if (n < 4)
        return true;
    else if (n % 2 == 0 || n % 3 == 0)
        return false;
    else if (primes[n])
        return true;
    long long x = (long long)sqrt(n) + 1;
    for (long long i = 6; i <= x; i += 6)
        if (n % (i + 1) == 0 || n % (i - 1) == 0)
            return false;

    return true;
}

long long reduce(long long n) {
    long long i = 2, ret = 0;
    while (n > 1) {
        if (n % i == 0) {
            n /= i;
            ret += i;
            if (primes[n] || isPrime(n)) {
            // if (isPrime(n)) {
                primes[n] = true;
                ret += n;
                break;
            }
        } else i++;
    }
    return ret;
} 

int main() {
    long long n;
    cin >> n;
    while (n--) {
        int x; cin >> x;
        if (x == 4) {
            cout << "4 has 1 representation(s)\n2+2\n\n";
            continue;
        }
        vector<pair<int,int> > solutions;
        int i = 3, j = x - 3;
        while (i <= j) {
            if (primes[i] && primes[j]) {
                solutions.push_back(make_pair(i,j));
            } else if (isPrime(i) && isPrime(j)) {
                primes[i] = primes[j] = true;
                solutions.push_back(make_pair(i,j));
            }
            i+=2;
            j=x-i;
        }
        
        cout << x << " has " << solutions.size() << " representation(s)\n";
        for (int i = 0; i < solutions.size(); i++)
            cout << solutions[i].first << "+" << solutions[i].second << "\n";

        cout << "\n";
    }
    return 0;
}
