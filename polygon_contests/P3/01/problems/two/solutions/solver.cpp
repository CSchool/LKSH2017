#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;
    vector<vector<bool>> adj(n, vector<bool>(n, false));
    for (int i = 0; i < m; ++i)
    {
        int a, b;
        cin >> a >> b;
        adj[a - 1][b - 1] = 1;
        adj[b - 1][a - 1] = 1;
    }

    auto q = adj;

    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            if (!adj[i][j]) continue;
            for (int k = 0; k < n; ++k)
            {
                if (!adj[j][k]) continue;
                q[i][k] = 1;
            }
        }
    }

    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            if (i == j) continue;
            if (!q[i][j])
            {
                cout << "NO\n";
                return 0;
            }
        }
    }
    cout << "YES\n";
}
