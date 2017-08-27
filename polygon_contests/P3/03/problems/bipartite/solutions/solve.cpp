#include <iostream>
#include <vector>

using namespace std;
int n;
vector<vector<int>> adj;
vector<int> cc;

void dfs(int v, int c)
{
    cc[v] = c;
    for (int u : adj[v])
    {
        if (cc[u] == c)
        {
            cout << "NO" << endl;
            exit(0);
        }
        if (cc[u] == 0)
        {
            dfs(u, 3 - c);
        }
    }
}

int main()
{
    cin >> n;
    adj.resize(n);
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            int t;
            cin >> t;
            if (t == 1)
            {
                adj[i].push_back(j);
                adj[j].push_back(i);
            }
        }
    }
    cc.resize(n, 0);
    for (int i = 0; i < n; ++i)
    {
        if (cc[i] == 0)
            dfs(i, 1);
    }
    cout << "YES" << endl;
    for (int i = 0; i < n; ++i)
    {
        cout << cc[i] << " ";
    }
    cout << endl;
    return 0;
}
