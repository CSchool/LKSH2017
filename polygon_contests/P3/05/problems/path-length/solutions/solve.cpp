#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int x[n][n];
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            cin >> x[i][j];
        }
    }
    int a, b;
    cin >> a >> b;
    a--;
    b--;
    queue<int> q;
    bool used[n];
    int par[n];
    memset(used, 0, sizeof used);
    q.push(a);
    used[a] = 1;
    par[a] = -1;

    while (!q.empty())
    {
        int v = q.front();
        q.pop();
        for (int u = 0; u < n; ++u)
        {
            if (x[v][u] && !used[u])
            {
                used[u] = 1;
                par[u] = v;
                q.push(u);
            }
        }
    }

    if (!used[b])
    {
        cout << -1 << endl;
    }
    else
    {
        int v = b;
        int t = 0;
        while (v != -1)
        {
            t++;
            v = par[v];
        }
        cout << t - 1 << endl;
    }
    return 0;
}
