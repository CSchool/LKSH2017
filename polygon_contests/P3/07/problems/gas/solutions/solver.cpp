#include <iostream>
#include <vector>

using namespace std;

int main()
{
    int n;
    cin >> n;
    int cost[n];
    for (int i = 0; i < n; ++i)
        cin >> cost[i];
    int m;
    cin >> m;
    vector<int> adj[n];
    for (int i = 0; i < m; ++i)
    {
        int a, b;
        cin >> a >> b;
        a--;
        b--;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    bool used[n];
    int dist[n];
    for (int i = 0; i < n; ++i)
    {
        used[i] = 0;
        dist[i] = -1;
    }
    dist[0] = 0;
    while (1)
    {
        int v = -1;
        for (int i = 0; i < n; ++i)
        {
            if (!used[i] && dist[i] != -1)
            {
                if (v == -1 || dist[i] < dist[v])
                {
                    v = i;
                }
            }
        }
        if (v == -1)
            break;
        used[v] = 1;
        for (vector<int>::iterator it = adj[v].begin(); it != adj[v].end(); ++it)
        {
            int i = *it;
            int d = dist[v] + cost[i];
            if (dist[i] == -1 || dist[i] > d)
                dist[i] = d;
        }
    }
    if (dist[n - 1] == -1)
    {
        cout << -1 << endl;
    }
    else
    {
        cout << dist[n - 1] + cost[0] - cost[n - 1] << endl;
    }
    return 0;
}
