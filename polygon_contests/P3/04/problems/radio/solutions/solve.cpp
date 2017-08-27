#include <iostream>
#include <cmath>
#include <vector>

using namespace std;
int n;
vector<pair<long long, long long>> q;
vector<int> used;
long long M;
double m;
bool R = false;

void dfs(int v, int c)
{
    used[v] = c;
    for (int i = 0; i < n; ++i)
    {
        if (i == v) continue;
        double d = sqrt((q[v].first - q[i].first) * (q[v].first - q[i].first) + 
                    (q[v].second - q[i].second) * (q[v].second - q[i].second));
        if (d <= 2 * m)
        {
            if (!used[i])
            {
                dfs(i, 3 - c);
                if (R)
                    return;
            }
            else if (used[i] == c)
            {
                R = true;
                return;
            }
        }
    }
}

int main()
{
    cin >> n;
    for (int i = 0; i < n; ++i)
    {
        int a, b;
        cin >> a >> b;
        q.push_back(make_pair(a, b));
    }
    double l = 0;
    double r = 1e5;
    for (int _ = 0; _ < 100; ++_)
    {
        R = false;
        m = (l + r) / 2;
        used.assign(n, 0);
        for (int i = 0; i < n; ++i)
        {
            if (!used[i])
                dfs(i, 1);
            if (R) break;
        }
        if (R)
            r = m;
        else
            l = m;
    }
    cout.setf(ios::fixed);
    cout.precision(16);
    cout << m << endl;
    return 0;
}
