#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> c;
vector<int> u;
int cc = 1;

void dfs(int v)
{
    u[v] = cc;
    for (int x : c[v])
        dfs(x);
}

int main()
{
    int n, a, b;
    cin >> n >> a >> b;
    a--;
    b--;
    c.resize(n);
    u.resize(n);
    for (int i = 0; i < n; ++i)
    {
        int p;
        cin >> p;
        if (p > 0)
            c[p - 1].push_back(i);
    }

    for (int i = 0; i < n; ++i)
    {
        if (!u[i])
        {
            dfs(i);
            cc++;
        }
    }
    cout << ((u[a] == u[b]) ? "YES" : "NO") << endl;
    return 0;
}
