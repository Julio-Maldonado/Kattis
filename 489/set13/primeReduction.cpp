#include <math.h>
#include <iostream>

using namespace std;

bool arr[1000000000];

bool isPrime(long long n) {
    if (n < 2)
        return false;
    else if (n < 4)
        return true;
    else if (n % 2 == 0 || n % 3 == 0)
        return false;
    else if (arr[n])
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
            if (arr[n] || isPrime(n)) {
            // if (isPrime(n)) {
                arr[n] = true;
                ret += n;
                break;
            }
        } else i++;
    }
    return ret;
} 

int main() {
    // ios::sync_with_stdio(false);
    // cin.tie(NULL); cout.tie(NULL);

    long long n;
    while (cin >> n) {
        if (n == 4) break;
        long long i = 1;
        while (!isPrime(n)) {
            n = reduce(n);
            // cout << n << endl;
            i++;
        }
        arr[n] = true;
        cout << n << " " << i << endl;
    }
    return 0;
}
