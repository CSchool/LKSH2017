#include <iostream>

using namespace std;

int main()
{
    int n, s, f;
    cin >> n >> s >> f;
    s--;
    f--;
    int adj[n][n];
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j)
            cin >> adj[i][j];
    int dist[n];
    bool used[n];
    for (int i = 0; i < n; ++i)
    {
        dist[i] = -1;
        used[i] = 0;
    }
    dist[s] = 0;
    while (1)
    {
        int v = -1;
        for (int j = 0; j < n; ++j)
        {
            if (!used[j] && dist[j] != -1)
            {
                if (v == -1 || dist[j] < dist[v])
                    v = j;
            }
        }
        if (v == -1)
            break;
        used[v] = 1;
        for (int j = 0; j < n; ++j)
        {
            if (adj[v][j] != -1)
            {
                int d = dist[v] + adj[v][j];
                if (dist[j] == -1 || d < dist[j])
                {
                    dist[j] = d;
                }
            }
        }
    }
    cout << dist[f] << endl;
    return 0;
}
