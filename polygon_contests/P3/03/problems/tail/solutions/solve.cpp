#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> adj;

int main()
{
     int n, m;
     cin >> n >> m;
     adj.resize(n);
     for (int i = 0; i < m; ++i)
     {
         int a, b;
         cin >> a >> b;
         adj[a - 1].push_back(b - 1);
         adj[b - 1].push_back(a - 1);
     }
     int mm = 0;
     for (int r = 0; r < n; ++r)
     {
         if (adj[r].size() == 1)
         {
             int v = r;
             int p = -1;
             int l = 0;
             while (adj[v].size() <= 2)
             {
                 bool b = false;
                 if (p != -1)
                 {
                     if (adj[v].size() == 1)
                     {
                         l++;
                         break;
                     }
                 }
                 for (int x : adj[v])
                 {
                     if (x != p)
                     {
                         b = true;
                         p = v;
                         v = x;
                         l++;
                         break;
                     }
                 }
             }
             mm = max(l, mm);
         }
     }
     cout << mm << endl;
     return 0;
}
