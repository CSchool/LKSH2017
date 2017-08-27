#include <iostream>
#include <vector>
#include "testlib.h"

using namespace std;

int main(int argc, char *argv[])
{
    registerGen(argc, argv, 1);
    int n = rnd.next(2, atoi(argv[1]));
    int t = n * atoi(argv[2]) / 100;
    int w = atoi(argv[3]);
    if (t < 1) t = 1;
    if (t > n) t = n;

    vector<double> dd(t);
    vector<int> rl(t);
    double tt = 0;
    for (auto &x : dd) tt += (x = rnd.next());
    shuffle(dd.begin(), dd.end());
    tt = n / tt;
    for (int i = 0; i < t; ++i)
    {
        rl[i] = round(dd[i] * tt);
        if (rl[i] < 1)
            rl[i] = 1;
    }
    int ss = 0;
    for (int i = 0; i < t; ++i)
        ss += rl[i];
    int q = n - ss; // we need to distribute this
    if (q < 0)
    {
        while (q < 0)
        {
            for (int i = 0; i < t && q < 0; ++i)
                if (rl[i] > 1)
                    rl[i]--, q++;
        }
    } else 
    if (q > 0)
    {
        while (q > 0)
        {
            for (int i = 0; i < t && q > 0; ++i)
                rl[i]++, q--;
        }
    }

    // now rl contains size of subtrees
    int r = 0;
    vector<int> f(n, 0);
    vector<int> perm(n);
    for (int i = 0; i < n; ++i)
        perm[i] = i;
    shuffle(perm.begin(), perm.end());
    vector<int> rperm(n);
    for (int i = 0; i < n; ++i)
        rperm[perm[i]] = i;
    for (int v : rl)
    {
        for (int i = 0; i < v; ++i)
            if (i > 0)
            {
r:;
                f[i + r] = rnd.wnext(i, w) + r;
                if (f[i + r] == i + r)
                    goto r;
            }
            else
                f[i + r] = -1;
        r += v;
    }
    int a, b;
    do
    {
        a = rnd.next(1, n);
        b = rnd.next(1, n);
    } while (a == b);
    cout << n << " " << a << " " << b << endl;
    vector<int> out(n);
    for (int i = 0; i < n; ++i)
    {
        if (f[perm[i]] == -1)
            out[i] = 0;
        else
            out[i] = rperm[f[perm[i]]] + 1;
    }
    for (int i = 0; i < n; ++i)
    {
        cout << out[i];
        if (i == n - 1)
            cout << endl;
        else
            cout << " ";
    }
    return 0;
}
