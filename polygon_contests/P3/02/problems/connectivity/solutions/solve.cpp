#include <iostream>
#include <vector>

using namespace std;
vector<bool> used;
vector<vector<int> > adj;

void dfs(int v)
{
    used[v] = 1;
    for (vector<int>::iterator it = adj[v].begin(); it != adj[v].end(); ++it)
    {
        if (!used[*it])
            dfs(*it);
    }
}

int main()
{
    int n, m;
    cin >> n >> m;
    used.resize(n, false);
    adj.resize(n);
    for (int i = 0; i < m; ++i)
    {
        int a, b;
        cin >> a >> b;
        adj[a - 1].push_back(b - 1);
        adj[b - 1].push_back(a - 1);
    }
    int ans = 0;
    for (int i = 0; i < n; ++i)
    {
        if (!used[i])
        {
            ans++;
            dfs(i);
        }
    }
    cout << ans << endl;
    return 0;
}
