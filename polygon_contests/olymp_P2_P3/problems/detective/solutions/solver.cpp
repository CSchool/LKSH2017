#include <bits/stdc++.h>

using namespace std;

int main() {
    int n, a, b;
    cin >> n >> a >> b;
    a--;
    b--;
    int p[n];
    int d[n];
    vector<int> k[n];
    p[0] = 0;
    d[0] = 0;
    for (int i = 1; i < n; ++i) {
        int t;
        cin >> t;
        p[i] = t - 1;
        k[t - 1].push_back(i);
    }
    function<void(int, int)> f = [&](int v, int q) {
        d[v] = q;
        for (int u : k[v]) {
            f(u, q + 1);
        }
    };
    f(0, 0);
    while (d[a] != d[b]) {
        if (d[a] < d[b]) {
            b = p[b];
        } else {
            a = p[a];
        }
    }
    while (a != b) {
        a = p[a];
        b = p[b];
    }
    cout << a + 1 << endl;
    return 0;
}
