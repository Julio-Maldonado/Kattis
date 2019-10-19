#include <math.h>
#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;
    int req = 1;
    double perimeter = 0.0;
    double p2 = 2.0*(pow(2.0,-5.0/4)+pow(2.0,-3.0/4));
    double p1 = sqrt(2)*p2;

    for (int i = 2; i <= n; i++) {
        req *= 2;
        int x;
        cin >> x;
        if (x >= req) { // we're done
            perimeter += req*p2;
            req = 0;
        } else {
            req -= x;
            perimeter += x*p2;
        }
        p2 /= sqrt(2);
    }

    cout << fixed;
    cout.precision(10);
    
    double answer = (perimeter - p1) / 2.0; // here's the trick! ;)
    if (req == 0.0) cout << answer << endl; // double check if condition (diff < eps) -> No need, got accepted!
    else cout << "impossible" << endl;
    
    return 0;
}
